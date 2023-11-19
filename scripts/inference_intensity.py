"""
Author: Jesher Joshua M
Email: jesherjoshua.m2021@vitstudent.ac.in

Description:
This script implements object detection and intensity tracking using YOLOv8 on video frames.
It detects objects, tracks their movements, and calculates intensity based on identified objects.

Libraries Used:
- OpenCV (cv2)
- Ultralytics YOLO and NAS
- Supervision
- NumPy
- SciPy

Note: Make sure to install the required libraries using pip install [library_name].
"""

# Import necessary libraries
import cv2
from ultralytics import YOLO
from ultralytics import NAS
import supervision as sv
import numpy as np
from scipy import spatial 
import robo_gen as rg

def mid_point(coord):
    """
    Calculate the mid-point of a bounding box given its coordinates.

    Args:
        coord (tuple): Coordinates in the format (x1, y1, x2, y2).

    Returns:
        tuple: Mid-point coordinates (x, y).
    """
    x1, y1, x2, y2 = coord
    x = (x1 + x2) / 2
    y = (y1 + y2) / 2

    return int(x), int(y)

def xyxy_to_xywh(xyxy):
    """
    Convert XYXY format (x, y top left and x, y bottom right) to XYWH format (x, y center point and width, height).

    Args:
        xyxy (list): List in the format [X1, Y1, X2, Y2].

    Returns:
        numpy.ndarray: Array in the format [X, Y, W, H].
    """
    if np.array(xyxy).ndim > 1 or len(xyxy) > 4:
        raise ValueError('xyxy format: [x1, y1, x2, y2]')
    x_temp = (xyxy[0] + xyxy[2]) / 2
    y_temp = (xyxy[1] + xyxy[3]) / 2
    w_temp = abs(xyxy[0] - xyxy[2])
    h_temp = abs(xyxy[1] - xyxy[3])
    return np.array([int(x_temp), int(y_temp), int(w_temp), int(h_temp)])

def bottom_mid(coords):
    """
    Calculate the bottom mid-point of a bounding box given its coordinates.

    Args:
        coords (tuple): Coordinates in the format (x1, y1, x2, y2).

    Returns:
        tuple: Bottom mid-point coordinates (x, y).
    """
    x1, y1, x2, y2 = coords
    x = (x1 + x2) // 2
    y = y2
    return int(x), int(y)

def distance(xy, xxyy):
    """
    Calculate the Euclidean distance between two points.

    Args:
        xy (tuple): Coordinates of the first point.
        xxyy (tuple): Coordinates of the second point.

    Returns:
        float: Euclidean distance between the two points.
    """
    return spatial.distance.euclidean(xy, xxyy)

def main():
    # Open video capture object
    cap = cv2.VideoCapture("./data/vid_long.mp4")
    
    # Get video properties
    input_fps = cap.get(cv2.CAP_PROP_FPS)
    w = int(cap.get(3))
    h = int(cap.get(4))
    
    # Load YOLO model
    model = YOLO('./models/yolov8n_nc4_trashcanext.pt')

    # Create a box annotator for visualization
    box_annotator = sv.BoxAnnotator(thickness=2, text_thickness=2, text_scale=1)

    # Initialize variables for tracking intensity
    intensity = 0
    count = 0
    divider = 1

    # Loop through video frames
    while cap.isOpened():
        print(f'count: {count}')
        ret, frame = cap.read()
        count += 1
        result = model(
            frame, agnostic_nms=True, device="mps", iou=0.45, conf=0.35
        )[0]
        detections = sv.Detections.from_yolov8(result)

        j = 9999
        k = None

        # Identify the object closest to the bottom of the frame
        for i in detections:
            if distance([bottom_mid(i[0])[1]], [h]) < j:
                j = distance([bottom_mid(i[0])[1]], [h])
                k = i

        labels = [f"{model.model.names[i[3]]} {i[2]:0.2f}" for i in detections]
        divider_monitor = True

        # Update intensity based on identified objects
        for i in labels:
            if i.lower().startswith('trash'):
                intensity += 1
                if divider_monitor:
                    divider += 1
                    divider_monitor = False

        frame = box_annotator.annotate(
            scene=frame, detections=detections, labels=labels
        )

        fps = 1 / (int(result.speed['inference']) * 0.001)

        cv2.putText(frame, "INPUT_FPS:" + str(input_fps), (10, 80), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), thickness=2)
        cv2.putText(frame, "OUTPUT_FPS:" + str(int(fps)), (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), thickness=2)
        cv2.imshow("yolov8", frame)
        print(f'Intensity: {intensity}, Divider: {divider}')

        # Generate fake location every 100 frames
        if count > 100:
            print(f'divider: {divider}')
            rg.gen_fake_loc(intensity // divider, 'intensity')
            count = 0
            intensity = 0
            divider = 1

        # Break the loop if 'Esc' key is pressed
        if cv2.waitKey(30) == 27:
            break

    # Release video capture object and close display window
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()

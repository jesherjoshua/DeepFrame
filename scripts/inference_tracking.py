
"""
Author: Jesher Joshua M
Email: jesherjoshua.m2021@vitstudent.ac.in

Description:
This script implements object tracking using YOLOv8 on video frames. It tracks objects, visualizes their paths,
and generates fake locations based on the tracking results.

Libraries Used:
- OpenCV (cv2)
- Ultralytics YOLO and NAS
- Supervision
- NumPy
- SciPy
- Collections

Note: Make sure to install the required libraries using pip install [library_name].
"""

import argparse
import cv2
from ultralytics import YOLO
from ultralytics import NAS
import supervision as sv
import numpy as np
from scipy import spatial 
import robo_gen as rg
from collections import defaultdict

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

def main(video_path):
    # Open video capture object
    cap = cv2.VideoCapture(video_path)
    
    # Load YOLO model
    model = YOLO('./models/yolov8n_nc4_trashcanext.pt')

    # Store the track history
    track_history = defaultdict(lambda: [])
    n = 0
    counter = 0

    # Loop through the video frames
    while cap.isOpened():
        counter += 1

        # Read a frame from the video
        success, frame = cap.read()

        if success:
            # Run YOLOv8 tracking on the frame, persisting tracks between frames
            results = model.track(frame, persist=True)

            # Get the boxes and track IDs
            boxes = results[0].boxes.xywh.cpu()
            try:
                track_ids = results[0].boxes.id.int().cpu().tolist()
            except:
                track_ids = []

            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Plot the tracks
            for box, track_id in zip(boxes, track_ids):
                n = track_id if track_id > n else n
                x, y, w, h = box
                track = track_history[track_id]
                track.append((float(x), float(y)))  # x, y center point

                if len(track) > 30:  # retain 90 tracks for 90 frames
                    track.pop(0)

                # Draw the tracking lines
                points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
                cv2.polylines(annotated_frame, [points], isClosed=False, color=(0, 0, 255), thickness=3)

            # Display the annotated frame
            cv2.imshow("YOLOv8 Tracking", annotated_frame)

            # Break the loop if 'q' is pressed
            if counter > 100:
                print(f'count: {n}')
                rg.generate_synthetic_location(n, 'count')
                counter = 0
                n = 0
                model = YOLO('./models/yolov8n_nc4_trashcanext.pt')

            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object and close the display window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    # Create an ArgumentParser object
    parser = argparse.ArgumentParser(description="Object tracking using YOLOv8 on video frames.")

    # Add an argument for the video_path parameter
    parser.add_argument('--video_path', type=str, required=True, help="Path to the input video.")

    # Parse the command line arguments
    args = parser.parse_args()

    # Call the main function with the specified video_path
    main(video_path=args.video_path)

import cv2
from ultralytics import YOLO
from ultralytics import NAS
import supervision as sv
import numpy as np
from scipy import spatial 
import robo_gen as rg
from collections import defaultdict

def mid_point(coord):
    x1, y1, x2, y2 = coord
    x = (x1 +  x2)/ 2
    y = (y1 + y2)/2

    return int(x), int(y)

def xyxy_to_xywh(xyxy):
    """
    Convert XYXY format (x,y top left and x,y bottom right) to XYWH format (x,y center point and width, height).
    :param xyxy: [X1, Y1, X2, Y2]
    :return: [X, Y, W, H]
    """
    if np.array(xyxy).ndim > 1 or len(xyxy) > 4:
        raise ValueError('xyxy format: [x1, y1, x2, y2]')
    x_temp = (xyxy[0] + xyxy[2]) / 2
    y_temp = (xyxy[1] + xyxy[3]) / 2
    w_temp = abs(xyxy[0] - xyxy[2])
    h_temp = abs(xyxy[1] - xyxy[3])
    return np.array([int(x_temp), int(y_temp), int(w_temp), int(h_temp)])
def bottom_mid(coords):
    x1,y1,x2,y2=coords
    x=(x1+x2)//2
    y=y2
    return int(x),int(y)

def distance(xy,xxyy):
    return spatial.distance.euclidean(xy,xxyy)
def main():

    cap = cv2.VideoCapture(
        "./data/vid_1.mp4"
    )
    # input_fps=cap.get(cv2.CAP_PROP_FPS)
    # w=int(cap.get(3))
    # h=int(cap.get(4))
    model = YOLO('./models/yolov8n_10e.pt')

    # model=NAS("yolo_nas_s")
    box_annotator = sv.BoxAnnotator(thickness=2, text_thickness=2, text_scale=1)
# Store the track history
    track_history = defaultdict(lambda: [])
    n=0
    # Loop through the video frames
    while cap.isOpened():
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
                track_ids=[]

            # Visualize the results on the frame
            annotated_frame = results[0].plot()

            # Plot the tracks
            for box, track_id in zip(boxes, track_ids):
                n= track_id if track_id>n else n
                x, y, w, h = box
                track = track_history[track_id]
                track.append((float(x), float(y)))  # x, y center point
                if len(track) > 30:  # retain 90 tracks for 90 frames
                    track.pop(0)

                # Draw the tracking lines
                points = np.hstack(track).astype(np.int32).reshape((-1, 1, 2))
                cv2.polylines(annotated_frame, [points], isClosed=False, color=(0,0,255), thickness=3)

            # Display the annotated frame
            cv2.imshow("YOLOv8 Tracking", annotated_frame)

            # Break the loop if 'q' is pressed

            if n!=0:
                rg.gen_fake_loc(n,'count')
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
        else:
            # Break the loop if the end of the video is reached
            break

    # Release the video capture object and close the display window
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()


import cv2
from ultralytics import YOLO
from ultralytics import NAS
import supervision as sv
import numpy as np
from scipy import spatial 
import robo_gen as rg

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
    input_fps=cap.get(cv2.CAP_PROP_FPS)
    w=int(cap.get(3))
    h=int(cap.get(4))
    model = YOLO('./models/yolov8n_10e.pt')

    # model=NAS("yolo_nas_s")
    box_annotator = sv.BoxAnnotator(thickness=2, text_thickness=2, text_scale=1)
    # size=(int(cap.get(3)),int(cap.get(4)))
    # writer = cv2.VideoWriter('filename.avi', cv2.VideoWriter_fourcc(*'MJPG'),10, size)
    intensity=0
    count = 0
    while True:
        ret, frame = cap.read()
        count += 8  # i.e. at 30 fps, this advances one second
        cap.set(cv2.CAP_PROP_POS_FRAMES, count)
        result = model(
            frame, agnostic_nms=True, device="mps", iou=0.45, conf=0.35
        )[0]
        detections = sv.Detections.from_yolov8(result)

        j=9999
        k=None
        for i in detections:
            if distance([bottom_mid(i[0])[1]],[h])<j:
                    j=distance([bottom_mid(i[0])[1]],[h])
                    k=i
            #cv2.circle(frame, mid_point(i[0]), 5, (0, 0, 255), -1)
        #cv2.drawMarker(frame, mid_point(k[0]), (0,0,255),cv2.MARKER_CROSS,120, 8)
        labels = [f"{model.model.names[i[3]]} {i[2]:0.2f}" for i in detections]
        for i in labels:
            if i.lower().startswith('trash'):
                intensity+=1
        # ndetections.append(i)
        frame = box_annotator.annotate(
            scene=frame, detections=detections, labels=labels
        )
        fps = 1/(int(result.speed['inference'])*0.001)
        # writer.write(frame)
        cv2.putText(frame,"INPUT_FPS:"+str(input_fps),(10,80),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,0),thickness=5)
        cv2.putText(frame,"OUTPUT_FPS:"+str(int(fps)),(10,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),thickness=5)
        cv2.imshow("yolov8", frame)
        print(f'Intensity: {intensity}')
        if intensity!=0:
            rg.gen_fake_loc(intensity)
        if cv2.waitKey(30) == 27:
            break


if __name__ == "__main__":
    main()

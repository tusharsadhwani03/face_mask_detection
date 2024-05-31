import os

from ultralytics import YOLO
import cv2

VIDEOS_DIR = 'Input Videos'

videos = os.listdir(VIDEOS_DIR)

path_list = [VIDEOS_DIR + '/' + video for video in videos]

for i in range(3):
    cap = cv2.VideoCapture(path_list[i])
    ret, frame = cap.read()

    H, W, _ = frame.shape

    out = cv2.VideoWriter('Output Videos' + '/' + videos[i], cv2.VideoWriter_fourcc(*'MP4V'), int(cap.get(cv2.CAP_PROP_FPS)), (W, H))


    model = YOLO('./detect/train/weights/best.pt')  # load a custom model

    threshold = 0.4

    while ret:

        results = model(frame)[0]

        for result in results.boxes.data.tolist():
            x1, y1, x2, y2, score, class_id = result

            if(class_id == 0):
                color = (255, 0, 0)
                label = "No Mask"
            else:
                color = (0,255,0)
                label = "Mask"

            if score > threshold:
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), color, 2)
                cv2.putText(frame, label, (int(x1), int(y1 - 10)),cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 3, cv2.LINE_AA)

    
        out.write(frame)
        ret, frame = cap.read()

    cap.release()
    out.release()
    cv2.destroyAllWindows()

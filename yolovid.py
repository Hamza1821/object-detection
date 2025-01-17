from ultralytics import YOLO
import cv2
import cvzone
cap=cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

model=YOLO('yolov8n.pt')
results=model("yolo/7.jpg", show=True)


while True:
    success, img =cap.read()
    results=model(img, stream=True)
    for r in results:
        boxes=r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2=int(x1), int(y1), int(x2), int(y2)
            cv2.rectangle(img,(x1,y1),(x2,y2),(255,0,255),3)
            
            print(x1, y1, x2, y2)

    
    cv2.waitKey(1)


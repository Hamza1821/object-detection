from ultralytics import YOLO 
import cv2
model=YOLO('yolov8l.pt')
results=model("yolo/7.jpg", show=True)
cv2.waitKey(0)
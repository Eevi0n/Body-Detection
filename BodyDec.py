import cv2
import mediapipe as mp
from cvzone.PoseModule import PoseDetector

detector = PoseDetector()
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    lmlist,bbox = detector.findPosition(img)
    
    #makes window
    cv2.imshow("Camera", img)
    #destroys window
    cv2.waitKey(1)

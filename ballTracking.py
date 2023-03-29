import cv2 as cv
import numpy as np

cap = cv.VideoCapture("opencvTutorial/videos/video.mp4")
# webcam cv.VideoCapture(0)


while cap.isOpened():
    ret, frame = cap.read()
    if ret is False:
        break
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_hue = np.array([21, 0, 0])
    upper_hue = np.array([45, 255, 255])

    

import cv2 as cv
import numpy as np

# from google.colab.patches import cv2_imshow

ball = []
cap = cv.VideoCapture("opencvTutorial/videos/video.mp4")
out = cv.VideoWriter(
    "output.avi", cv.VideoWriter_fourcc("M", "J", "P", "G"), 10, (1920, 1080)
)
while cap.isOpened():
    ret, frame = cap.read()
    if ret is False:
        break
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    lower_hue = np.array([21, 0, 0])
    upper_hue = np.array([45, 255, 255])
    mask = cv.inRange(hsv, lower_hue, upper_hue)

    (contours, _) = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    center = None

    if len(contours) > 0:
        c = max(contours, key=cv.contourArea)
        ((x, y), radius) = cv.minEnclosingCircle(c)
        M = cv.moments(c)
        try:
            center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
            cv.circle(frame, center, 10, (255, 0, 0), -1)
            ball.append(center)
        except:
            pass
        if len(ball) > 2:
            for i in range(1, len(ball)):
                cv.line(frame, ball[i - 1], ball[i], (0, 0, 255), 5)
    out.write(frame)
out.release()

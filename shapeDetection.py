import cv2 as cv
import numpy as np

img = cv.imread("opencvTutorial/images/shapes.png")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret, trhesh = cv.threshold(gray, 50, 255, 1)
contours, h = cv.findContours(trhesh, 1, 2)

cv.imshow("Shapes", trhesh)
cv.waitKey(0)

for cnt in contours:
    approx = cv.approxPolyDP(cnt, 0.01 * cv.arcLength(cnt, True), True)
    n = len(approx)
    if n == 4:
        # this is a square
        cv.drawContours(img, [cnt], 0, 255, 5)
    if n == 6:
        # this is a hexagon
        cv.drawContours(img, [cnt], 0, 255, 5)
    if n == 3:
        # this is a triangle
        cv.drawContours(img, [cnt], 0, 255, 5)
    if n >= 9:
        # this is a square
        cv.drawContours(img, [cnt], 0, 255, 5)

cv.imshow("Shapes", img)
cv.waitKey(0)

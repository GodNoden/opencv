import cv2 as cv
import numpy as np

image = cv.imread("images/original.jpg")
cv.imshow("Tea", image)
cv.waitKey(0)

# Edge detection
gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
canny = cv.Canny(gray, 150, 200)
cv.imshow("Tea", canny)
cv.waitKey(0)

# Erosion and dilation 
kernel = np.ones((5, 5), np.int8)

# Dilation
dilate_image = cv.dilate(canny, kernel, iterations=1)
cv.imshow("Tea", dilate_image)
cv.waitKey(0)

# Erosion 
erode_image = cv.erode(canny, kernel, iterations=1)
cv.imshow("Tea", erode_image)
cv.waitKey(0)

display = np.hstack((canny, dilate_image, erode_image))
cv.imshow('Display', display)
cv.waitKey(0)

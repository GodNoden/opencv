import cv2 as cv
import numpy as np

image = cv.imread("opencvTutorial/images/lion.jpg")
cv.imshow("Image", image)
cv.waitKey(0)
dst = cv.fastNlMeansDenoisingColored(image, None, 20, 20, 7, 15)
cv.imshow("Image", dst  )
cv.waitKey(0)

import cv2 as cv
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
# uint8: 0 to 255

# Drawing Function
# Draw a circle
cv.circle(img, (100, 100), 50, (0, 255, 0), 5)

# Draw a rectangle
cv.rectangle(img, (200, 200), (400, 500), (0, 0, 255), 5)

# Draw a line
cv.line(img, (160, 160), (359, 29), (255, 0, 0), 3)

# Draw a text
cv.putText(img, "morning", (160, 160), cv.FONT_HERSHEY_COMPLEX, 2, (0, 255, 255), 4)
#Display
cv.imshow("Circle", img)
cv.waitKey(0)

import cv2 as cv
import numpy as np

# BGR Image . It's represented in Blue, Green and Red channels
image = cv.imread("opencvTutorial/images/shapes.png")
cv.imshow("Shapes", image)
cv.waitKey(0)

hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
cv.imshow("Hsv", hsv)
# cv.waitKey(0)

# Blue Color Triangle
lower_hue = np.array([65, 0, 0])
upper_hue = np.array([110, 255, 255])


def nothing(x):
    pass


red_hue = cv.createTrackbar("R", "Hsv", 0, 255, nothing)
green_hue = cv.createTrackbar("G", "Hsv", 0, 255, nothing)
blue_hue = cv.createTrackbar("B", "Hsv", 0, 255, nothing)
upper_hue = np.array([255, 255, 255])


# Red color
while True:
    # lower_hue = np.array([0, 0, 0])
    valueRed = cv.getTrackbarPos("B", "Hsv")
    valueGreen = cv.getTrackbarPos("G", "Hsv")
    valueBlue = cv.getTrackbarPos("B", "Hsv")

    lower_hue = np.array([valueBlue, valueGreen, valueRed])
    mask = cv.inRange(hsv, lower_hue, upper_hue)
    result = cv.bitwise_and(image, image, mask=mask)
    cv.imshow("Mask", result)

    if cv.waitKey(1) & 0xFF == ord("q"):
        break

cv.destroyAllWindows()

# # Green color
# lower_hue = np.array([46, 0, 0])
# upper_hue = np.array([])

# mask = cv.inRange(hsv, lower_hue, upper_hue)
# result = cv.bitwise_and(image, image, mask=mask)
# cv.imshow("Mask", result)
# cv.waitKey(0)

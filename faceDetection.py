import cv2 as cv

face_cascade = cv.CascadeClassifier(
    "opencvTutorial/files/haarcascade_frontalface_default.xml"
)

img = cv.imread("opencvTutorial/images/group.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.3, 5)
# print(faces)

for x, y, w, h in faces:
    cv.rectangle(
        img,
        (x, y),
        (x + w, y + h),
        (0, 255, 0),
        3,
    )

cv.imshow("Person", img)
cv.waitKey(0)

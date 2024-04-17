#import cv2
#img = cv2.imread("punit.jpg")
#imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Gray Image", imgGray)
#cv2.waitKey(0)

#import cv2
#img = cv2.imread("punit.jpg")
#imgCanny = cv2.Canny(img, 150, 200)
#cv2.imshow("Canny Image", imgCanny)
#cv2.waitKey(0)

import cv2

face_Cascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

image = cv2.imread('punit.jpg')
imgGray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

faces = face_Cascade.detectMultiScale(imgGray, 1.1, 4)

for (x, y, w, h) in faces:
  cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

cv2.imshow("Result", image)
cv2.waitKey(0)
import cv2
import cv2.data

face_detectr = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img = cv2.imread("detetettttt.jpeg")

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

detected = face_detectr.detectMultiScale(gray_img, 1.2, 4)

for x, y, w, h in detected:
    cv2.rectangle(img, (x, y), (x+w, y+h), (10, 255, 10), 2)

    cv2.imshow("detected faces", img)

cv2.waitKey(0)
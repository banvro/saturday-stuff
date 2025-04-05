import cv2
import cv2.data

capture = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")


while True:
    isTrue, frame = capture.read()

    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_detector.detectMultiScale(gray_frame, 1.5, 4)

        # (x-axis, y-axix, width, height)
    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (12, 244, 100), 3)

    cv2.imshow("read faces", frame)

    if cv2.waitKey(20) & 0xff == ord("e"):
        break
import cv2

capture = cv2.VideoCapture(0)

while True:
    isTrue, frame = capture.read()

    cv2.imshow("my camra", frame)

    if cv2.waitKey(20) & 0xff == ord("q"):
        break
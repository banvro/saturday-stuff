import cv2

capure = cv2.VideoCapture(0)

while True:
    x, frame = capure.read()
    cv2.imshow("videoooo", frame)

    blur_fm = cv2.GaussianBlur(frame, (13, 13), 0)
    cv2.imshow("gray videp", blur_fm)

    if cv2.waitKey(20) & 0xff == ord("w"):
        break
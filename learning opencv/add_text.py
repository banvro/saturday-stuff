import cv2

img = cv2.imread("740full-kristina-pimenova.jpg")

showing = cv2.putText(img, "hellow world", (100, 100), cv2.FONT_HERSHEY_PLAIN, 2, (10, 255, 20), 3)

ee = cv2.circle(showing, (200, 300), 150, (10, 200, 80), -1)

cv2.imshow("eeeeeee", ee)


cv2.waitKey(0)
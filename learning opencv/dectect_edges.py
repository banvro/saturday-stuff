import cv2

img = cv2.imread("740full-kristina-pimenova.jpg")
cv2.imshow("kristina pemenova", img)

detect_eges = cv2.Canny(img, 50, 100)
cv2.imshow("edges", detect_eges)

cv2.waitKey(0)
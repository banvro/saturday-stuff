import cv2

img = cv2.imread("740full-kristina-pimenova.jpg")
cv2.imshow("kristina pemenova", img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray_image", gray_img)

bluring = cv2.GaussianBlur(gray_img, (7, 7), 0)
cv2.imshow("blured image", bluring)

detect_eges = cv2.Canny(bluring, 50, 100)
cv2.imshow("edges", detect_eges)

cv2.waitKey(0)
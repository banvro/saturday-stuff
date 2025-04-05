import cv2

img = cv2.imread("740full-kristina-pimenova.jpg")
cv2.imshow("kristina pemenova", img)

img_blur = cv2.GaussianBlur(img, (11, 11), 0)
cv2.imshow("blur image", img_blur)

cv2.waitKey(0)
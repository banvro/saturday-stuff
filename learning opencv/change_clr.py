import cv2

img = cv2.imread("740full-kristina-pimenova.jpg")
cv2.imshow("kritina permenova", img)

gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow("gray image", gray_img)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow("hsv image", hsv)


cv2.waitKey(0)
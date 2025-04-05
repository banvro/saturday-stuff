import cv2
import numpy as np


img_ary = np.zeros((700, 700))

do_soming = cv2.rectangle(img_ary, (50, 50), (400, 400), (100, 78, 15), 3)

cv2.imshow("black image", do_soming)

cv2.waitKey(0)


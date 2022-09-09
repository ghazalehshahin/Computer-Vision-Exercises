import numpy as np
import cv2 as cv
import sys

img1 = cv.imread("images/bicycle.png")
img2 = cv.imread("images/fruit.png")

rows, cols, channels = img2.shape
roi = img1[0:rows, 0:cols]

# cv.imshow("roi" , roi)

img2gray = cv.cvtColor(img2, cv.COLOR_BGR2GRAY)
# cv.imshow("img2gray" , img2gray)

ret, mask = cv.threshold(img2gray, 240, 255, cv.THRESH_BINARY)
# cv.imshow("mask", mask)
# print(ret)

mask_inv = cv.bitwise_not(mask)
# cv.imshow("mask inverse", mask_inv)

img1_bg = cv.bitwise_and(roi, roi, mask=mask)
img2_fg = cv.bitwise_and(img2, img2, mask=mask_inv)
# cv.imshow("img1_bg", img2_fg)

dst = cv.add(img1_bg, img2_fg)
img1[0:rows, 0:cols] = dst
cv.imshow("final result", img1)
cv.waitKey(0)
cv.destroyAllWindows()
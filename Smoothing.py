import cv2 as cv

img = cv.imread('images/Ghazal.jpg')

blurred_img = cv.bilateralFilter(img, 9, 250,500)
cv.imshow('blurred image', blurred_img)
cv.waitKey(0)
cv.destroyAllWindows()
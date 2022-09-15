import sys
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


img = cv.imread('images/Ghazal.jpg')
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# img_gray_res = cv.resize(img_gray,dsize=(600,400))
ret, thresh1 = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY)
ret, thresh2 = cv.threshold(img_gray, 127, 255, cv.THRESH_BINARY_INV)
ret, thresh3 = cv.threshold(img_gray, 127, 255, cv.THRESH_TRUNC)
ret, thresh4 = cv.threshold(img_gray, 127, 255, cv.THRESH_TOZERO)
ret, thresh5 = cv.threshold(img_gray, 127, 255, cv.THRESH_TOZERO_INV)
thresh6 = cv.adaptiveThreshold(img_gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,2)
thresh7 = cv.adaptiveThreshold(img_gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
noisyImage = cv.imread('images/noisy.jpg')
# noisyImageGray = cv.cvtColor(noisyImage,cv.COLOR_BGR2GRAY)
img_gray_blur = cv.GaussianBlur(img_gray,(5,5), 0)
ret, thresh8 = cv.threshold(img_gray, 0, 255, cv.THRESH_BINARY+cv.THRESH_OTSU)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV', 'Adaptive Mean Thresholding',
 'Adaptive Gaussian Thresholding', 'Gaussian filtered Image', 'Otsu_Thresholding']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5, thresh6, thresh7, img_gray_blur, thresh8]

for i in range(10):
    plt.subplot(2,5,i+1),plt.imshow(images[i],'gray',vmin=0,vmax=255)
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()       

# cv.imshow("hsv-image", img_simple_threshold_binary)
# cv.waitKey(0)
# cv.destroyAllWindows()          
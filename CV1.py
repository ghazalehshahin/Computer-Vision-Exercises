import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys
# img = cv.imread ('dolphin.png')
# img = cv.imread ('bicycle.png')
img = cv.imread ('images/fruit.png')

##show image and wait
# cv.imshow("image", img)
# cv.waitKey(0)
# cv.destroyAllWindows()


##check for availability
if img is None:
    sys.exit("Could not read the image.")


##size and shape of image
# img.shape


##get data from a special part of picture
# for i in range (101, 104):
#     for j in range (201, 204):
#        print(img[i,j])

##cropping an image
# print(img.shape)
# cv.imshow("original", img)
# cropped_img = img[110:310, 10:160]
# print(cropped_img.shape)
# cv.imshow("cropped", cropped_img)

##working with colors
# cv.imshow("colored image", img)
red_img = img [:,:,1]
# print(red_img.shape)
# cv.imshow("red img", red_img)
color = ('b','g','r')
for i,col in enumerate(color):
    histr = cv.calcHist([img],[i],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.show()
cv.waitKey(0)
cv.destroyAllWindows()
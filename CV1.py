import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import sys
img = cv.imread ('dolphin.png')
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
for i in range (101, 104):
    for j in range (201, 204):
       print(img[i,j])
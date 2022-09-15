import cv2 as cv
import numpy as np
import sys

img = cv.imread('images/fruit.png')
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

color_dict_HSV = {
              'red': [[9, 255, 255], [0, 50, 70]],
              'green': [[89, 255, 255], [36, 50, 70]],
              'yellow': [[35, 255, 255], [25, 50, 70]]
}

for i in color_dict_HSV:
  mask = cv.inRange(hsv,np.array(color_dict_HSV.get(i)[1]), np.array(color_dict_HSV.get(i)[0]))
  res = cv.bitwise_and(img,img,mask=mask)
  cv.imshow("object", res)
  cv.waitKey(0)
cv.destroyAllWindows()
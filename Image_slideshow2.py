from unittest import result
import cv2 as cv
import numpy as np
from math import ceil
import os
import time
import sys

def getImagePath():
    dst = "images/"
    images = os.listdir(dst)
    length = len(images)
    return [dst, images, length]

def getImage(array, i):
    img = cv.imread(array[0] + array[1][i])
    if img is None:
        sys.exit("couldnt read file")
    img = cv.resize(img, (360,360))
    return img

def slideShow(array, i, alpha, result, img):
    while(True):
        if(ceil(alpha) == 0):
            alpha = 1.0
            i = (i+1) % array[2]
            img = getImage(array, i)
        alpha -= 0.01
        result = cv.addWeighted(result, alpha, img, 1-alpha, 0)
        cv.imshow("slide show", result)
        time.sleep(0.002)
        key = cv.waitKey(1) & 0xff
        if key == ord('q'):
            break

def main():
    result = np.zeros((360, 360, 3) , np.uint8)
    index = 1
    alpha = 1.0
    e1 = cv.getTickCount()
    ImageData = getImagePath()
    e2 = cv.getTickCount()
    time = (e2-e1)/cv.getTickFrequency()
    print("time: ", time)
    img = getImage(ImageData, index)
    slideShow(ImageData, index, alpha, result, img)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
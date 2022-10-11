from glob import glob
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('images/fruit.png', cv.IMREAD_GRAYSCALE)
edge = img.copy()

def nothing():
    pass

def make_trackbar():
    cv.createTrackbar('Maximum Value', 'Edge_Detector', 255, 255, nothing)
    cv.createTrackbar('Minimum Value', 'Edge_Detector', 0, 255, nothing)

def canny_edge_detector(event,x,y,flags,param):
    global img, edge
    max = cv.getTrackbarPos('Maximum Value', 'Edge_Detector')
    min = cv.getTrackbarPos('Minimum Value', 'Edge_Detector')
    if event == cv.EVENT_LBUTTONDOWN:
        edge = cv.Canny(img, min, max)

def plotting_images(img1, img2):
    plt.figure((10,10))
    plt.subplot(121)
    plt.imshow(img1[1])
    plt.title(img1[0])
    plt.subplot(122)
    plt.imshow(img2[1])
    plt.title(img2[0])
    plt.show()

def main():
    cv.namedWindow('Edge_Detector')
    make_trackbar()
    cv.setMouseCallback('Edge_Detector',canny_edge_detector)
    while(1):
        cv.imshow('Edge_Detector',edge)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break
    cv.destroyAllWindows()

if __name__ == '__main__':
    main()
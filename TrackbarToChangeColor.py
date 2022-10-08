import numpy as np
import cv2 as cv


def nothing(x):
    pass

def trackbar(switch):
    cv.createTrackbar('R','image',0,255,nothing)
    cv.createTrackbar('G','image',0,255,nothing)
    cv.createTrackbar('B','image',0,255,nothing)
    cv.createTrackbar(switch, 'image',0,1,nothing)

def main():
    switch = '0 : OFF \n1 : ON'
    img = np.zeros((300,512,3), np.uint8)
    cv.namedWindow('image')
    trackbar(switch)
    while(1):
        cv.imshow('image',img)
        k = cv.waitKey(1) & 0xFF
        if k == 27:
            break
        r = cv.getTrackbarPos('R','image')
        g = cv.getTrackbarPos('G','image')
        b = cv.getTrackbarPos('B','image')
        s = cv.getTrackbarPos(switch,'image')
        if s == 0:
            img[:] = 0
        else:
            img[:] = [b,g,r]
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
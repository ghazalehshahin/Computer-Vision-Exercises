import cv2 as cv
import numpy as np

def main():
    img = np.zeros((512,2000,3), np.uint8)
    cv.ellipse(img, (340,250), (64,64), 312, 0, 280, (255,0,0), 24)
    cv.ellipse(img, (160,250), (64,64), 0, 0, 280, (0,255,0), 24)
    cv.ellipse(img, (250,110), (64,64), 130, 0, 280, (0,0,255), 24)
    cv.putText(img, "OpenCV", (460, 250), cv.FONT_HERSHEY_DUPLEX, 6, (255,255,255), 16)
    cv.imshow("opencv-logo", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

if __name__ == "__main__":
    main()
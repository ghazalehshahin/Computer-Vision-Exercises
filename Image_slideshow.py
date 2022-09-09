import numpy as np
import cv2 as cv
import sys
import glob
import imutils

images = [cv.imread(file) for file in glob.glob("images/*.png")]
rimgs = []
for image in images:
    if image is None:
        sys.exit("could not read the file")
    print(image.shape)
    image = imutils.resize(image, width=1280, height=1280)
    rimgs.append(image)

i = 0
results = []
for image in rimgs:
    alpha = 0
    if i<(len(rimgs)-1):
        while(alpha <= 1):
            dst = cv.addWeighted(image, alpha, rimgs[i+1], 1-alpha, 0)
            results.append(dst)
            alpha+=0.2
    i+=1
# print(len(results))
for r in results:
    cv.imshow("slider", r)
    cv.waitKey(0)
cv.destroyAllWindows()





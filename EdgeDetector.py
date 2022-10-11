from email.mime import image
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def sobel_edge_detector(img):
    grad_x = cv.Sobel(img, cv.CV_64F, 1, 0, 7)
    A = cv.convertScaleAbs(grad_x)
    grad_y = cv.Sobel(img, cv.CV_64F, 0, 1, 7)
    B = cv.convertScaleAbs(grad_y)
    img = cv.addWeighted(A, 0.5, B, 0.5, 0)
    return img

def laplacian_edge_detector(img):
    lap_img = cv.Laplacian(img, cv.CV_64F)
    return lap_img

def plotting_images(images):
    plt.figure(figsize=(10,10))
    for i in range (len(images)):
        plt.subplot(1,len(images),i+1)
        plt.imshow(images[i][1], cmap='gray')
        plt.title(images[i][0])
    plt.show()

def main():
    images = []
    frizzy = cv.imread('images/frizzy.png', cv.IMREAD_GRAYSCALE)
    frizzy_sobel = sobel_edge_detector(frizzy)
    images.append(('sobel_version',frizzy_sobel))
    frizzy_laplacian = laplacian_edge_detector (frizzy)
    images.append(('laplacian_version',frizzy_laplacian))
    plotting_images(images)

if __name__ == '__main__':
    main()
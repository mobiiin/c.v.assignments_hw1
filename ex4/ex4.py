import cv2 as cv
from matplotlib import pyplot as plt
import numpy as np

img1 = cv.imread('1.jpg', 0)
img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)
img2 = cv.imread('2.jpg', 0)
img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)

sobel_x = cv.Sobel(img1, cv.CV_64F, 1, 0)  # detects vertical change in color intensities
sobel_x1 = np.uint8(np.absolute(sobel_x))  # returns only 0 or 255 for each pixel
sobel_y = cv.Sobel(img1, cv.CV_64F, 0, 1)  # detects horizontal change in color intensities
sobel_y1 = np.uint8(np.absolute(sobel_y))
sobel_combined1 = cv.bitwise_or(sobel_x1, sobel_y1)  # adds two images pixel wise

canny1 = cv.Canny(img1, 100, 200)  # applying canny edge detector

log1 = cv.Laplacian(img1, cv.CV_64F)
log1 = np.uint8(np.absolute(log1))

sobel_x = cv.Sobel(img2, cv.CV_64F, 1, 0)
sobel_x2 = np.uint8(np.absolute(sobel_x))
sobel_y = cv.Sobel(img2, cv.CV_64F, 0, 1)
sobel_y2 = np.uint8(np.absolute(sobel_y))
sobel_combined2 = cv.bitwise_or(sobel_x2, sobel_y2)

canny2 = cv.Canny(img2, 100, 200)

log2 = cv.Laplacian(img2, cv.CV_64F)
log2 = np.uint8(np.absolute(log2))

titles = ['original1', 'sobel_x1', 'sobel_y1', 'sobel_combined1', 'canny1', 'log1']
images = [img1, sobel_x1, sobel_y1, sobel_combined1, canny1, log1]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

titles = ['original2', 'sobel_x2', 'sobel_y2', 'sobel_combined2', 'canny2', 'log2']
images = [img2, sobel_x2, sobel_y2, sobel_combined2, canny2, log2]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
# I recommend bilateral filter , it removes the noise with respect to the edges

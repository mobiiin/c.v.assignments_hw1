import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('limbo.png', 1)
_, binary = cv.threshold(img, 60, 255, cv.IMREAD_GRAYSCALE)  # transmutes the image to binary
kernel = np.ones((2, 2), np.uint8)  # creates a square as a sampling criteria while applying the filters

dilation = cv.dilate(binary, kernel, iterations=16)
erosion = cv.erode(binary, kernel, iterations=16)
# first erosion then dilation will be performed on image
opening = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=16)
closing = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel, iterations=16)  # first dilation then erosion

titles = ['original', 'binary', 'dilation', 'erosion', 'opening', 'closing']
images = [img, binary, dilation, erosion, opening, closing]

for i in range(6):
    plt.subplot(2, 3, i+1)  # acts exactly as subplot of matlab
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])  # hides the x y rulers
plt.show()

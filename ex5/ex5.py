import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('limbo.png', 1)
_, binary = cv.threshold(img, 60, 255, cv.IMREAD_GRAYSCALE)  # transmutes the image to binary
kernel = np.ones((2, 2), np.uint8)  # creates a square as a sampling criteria while applying the filters

# the following filters go through the whole picture applying the kernel
# for instance the dilation assigns all the pixels of kernel to 1 even if only one of them are 1
# therefore the results looks like the white area is advancing and the black area is receding
# the opposite scenario happens in erosion
dilation = cv.dilate(binary, kernel, iterations=8)
erosion = cv.erode(binary, kernel, iterations=8)
opening = cv.morphologyEx(binary, cv.MORPH_OPEN, kernel, iterations=8)  # first erosion then dilation will be performed on image
closing = cv.morphologyEx(binary, cv.MORPH_CLOSE, kernel, iterations=8)  # first dilation then erosion

titles = ['original', 'binary', 'dilation', 'erosion', 'opening', 'closing']
images = [img, binary, dilation, erosion, opening, closing]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])  # hides the x y rulers
plt.show()

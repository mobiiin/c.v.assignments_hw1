import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('2.jpg', 0)
# change from BGR to RGB for viewing in pyplot
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# resizing the picture to 400*300
img1 = cv.resize(img, (400, 300), interpolation=cv.INTER_AREA)

# creating gaussian kernel
kernel = np.array(([1, 2, 1], [2, 4, 2], [1, 2, 1]), np.float32)/16
# applying the kernel to the image
blur = cv.filter2D(img1, -1, kernel)  # -1 is the depth which keeps it equal to the original

# zero-padding, adds a row of zero pixels to every border
blurz = cv.copyMakeBorder(blur, 1, 1, 1, 1, cv.BORDER_CONSTANT, value=0)
# creating the vertical kernel
vertk = np.array(([0, -1, 1]), np.float32)
vert = cv.filter2D(blurz, -1, vertk)
# adding a fixed value to each pixel to make the image more visible
vert = vert + 127*np.ones(vert.shape, np.uint8)
# saving the image
cv.imwrite('vert.jpg', vert)

# creating the horizontal kernel
horik = np.array(([0], [-1], [1]), np.float32)
hori = cv.filter2D(blurz, -1, horik)
hori = hori + 127*np.ones(hori.shape, np.uint8)
cv.imwrite('hori.jpg', hori)

# the final e=image is obtained from adding vertical and horizontal together
edge = vert + hori
# creating the binary image
_, edge_bin = cv.threshold(edge, 20, 255, cv.IMREAD_GRAYSCALE)
cv.imwrite('edge.jpg', edge_bin)

# high passed image
hpf = img1 - blur
# adding a fixed value to each pixel to make the image more visible
hpf = hpf + 127*np.ones(img1.shape, np.uint8)
cv.imwrite('highpf.jpg', hpf)

titles = ['original', 'blurred', 'vertical', 'horizontal', 'edge', 'high passed image']
images = [img1, blur, vert, hori, edge_bin, hpf]

for i in range(6):
    plt.subplot(2, 3, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()

import cv2 as cv
import numpy as np
import math

img = cv.imread('space.jpg', 1)
height, width = img.shape[:2]
point1 = (100, 100)
point2 = (1180, 100)


def degree1(x):
    degree = cv.getTrackbarPos('rot_degree', 'image')
    rotation_matrix = cv.getRotationMatrix2D((width / 2, height / 2), degree, 1)
    rotated_image = cv.warpAffine(img, rotation_matrix, (width, height))  # applies a transformation matrix to an image
    horizontal = np.concatenate((img, rotated_image), axis=1)
    x0 = 3*width/2
    y0 = height/2
    alpha = degree * math.pi/180
    x2 = ((1180 - x0) * math.cos(alpha)) + ((100 - y0) * math.sin(alpha)) + x0
    y2 = (-(1180 - x0) * math.sin(alpha)) + ((100 - y0) * math.cos(alpha)) + y0
    point3 = (int(x2), int(y2))
    cv.line(horizontal, point1, point3, (0, 0, 255), 2)
    cv.imshow('image', horizontal)


cv.namedWindow('image')
cv.resizeWindow('image', 1080, 1920)
cv.createTrackbar('rot_degree', 'image', 0, 360, degree1)

# concatenate image Horizontally , connect two pictures toward x axis
horizontal1 = np.concatenate((img, img), axis=1)
cv.imshow('image', horizontal1)

cv.waitKey(0) & 0xFF
cv.destroyAllWindows()

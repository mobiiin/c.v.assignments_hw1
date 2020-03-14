import cv2 as cv
import numpy as np

img = cv.imread("3.jpg", 0)
# creating the parameters for blob detector
params = cv.SimpleBlobDetector_Params()
# this thresholds determine whether the detector will find the blob or not based on tits pixel value
params.minThreshold = 100
params.maxThreshold = 255
# filter by Area
params.filterByArea = True
params.minArea = 100
# filter by circularity
params.filterByCircularity = True
params.minCircularity = 0.5
# filter by convexity
params.filterByConvexity = True
params.minConvexity = 0.3
# filter by inertia
params.filterByInertia = True
params.minInertiaRatio = 0.4
# creating a blob detector
detector = cv.SimpleBlobDetector_create(params)
# applying the detector on the image
blobs = detector.detect(img)
# draw a red circle around the detected blob
img_blobs = cv.drawKeypoints(img, blobs, np.array([]), (0, 0, 255),
                             cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle corresponds to the size of blob
cv.imshow("image", img_blobs)
cv.waitKey(0)

import cv2
import numpy as np
img = cv2.imread('football.jpg', 1)
cv2.rectangle(img, (300, 455), (375, 530), (0, 255, 0), 2)
cv2.imshow('football', img)
dimension = img.shape
print(dimension)
img1 = cv2.imread('football.jpg', 1)
ball = img1[455:530, 300:375]
img1[460:535, 600:675] = ball
cv2.imshow('football1', img1)
cv2.imwrite('football_f.jpg', img1)
# create a mask around the ball
# ball_m = np.zeros(ball.shape, ball.dtype)
# b_cor = (360, 690)
# final = cv2.seamlessClone(ball, img, ball_m, b_cor, cv2.NORMAL_CLONE)
# cv2.imshow('final', final)
cv2.waitKey(0)
cv2.destroyAllWindows()


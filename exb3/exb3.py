import cv2 as cv
import numpy as np

cap = cv.VideoCapture('webcam.mp4')

fourcc = cv.VideoWriter_fourcc(*'X264')  # adding mp4 codec for saving
cannyf = cv.VideoWriter('cannyf.mp4', fourcc, 20, (640, 480))  # saves the video
sobelf = cv.VideoWriter('sobelf.mp4', fourcc, 20, (640, 480))
prewittf = cv.VideoWriter('prewittf.mp4', fourcc, 20, (640, 480))

cannyg = cv.VideoWriter('cannyg.mp4', fourcc, 20, (640, 480))
sobelg = cv.VideoWriter('sobelg.mp4', fourcc, 20, (640, 480))
prewittg = cv.VideoWriter('prewittg.mp4', fourcc, 20, (640, 480))

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    if ret == 1:
        frame1 = cv.GaussianBlur(frame, (5, 5), 0)
        frame = [frame, frame1]  # the first frame is original and second frame is gaussian filtered
        for i in range(2):
            # first loop is for applying the filter to original frame, the second loop is for the gaussian filtered one
            # canny
            canny = cv.Canny(frame[i], 100, 200)
            if i == 1:
                cannyf.write(canny)
            else:
                cannyg.write(canny)

            # sobel
            sobel_x = cv.Sobel(frame[i], cv.CV_64F, 1, 0)  # detects vertical change in color intensities
            sobel_x = np.uint8(np.absolute(sobel_x))
            sobel_y = cv.Sobel(frame[i], cv.CV_64F, 0, 1)  # detects horizontal change in color intensities
            sobel_y = np.uint8(np.absolute(sobel_y))
            sobel = cv.bitwise_or(sobel_x, sobel_y)
            if i == 1:
                sobelf.write(sobel)
            else:
                sobelg.write(sobel)

            # prewitt
            kernel_x = np.array([[1, 1, 1], [0, 0, 0], [-1, -1, -1]])
            kernel_y = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
            prewitt_x = cv.filter2D(frame[i], -1, kernel_x)
            prewitt_y = cv.filter2D(frame[i], -1, kernel_y)
            prewitt = prewitt_x + prewitt_y
            if i == 1:
                prewittf.write(prewitt)
            else:
                prewittg.write(prewitt)

    else:
        break


cap.release()
cannyf.release()
sobelf.release()
prewittf.release()
cannyg.release()
sobelg.release()
prewittg.release()

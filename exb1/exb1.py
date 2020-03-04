import cv2 as cv

video = cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'X264')
webcam = cv.VideoWriter('webcam.mp4', fourcc, 20, (640, 480))
i = 0
while 1:
    (ret, frame) = video.read()
    cv.imshow('webcam', frame)
    k = cv.waitKey(1) & 0xFF

    if k == ord('s') or i == 1:
        webcam.write(frame)
        i = 1
    if k == ord('e'):
        break


video.release()
webcam.release()
cv.destroyAllWindows()

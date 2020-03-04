import cv2 as cv

video = cv.VideoCapture(0)  # reads video from webcam
fourcc = cv.VideoWriter_fourcc(*'X264')  # adding mp4 codec for saving
webcam = cv.VideoWriter('webcam.mp4', fourcc, 20, (640, 480))  # saves the video
i = 0
while 1:
    (ret, frame) = video.read()  # starts reading video and adding them to frame
    cv.imshow('webcam', frame)
    k = cv.waitKey(1) & 0xFF

    if k == ord('s') or i == 1:
        webcam.write(frame)  # runs the webcam code above
        i = 1
    if k == ord('e'):
        break

video.release()
webcam.release()
cv.destroyAllWindows()

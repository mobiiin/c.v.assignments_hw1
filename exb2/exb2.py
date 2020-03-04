import cv2 as cv
import numpy as np

cap = cv.VideoCapture('video.mp4')

rndframe = cap.get(cv.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=30)  # Randomly chooses 30 frames

frames = []   # create an empty array
for i in rndframe:
    cap.set(cv.CAP_PROP_POS_FRAMES, i)
    (ret, frame) = cap.read()
    frames.append(frame)  # adds each frame to the end of the frame arrays

# Calculates the middle frame
medianF = np.median(frames, axis=0).astype(dtype=np.uint8)
cv.imshow('frame', medianF)
medianF = cv.cvtColor(medianF, cv.COLOR_BGR2GRAY)

while 1:
    (ret, frame1) = cap.read()
    if ret == 1:
        frame1 = cv.cvtColor(frame1, cv.COLOR_BGR2GRAY)
        backg_sub = cv.absdiff(medianF, frame1)  # subtracts backG from the rest of the frames
        cv.imshow('cars', backg_sub)
        k = cv.waitKey(1) & 0xFF
        if k == ord('e'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()

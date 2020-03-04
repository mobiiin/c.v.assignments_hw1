import cv2 as cv
import numpy as np

img = cv.imread('4.jpg', 1)
imgG = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # converts the image to gray scale

# (_, thresh) = cv.threshold(imgG, 240, 255, cv.THRESH_BINARY)
# (contours, _) = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

# for contour in contours:
#   approx = cv.approxPolyDP(contour, 0.01*cv.arcLength(contour, 1), 1)  # counts the straight lines of each shape
#    cv.drawContours(img, [approx], 0, (0, 0, 0), 2)
#    x = approx.ravel()[0]
#    y = approx.ravel()[1]
#    if len(approx) == 4:
#        (x, y, w, h) = cv.boundingRect(approx)
#        ratio = float(w/h)
#        if ratio >= 1.2 or ratio <= 0.8:
#            cv.circle(img, (int(x+h/2), int(y+w/2)), int((w+h)/2), (0, 0, 255), 2)
#
dimension = img.shape
print(dimension)
temp = imgG[45:80, 320:370]
imgG[45:80, 320:370] = temp  # I cropped a rectangle for template matching
(w, h) = temp.shape[::-1]  # it gives us the height and width of the shape in the reverse order
match = cv.matchTemplate(imgG, temp, cv.TM_CCOEFF_NORMED)  # fetches us the coordinates of possible matches
print(match)
match1 = np.where(match >= 0.7)  # searches inside the match data and brings us the ones greater than specified value
print(match1)

for pt in zip(*match1[::-1]):
    cv.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv.imshow('imgG', img)
cv.waitKey(0)
cv.destroyAllWindows()

import cv2
img1 = cv2.imread('1.jpg', 1)  # 1 is colored and 0 is grayscale
img0 = cv2.imread('1.jpg', 0)
font = cv2.FONT_HERSHEY_SIMPLEX  # choosing a font style here
cv2.putText(img1, '98210727', (10, 100), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
cv2.putText(img0, '98210727', (10, 100), font, 1, (0, 255, 0), 2, cv2.LINE_AA)
cv2.imshow('image1', img1)
cv2.imshow('image0', img0)
k = cv2.waitKey(0) & 0xFF  # waits for our action then saves the key in k
if k == ord('s'):    # if the pressed key is s it executes the following commands
    cv2.imwrite('1_copy.jpg', img1)
    cv2.imwrite('0_copy.jpg', img0)
    cv2.destroyAllWindows()
else:
    cv2.destroyAllWindows()

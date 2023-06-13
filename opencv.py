import cv2

img = cv2.imread('mottonetua-2284.jpg')
# print(img.shape)

img = cv2.resize(img, (1780,1200))
# print(img.shape)
cv2.imshow('Result', img)
cv2.waitKey(0)
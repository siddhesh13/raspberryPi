import cv2
import numpy as np

img = cv2.imread('corner.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = np.float32(gray)

'''
#Shi-Tomasi Corner Detector
corners = cv2.goodFeaturesToTrack(gray, 60, 0.01, 10)
corners = np.int0(corners)

for corner in corners:
    x, y = corner.ravel()
    cv2.circle(img, (x,y), 3, 255, -1)
'''

#harris corner detector
dst = cv2.cornerHarris(gray, 2, 3, 0.07)
dst = cv2.dilate(dst, None)
img[dst>0.01*dst.max()] = [0,255,0]

cv2.imshow('corners', img)
cv2.waitKey()

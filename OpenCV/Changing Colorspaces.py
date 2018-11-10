import cv2
import numpy as np

#flags = [i for i in dir(cv2) if i.startswith('COLOR_')]
#print(flags)

img1 = cv2.imread('cartoon.png')
hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV)
cv2.imshow('hsv', hsv)
print(img1.shape)

lower_yellow = np.array([0,255,255])
upper_yellow = np.array([190,255,255])

mask = cv2.inRange(hsv, lower_yellow,upper_yellow)
cv2.imshow('mask',mask)

res = cv2.bitwise_and(img1, img1, mask=mask)
cv2.imshow('res',res)

cv2.waitKey()

import cv2
import numpy as np

img1 = cv2.imread('3D-Matplotlib.png')
#img2 = cv2.imread('mainsvmimage.png')

img2 = cv2.imread('mainlogo.png')
#add = img1 + img2
#add = cv2.add(img1,img2)
#cv2.imshow('add',add)
#weighted = cv2.addWeighted(img1,0.7,img2,0.5,0)
#cv2.imshow('weighted',weighted)

rows,cols,channels = img2.shape
roi = img1[0:rows, 0:cols]
cv2.imshow('img1',img1)
#cv2.imshow('img2',img2)
#cv2.imshow('roi',roi)

img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
cv2.imshow('img2gray',img2gray)

ret, mask = cv2.threshold(img2gray, 220, 255, cv2.THRESH_BINARY_INV)
cv2.imshow('mask',mask)

mask_inv = cv2.bitwise_not(mask)
cv2.imshow('mask_inv',mask_inv)

img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)
cv2.imshow('img1_bg',img1_bg)

img2_fg = cv2.bitwise_and(img2, img2, mask=mask)
cv2.imshow('img2_fg',img2_fg)

dst = cv2.add(img1_bg, img2_fg)
cv2.imshow('dst',dst)

img1[0:rows, 0:cols] = dst

cv2.imshow('img1',img1)
cv2.waitKey(0)

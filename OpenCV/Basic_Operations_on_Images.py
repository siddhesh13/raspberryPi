import numpy as np
import cv2
from matplotlib import pyplot as plt

#Accessing and Modifying pixel values
img = cv2.imread('watch.jpg')
px = img[100,100]
print(px)
px = img[100,100,0]
print(px)
img[100,100] = (0,20,57)
print(img[100,100])
img.itemset((100,100,2), 0)
print(img.item(100,100,2))

#Accessing Image Properties

print(img.shape)
print(img.size)
print(img.dtype)

#Image ROI

watchface = img[40:120, 100:200]
img[0:80, 0:100] = watchface
'''
cv2.imshow('image', img)
cv2.waitKey()
'''
#Splitting and Merging Image Channels
'''
b, g, r = cv2.split(img)
img = cv2.merge((b,g,r))
b = img[:,:,0]#set all blue pixels to zro
img[:,:,2] = 0
'''
#Making Borders for Images (Padding)

BLUE = [255,0,0]
img = cv2.imread('opencv.jpg')

replicate = cv2.copyMakeBorder(img, 10,10,10,10,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img,10,10,10,10,cv2.BORDER_CONSTANT,value=BLUE)

plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()

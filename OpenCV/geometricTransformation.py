import cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('robot.jpg')
rows,cols,channel = img.shape#
'''
#roateion, transformation
#M = np.float32([[1,0,20], [0,1,20]])

M=cv2.getRotationMatrix2D((cols/2,rows/2),90,1)
dst = cv2.warpAffine(img,M,(cols,rows))
'''
print(img.shape)
#perspective transform

pt1 = np.float32([[20,50],[200,50],[20,175],[200,175]])
pt2 = np.float32([[0,0],[225,0],[0,225],[225,225]])

M = cv2.getPerspectiveTransform(pt1,pt2)
dst = cv2.warpPerspective(img,M,(225,225))

plt.subplot(121),plt.imshow(img),plt.title('Input')
plt.subplot(122),plt.imshow(dst),plt.title('Output')
plt.show()
#cv2.imshow('img',dst)

cv2.waitKey()



# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
from matplotlib import pyplot as plt
 
# initialize the camera and grab a reference to the raw camera capture
camera = PiCamera()
rawCapture = PiRGBArray(camera)
 
# allow the camera to warmup
time.sleep(3)
 
# grab an image from the camera
camera.capture(rawCapture, format="bgr")
image = rawCapture.array 
img = cv2.imread('watch.jpg',cv2.IMREAD_GRAYSCALE)
# display the image on screen and wait for a keypress
#cv2.imshow("Image", img)
#cv2.waitKey(0)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([15,100],[80,100],'c',linewidth=5)
plt.show()

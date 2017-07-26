# Image enhancement using thresholding

import cv2
import numpy as np

testImg = cv2.imread('bookpage.jpg')


#Thresholding normally
retval, threshold = cv2.threshold(testImg, 12, 255,cv2.THRESH_BINARY)

#Converting to Grayscale
grayImg = cv2.cvtColor(testImg,cv2.COLOR_BGR2GRAY)

#Using a Gaussian Adaptive Threshold
gthreshold = cv2.adaptiveThreshold(grayImg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)


cv2.imshow('Original',testImg)
cv2.imshow('Threshold',threshold)
cv2.imshow('Gaussian Threshold',gthreshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

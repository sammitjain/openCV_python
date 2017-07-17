# OpenCV for Python #4
# Threshold logo and add to image. (Maintain transparency of background

import numpy as np
import cv2

#Loading the two images
backg = cv2.imread('messi.jpg',cv2.IMREAD_COLOR)
logo = cv2.imread('matlablogo.jpg',cv2.IMREAD_COLOR)

#Resizing the logo
logo = cv2.resize(logo,None,fx=0.3,fy=0.3)

#Setting the size for ROI
rows,cols,channels = logo.shape
roi = backg[0:rows,0:cols]

#Now creating a mask of the Logo
grayLogo = cv2.cvtColor(logo,cv2.COLOR_BGR2GRAY)

#Adding the threshold
ret, mask = cv2.threshold(grayLogo,220,255, cv2.THRESH_BINARY_INV)

#Inverting the mask
mask_inv = cv2.bitwise_not(mask)

#Resetting the unnecessary background of logo to background image
backg_logo = cv2.bitwise_and(roi,roi,mask = mask_inv)

#Choosing relevant portion of the logo image
logo_rel = cv2.bitwise_and(logo,logo,mask = mask)

trans_roi = cv2.add(backg_logo,logo_rel)

backg[0:rows, 0:cols] = trans_roi

cv2.imshow('Original Image',backg)
cv2.imshow('Logo',logo)
cv2.imshow('grayLogo',grayLogo)
cv2.imshow('mask',mask)
cv2.imshow('mask_inv',mask_inv)
cv2.imshow('backg_logo',backg_logo)
cv2.imshow('FINAL',backg)
cv2.waitKey(0)
cv2.destroyAllWindows()


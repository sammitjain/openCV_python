# Color-based segmentation in Python using OpenCV
# Morphological Transformations

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    _, frame = cap.read()

    # Converting to HSV space for more accurate results
    hsvImg = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    #Initializing range
    lower_v = np.array([140,150,50])
    upper_v = np.array([180,200,150])

    #Initializing Mask
    mask = cv2.inRange(hsvImg,lower_v,upper_v)

    #Final result
    finalImg = cv2.bitwise_and(frame,frame,mask=mask)

    #Setting up the kernel for transformation
    kernel = np.ones((5,5),np.uint8)

    #Erosion and Dilation
    erosion = cv2.erode(mask, kernel, iterations=1)
    dilation = cv2.dilate(mask,kernel, iterations=2)

    opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    #Applying dilated mask to original
    #dilImg = cv2.bitwise_and(frame,frame,mask=dilation)
    #Can also use tophat and blackhat
    
    cv2.imshow('frame',frame)
    cv2.imshow('Result', finalImg)
    cv2.imshow('erosion',erosion)
    cv2.imshow('dilation',dilation)
    cv2.imshow('opening',opening)
    cv2.imshow('closing',closing)
    #cv2.imshow('dilImg',dilImg)
    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

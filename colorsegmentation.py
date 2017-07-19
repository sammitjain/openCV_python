# Color-based segmentation in Python using OpenCV

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

    #Initializing filter
    kernel = np.ones((15,15),np.float32)/255

    #Smooth the image
    smoothImg = cv2.filter2D(finalImg,-1,kernel)

    #Adding Gaussian Blur to image
    blurImg = cv2.GaussianBlur(finalImg, (15,15),0)

    #Adding Median Blur
    medblurImg = cv2.medianBlur(finalImg,15)

    #Adding Bilateral Blur
    bilblurImg = cv2.bilateralFilter(finalImg,15,75,75)

    
##    cv2.imshow('frame',frame)
##    cv2.imshow('mask',mask)
##    cv2.imshow('Median',medblurImg)
##    cv2.imshow('Bilateral',bilblurImg)
##    cv2.imshow('Result', finalImg)
##    cv2.imshow('Smoothed',smoothImg)
##    cv2.imshow('Blurred',blurImg)
##    
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
cap.release()

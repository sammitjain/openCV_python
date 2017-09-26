#Program:       To match templates to original image
#Programmer:    Sammit Jain | 2014B4A30909G
#Project:       Templat matching / Correlation / Cross Normalization
#Supervisor:    Prof. Neena Goveas, Dept. of Computer Science, BITS Pilani

import cv2
import numpy as np
from matplotlib import pyplot as plt

testImg = cv2.imread('famous_people.jpg')
testSample = cv2.imread('gandhi_big.jpg')
#testSample = cv2.imread('gandhi_big.jpg')
#Doesn't work with the a scaled image, need to try something different for that. 
#cv2.imshow('Original',testImg)
#cv2.imshow('Gandhi',testSample)

testImg2 = testImg.copy()

#Setting the height and width of the template to be found in the main image
h,w = testSample.shape[0:2]

#Creating a list of methods that can be used for template matching

methods = ['cv2.TM_CCOEFF','cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR', 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:
    testImg = testImg2.copy()
    method = eval(meth)

    #Applying the template matching algorithm

    resImg = cv2.matchTemplate(testImg, testSample, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resImg)

    #For specifically some methods, SQDIFF and SQDIFF_NORMED, take minimum
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(testImg,top_left,bottom_right,255,2)

    plt.subplot(121),plt.imshow(resImg, cmap = 'gray')
    plt.title('Matching Result'),plt.xticks([]),plt.yticks([])
    plt.subplot(122),plt.imshow(testImg, cmap = 'gray')
    plt.title('Detected Area'),plt.xticks([]),plt.yticks([])    
    plt.suptitle(meth)

    plt.show()


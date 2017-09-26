#Program:       Script to make multiple resized copies at 5% downsize and then match templates
#Programmer:    Sammit Jain | 2014B4A30909G
#Project:       As part of the scale invariant template matching
#Supervisor:    Prof. Neena Goveas, Dept. of Computer Science, BITS Pilani

import cv2
import numpy as np
from matplotlib import pyplot as plt

testImg = cv2.imread('gandhi_big.jpg')

for i in range(10):
    tempImg = cv2.resize(testImg,None,fx=(100-i*10)/100,fy=(100-i*10)/100)
    file_name = 'resized'+str(i)+'.jpg'
    cv2.imwrite(file_name,tempImg)


for i in range(10):
    fname = 'resized'+str(i)+'.jpg'
    testImg = cv2.imread('famous_people.jpg')
    testSample = cv2.imread(fname)
    #testSample = cv2.imread('gandhi_big.jpg')
    #Doesn't work with the a scaled image, need to try something different for that. 
    #cv2.imshow('Original',testImg)
    #cv2.imshow('Gandhi',testSample)


    #Setting the height and width of the template to be found in the main image
    h,w = testSample.shape[0:2]

    #Applying the template matching algorithm

    resImg = cv2.matchTemplate(testImg, testSample, eval('cv2.TM_CCOEFF_NORMED'))
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(resImg)

    #For specifically some methods, SQDIFF and SQDIFF_NORMED, take minimum

    top_left = max_loc
    bottom_right = (top_left[0] + w, top_left[1] + h)

    cv2.rectangle(testImg,top_left,bottom_right,255,2)

    plt.subplot(121),plt.imshow(resImg, cmap = 'gray')
    plt.title('Matching Result'),plt.xticks([]),plt.yticks([])
    plt.subplot(122),plt.imshow(testImg, cmap = 'gray')
    plt.title('Detected Area'),plt.xticks([]),plt.yticks([])    
    plt.suptitle('Result')

    plt.show()

#Program:       Skew Invariant Template matching (Using SURF/SIFT feature matching)
#Programmer:    Sammit Jain | 2014B4A30909G
#Project:       Scale, Rotation and Skew invariant template matching
#Supervisor:    Prof. Neena Goveas, Dept. of Computer Science, BITS Pilani

import cv2
import numpy as np
from matplotlib import pyplot as plt

tempImg = cv2.imread('bitsgoanew1.jpg',0); #Template Image
mainImg = cv2.imread('bitsgoanew1_skewed.jpg',0) #Main Image

#Starting the SIFT detector

orb = cv2.ORB_create()

#finding the keypoints and descriptors with SIFT

#Slightly different from initializing keypoints and descriptors in C++
#Python used slightly different openCV definitions

kp1 = orb.detect(tempImg, None)
kp1, des1 = orb.compute(tempImg, kp1)

kp2 = orb.detect(mainImg, None)
kp2, des2 = orb.compute(mainImg, kp2)

#Creating a BFMatcher Object
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

matches = bf.match(des1,des2)

matches = sorted(matches, key = lambda x:x.distance)

resImg = cv2.drawMatches(tempImg,kp1,mainImg,kp2,matches[:20], tempImg, flags=2)

plt.imshow(resImg)

plt.show()

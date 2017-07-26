# Make a 6 cell display by stitching windows in Numpy
# Programmer:   Sammit Jain | 2014B4A3909G

import numpy as np
import cv2

testImg = cv2.imread('laligalogo.jpg')

stitched1 = np.hstack((testImg,testImg,testImg))
stitched2 = np.hstack((testImg,testImg,testImg))

stitched = np.vstack((stitched1,stitched2))

cv2.imshow('Results',stitched)

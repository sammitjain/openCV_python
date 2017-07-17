# Basic program with OpenCV in Python
# Loading and writing images + scaling

import cv2
import numpy as np
import matplotlib.pyplot as plt


testImg = cv2.imread('testImg.jpg', cv2.IMREAD_GRAYSCALE)
testImg = cv2.resize(testImg,None,fx=0.3,fy=0.3) #it's imresize in MATLAB. NOTE.

#Showing with cv2
cv2.imshow('Original Image',testImg)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('grayImg.jpg',testImg)

#Showing the image with matplotlib

##plt.imshow(testImg, cmap='gray', interpolation='bicubic')
##plt.plot([50,100],[80,100],'c',linewidth=5)
##plt.show()


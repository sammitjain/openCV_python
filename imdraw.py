# OpenCV for Python #3
# Drawing objects on image

import numpy as np
import cv2

testImg = cv2.imread('testImg.jpg',cv2.IMREAD_COLOR)

testImg = cv2.resize(testImg,None,fx=0.3,fy=0.3)

#This one's to draw a line
cv2.line(testImg,(0,0), (550,250), (255,255,255), 5)
cv2.rectangle(testImg,(15,25), (600,250), (0,255,0), 5)
cv2.circle(testImg, (300,100),55, (0,0,255),2)

#Negative lineWidth fills the object

pts = np.array([[10,5],[20,30],[600,100],[50,10]], np.int32)
cv2.polylines(testImg, [pts], True, (0,255,255),1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(testImg,'Lorem Ipsum', (580,280), font, 0.5, (255,255,255),1,cv2.LINE_AA)
cv2.imshow('Original Image',testImg)

cv2.waitKey(0)
cv2.destroyAllWindows()


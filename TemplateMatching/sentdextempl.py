#Program:       Match templates and mark corrected templates
#Programmer:    Sammit Jain | 2014B4A30909G
#Supervisor:    Prof. Neena Goveas

import cv2
import numpy as np

mainImg = cv2.imread('sentdexmain.jpg')
mainImgGray = cv2.cvtColor(mainImg, cv2.COLOR_BGR2GRAY)

tempImg = cv2.imread('sentdextemplate.jpg',0)

w, h = tempImg.shape[::-1]

resImg = cv2.matchTemplate(mainImgGray, tempImg, cv2.TM_CCOEFF_NORMED)
threshold = 0.9

loc = np.where(resImg >= threshold)

for pt in zip(*loc[::-1]):
    cv2.rectangle(mainImg, pt, (pt[0]+w, pt[1]+h), (0,255,255), 2)


cv2.imshow('DETECTED',mainImg)

    


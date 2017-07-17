# Basic program 2 with OpenCV in Python
# Working with Video (Reading from webcam, editing, writing)

import cv2
import numpy as np

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('test_gray.avi',fourcc,20.0,(640,480))
# out = cv2.VideoWriter('test_gray.avi',-1,20.0,(640,480))
# use the above to choose compression codec
while (True):
    ret, frame = cap.read()
    grayFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    out.write(frame)

    cv2.imshow('Video frame',frame)
    cv2.imshow('Gray',grayFrame)

    if cv2.waitKey(1) & 0xFF ==ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()


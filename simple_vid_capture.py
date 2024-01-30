import cv2 
import numpy
vid = cv2.VideoCapture(2)
while(1):
    ret,frame = vid.read()
    cv2.line(frame,(0,400),(800,400),(0,0,0),3)
    cv2.imshow('original', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
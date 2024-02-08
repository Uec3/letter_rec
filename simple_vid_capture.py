import cv2 
import numpy
vid = cv2.VideoCapture(2)

def nothing(x):
    pass

cv2.namedWindow('binarized')

cv2.createTrackbar('Rmin','binarized',0,255,nothing)
cv2.createTrackbar('Gmin','binarized',0,255,nothing)
cv2.createTrackbar('Bmin','binarized',0,255,nothing)
cv2.createTrackbar('Rmax','binarized',255,255,nothing)
cv2.createTrackbar('Gmax','binarized',255,255,nothing)
cv2.createTrackbar('Bmax','binarized',255,255,nothing)

while(1):
    ret,frame = vid.read()    
    # hsv = cv2.cvtColor(frame,cv2.COLOR_RGB2HSV)
    rmin = cv2.getTrackbarPos('Rmin','binarized')
    gmin = cv2.getTrackbarPos('Gmin','binarized')
    bmin = cv2.getTrackbarPos('Bmin','binarized')
    rmax = cv2.getTrackbarPos('Rmax','binarized')
    gmax = cv2.getTrackbarPos('Gmax','binarized')
    bmax = cv2.getTrackbarPos('Bmax','binarized')
    
    mn = (rmin,gmin,bmin)
    mx = (rmax,gmax,bmax)
    # ret,bin = cv2.threshold(frame,rmin,rmax,cv2.THRESH_BINARY)
    bin = cv2.inRange(frame,mn,mx)
    # cv2.line(frame,(0,400),(800,400),(0,0,0),3)
    cv2.imshow('original', frame)
    cv2.imshow('binarized',bin)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
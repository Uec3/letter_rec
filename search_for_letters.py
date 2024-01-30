import cv2 
import numpy
vid = cv2.VideoCapture(2)
while(1):
    ret,frame = vid.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    canny = cv2.Canny(gray,245,250)
    contur,hierarchy = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    contur_poly = [None]*len(contur)
    i_max = 0
    max_area = 0
    for i,c in enumerate(contur):
        contur_poly[i] = cv2.approxPolyDP(c,20,True)
        if(max_area < cv2.contourArea(contur_poly[i])):
            max_area = cv2.contourArea(contur_poly[i])
            i_max = i
    x,y,h,w= cv2.boundingRect(contur_poly[i_max])
    cv2.rectangle(frame,(x,y),(x + h,y + w),(255,0,0),3)
    err_table = numpy.array(int)
    f = open('tst.txt')
    for i in contur:
        for line in f:
            x_f,y_f = line.split()
            x_f = (float(x_f)) * (h) + x
            y_f = (float(y_f)) * (w) + y
            cv2.circle(frame,(int(x_f), int(y_f)),5,(255,0,0),3)
                        
    cv2.imshow('canny', canny)
    cv2.imshow('original', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
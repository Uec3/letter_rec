import cv2 
import numpy
vid = cv2.VideoCapture(3)
DEBUG = 1
def distance(x,y,x0,y0,x1,y1):
    return (abs((y1 - y0) * x - (x1 - x0) * y + x1 * y0 - y1 * x0) / numpy.square( (y1 - y0) ** 2 + (x1 - x0) ** 2))

def nothing(x):
    pass

while(1):
    ret,frame = vid.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    canny = cv2.Canny(gray,250,255)
    contur,hierarchy = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_NONE)
    contur_poly = [None]*len(contur)
    i_max = 0
    max_area = 0
    max_contour = 0
    counter = 0
    for i,c in enumerate(contur):
        contur_poly[i] = cv2.approxPolyDP(c,5,True)
        if(max_area < cv2.contourArea(contur_poly[i])):
            max_area = cv2.contourArea(contur_poly[i])
            i_max = i
            max_contour = contur_poly[i]
    x,y,h,w= cv2.boundingRect(max_contour)
    if(DEBUG):
        cv2.drawContours(frame,contur_poly,-1,(0,0,0),5)
        cv2.rectangle(frame,(x,y),(x + h,y + w),(255,0,0),3)
    err = 0
    f = open('tst.txt')
    for line in f:
        x_f,y_f = line.split()
        x_f = (float(x_f)) * (h) + x
        y_f = (float(y_f)) * (w) + y
        if(DEBUG):
            cv2.circle(frame,(int(x_f), int(y_f)),5,(255,0,0),3)
        min_e = 1000 
        counter += 1
        for c, i in enumerate(contur_poly[i_max]):
            if(DEBUG):
                cv2.circle(frame,(i[0][0],i[0][1]), 3,(0,255,0),2)
                # print(contur_poly[i_max][c + 1],i)
            if(c < len(contur_poly[i_max]) - 1):
                if(distance(int(x_f), int(y_f), i[0][0],i[0][1],contur_poly[i_max][c + 1][0][0],contur_poly[i_max][c + 1][0][1]) < min_e):
                    min_e = distance(int(x_f), int(y_f), i[0][0],i[0][1],contur_poly[i_max][c + 1][0][0],contur_poly[i_max][c + 1][0][1])
                cv2.line(frame,(i[0][0],i[0][1]),(contur_poly[i_max][c + 1][0][0],contur_poly[i_max][c + 1][0][1]),(255,0,0),2)
            else:
                if(distance(int(x_f), int(y_f), i[0][0],i[0][1],contur_poly[i_max][0][0][0],contur_poly[i_max][0][0][1]) < min_e):
                    min_e = distance(int(x_f), int(y_f), i[0][0],i[0][1],contur_poly[i_max][0][0][0],contur_poly[i_max][0][0][1])
                cv2.line(frame,(i[0][0],i[0][1]),(contur_poly[i_max][0][0][0],contur_poly[i_max][0][0][1]),(255,0,0),2)    
            # if(distance(i[0][0], i[0][1], int(x_f), int(y_f)) < min_e):
            #     min_e = distance(i[0][0], i[0][1], int(x_f), int(y_f))
        # print(min_e)
        err += min_e
    err /= counter
    err *= 1000000
    print (err)
    # if(err < 10 ):
    #     print("Letter Rec")
    # else:
    #     print(err)
    cv2.imshow('canny', canny)
    cv2.imshow('original', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
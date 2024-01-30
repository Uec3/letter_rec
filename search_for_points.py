import cv2 
import numpy

vid = cv2.VideoCapture(2)


while(1):
    ret,frame = vid.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_RGB2GRAY)
    canny = cv2.Canny(gray,250,255)
    contur,hierarchy = cv2.findContours(canny,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
    contur_poly = [None]*len(contur)
    i_max = 0
    max_area = 0
    for i,c in enumerate(contur):
        contur_poly[i] = cv2.approxPolyDP(c,5,True)
        if(max_area < cv2.contourArea(contur_poly[i])):
            max_area = cv2.contourArea(contur_poly[i])
            i_max = i
    try:
        # cv2.drawContours(frame,contur_poly,-1,(255,0,0),5)
        rl_countur = numpy.ndarray(shape=(2,len(contur_poly[i_max])), dtype= float, )
        x,y,h,w= cv2.boundingRect(contur_poly[i_max])
        # print(len(contur_poly[i_max]))
        # cv2.drawContours(frame, contur_poly,-1,(0,0,255),2)
        if( x != 0 and y != 0):
            # cv2.line(frame,(x-5,y),(x+5,y),(255,0,0),3)
            # cv2.line(frame,(x,y-5),(x,y+5),(255,0,0),3)
            # cv2.drawContours(frame,contur_poly,-1,(0,0,255),3)
            cv2.rectangle(frame,(x,y),(x+h,y+w),(255,0,0),3)
            d = input()
            # print(len(contur_poly[i_max]))
            # print(len(rl_countur[0]), len(rl_countur[1]))
            for i in range(len(rl_countur[0])):
                rl_countur[0][i] = (contur_poly[i_max][i][0][0] - x) / (h)
                rl_countur[1][i] = (contur_poly[i_max][i][0][1] - y) / (w)
                x_point = rl_countur[0][i] * (h) + x 
                y_point = rl_countur[1][i] * (w) + y 
                cv2.circle(frame,(int(rl_countur[0][i] * (h) + x), int(rl_countur[1][i] * (w) + y)),3,(255,255,0),3)
            if d == 'w':
                f = open('tst.txt','w')
                for i in range(len(contur_poly[i_max])):
                    x_point = rl_countur[0][i]
                    y_point = rl_countur[1][i]
                    # if( f.readable()):
                    # print(f.readable())
                    f.write(str(x_point) + '\t' + str(y_point) + '\n')
                f.close()
    except IndexError:
        pass
    cv2.imshow('canny', canny)
    cv2.imshow('original', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()

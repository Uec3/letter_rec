import cv2 
import numpy
alb = {}
f = open('dict.txt')
arr = []
for line in f:
    #ord(d) > 96 and ord(d) < 123
    if(len(str(line)) < 3):
        letter = str(line)[0]
        # print(letter)
        alb[letter] = arr
        arr.clear()
    else:
        x_f,y_f = line.split()
        x_f = float(x_f)
        y_f = float(y_f)
        arr.append((x_f,y_f))     
    # print(len(line))
print(alb)
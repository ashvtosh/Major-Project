import sys
import cv2
import time
import numpy as np 
import math
import string
import os
import random  
import operator
import tensorflow as tf 
from tensorflow import keras






'''
from keras.models import model_from_json
with open("coloredvgg16.json","r")as file:
    coloredvgg16_json=file.read()

loaded_model=model_from_json(coloredvgg16_json)

loaded_model.load_weights("coloredvgg16.h5")

print("Loaded model from disk")

'''


if not os.path.exists("data1"):
    os.makedirs("data1")
if not os.path.exists("data1/train1"):
    os.makedirs("data1/train1")
    
if not os.path.exists("data1/test1"):
    os.makedirs("data1/test1")
for i in string.ascii_uppercase:
    if not os.path.exists("data1/train1/" +i):
        os.makedirs("data1/train1/" +i)
    if not os.path.exists("data1/test1/" + i):
        os.makedirs("data1/test1/"+i)    



cam = cv2.VideoCapture(0)




while(cam.isOpened()):
    
    ret, frame = cam.read()
    frame=cv2.flip(frame,1)
    if cv2.waitKey(1)&0xFF == ord('-'):
        break
    x1 = int(0.5*frame.shape[1])
    y1 = 10
    x2 = frame.shape[1]-10
    y2 = int(0.5*frame.shape[1])
    cv2.rectangle(frame, (x1-1, y1-1), (x2+1, y2+1), (255,0,0) ,1)
    roi = frame[y1:y2, x1:x2]
    cv2.imshow("Frame", frame)
    minvalue=20
    roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
    _, roi = cv2.threshold(roi, 120, 255, cv2.THRESH_BINARY)
    cv2.imshow("sign detection", roi)
    mode='train1'
    directory='data1/'+mode+'/'
    count={
        'a':len(os.listdir(directory+"/A")),
        'b':len(os.listdir(directory+"/B")),
        'c':len(os.listdir(directory+"/C")),
        'd':len(os.listdir(directory+"/D")),
        'e':len(os.listdir(directory+"/E")),
        'f':len(os.listdir(directory+"/F")),
        'g':len(os.listdir(directory+"/G")),
        'h':len(os.listdir(directory+"/H")),
        'i':len(os.listdir(directory+"/I")),
        'j':len(os.listdir(directory+"/J")),
        'k':len(os.listdir(directory+"/K")),
        'l':len(os.listdir(directory+"/L")),
        'm':len(os.listdir(directory+"/M")),
        'n':len(os.listdir(directory+"/N")),
        'o':len(os.listdir(directory+"/O")),
        'p':len(os.listdir(directory+"/P")),
        'q':len(os.listdir(directory+"/Q")),
        'r':len(os.listdir(directory+"/R")),
        's':len(os.listdir(directory+"/S")),
        't':len(os.listdir(directory+"/T")),
        'u':len(os.listdir(directory+"/U")),
        'v':len(os.listdir(directory+"/V")),
        'w':len(os.listdir(directory+"/W")),
        'x':len(os.listdir(directory+"/X")),
        'y':len(os.listdir(directory+"/Y")),
        'z':len(os.listdir(directory+"/Z")),
        
    }
    interrupt=cv2.waitKey(10)
    if interrupt & 0xFF==27:
        break
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory+'A/'+str(count['a'])+'.jpg', roi)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory+'B/'+str(count['b'])+'.jpg', roi)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'C/'+str(count['c'])+'.jpg', roi)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(directory+'D/'+str(count['d'])+'.jpg', roi)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(directory+'E/'+str(count['e'])+'.jpg', roi)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(directory+'F/'+str(count['f'])+'.jpg', roi)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(directory+'G/'+str(count['g'])+'.jpg', roi)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(directory+'H/'+str(count['h'])+'.jpg', roi)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(directory+'I/'+str(count['i'])+'.jpg', roi)
    if interrupt & 0xFF == ord('j'):
        cv2.imwrite(directory+'J/'+str(count['j'])+'.jpg', roi)
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite(directory+'K/'+str(count['k'])+'.jpg', roi)
    if interrupt & 0xFF == ord('l'):
        cv2.imwrite(directory+'L/'+str(count['l'])+'.jpg', roi)
    if interrupt & 0xFF == ord('m'):
        cv2.imwrite(directory+'M/'+str(count['m'])+'.jpg', roi)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(directory+'N/'+str(count['n'])+'.jpg', roi)
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(directory+'O/'+str(count['o'])+'.jpg', roi)
    if interrupt & 0xFF == ord('p'):
        cv2.imwrite(directory+'P/'+str(count['p'])+'.jpg', roi)
    if interrupt & 0xFF == ord('q'):
        cv2.imwrite(directory+'Q/'+str(count['q'])+'.jpg', roi)
    if interrupt & 0xFF == ord('r'):
        cv2.imwrite(directory+'R/'+str(count['r'])+'.jpg', roi)
    if interrupt & 0xFF == ord('s'):
        cv2.imwrite(directory+'S/'+str(count['s'])+'.jpg', roi)
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(directory+'T/'+str(count['t'])+'.jpg', roi)
    if interrupt & 0xFF == ord('u'):
        cv2.imwrite(directory+'U/'+str(count['u'])+'.jpg', roi)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(directory+'V/'+str(count['v'])+'.jpg', roi)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(directory+'W/'+str(count['w'])+'.jpg', roi)
    if interrupt & 0xFF == ord('x'):
        cv2.imwrite(directory+'X/'+str(count['x'])+'.jpg', roi)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(directory+'Y/'+str(count['y'])+'.jpg', roi)
    if interrupt & 0xFF == ord('z'):
        cv2.imwrite(directory+'Z/'+str(count['z'])+'.jpg', roi)
    mode='test1'
    directory='data1/'+mode+'/'
    count={
        'A':len(os.listdir(directory+"/A")),
        'B':len(os.listdir(directory+"/B")),
        'C':len(os.listdir(directory+"/C")),
        'D':len(os.listdir(directory+"/D")),
        'E':len(os.listdir(directory+"/E")),
        'F':len(os.listdir(directory+"/F")),
        'G':len(os.listdir(directory+"/G")),
        'H':len(os.listdir(directory+"/H")),
        'I':len(os.listdir(directory+"/I")),
        'J':len(os.listdir(directory+"/J")),
        'K':len(os.listdir(directory+"/K")),
        'L':len(os.listdir(directory+"/L")),
        'M':len(os.listdir(directory+"/M")),
        'N':len(os.listdir(directory+"/N")),
        'O':len(os.listdir(directory+"/O")),
        'P':len(os.listdir(directory+"/P")),
        'Q':len(os.listdir(directory+"/Q")),
        'R':len(os.listdir(directory+"/R")),
        'S':len(os.listdir(directory+"/S")),
        'T':len(os.listdir(directory+"/T")),
        'U':len(os.listdir(directory+"/U")),
        'V':len(os.listdir(directory+"/V")),
        'W':len(os.listdir(directory+"/W")),
        'X':len(os.listdir(directory+"/X")),
        'Y':len(os.listdir(directory+"/Y")),
        'Z':len(os.listdir(directory+"/Z")),
        
    }

    interrupt=cv2.waitKey(10)
    if interrupt & 0xFF==27:
        break
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory+'A/'+str(count['A'])+'.jpg', roi)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory+'B/'+str(count['B'])+'.jpg', roi)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'C/'+str(count['C'])+'.jpg', roi)
    if interrupt & 0xFF == ord('d'):
        cv2.imwrite(directory+'D/'+str(count['D'])+'.jpg', roi)
    if interrupt & 0xFF == ord('e'):
        cv2.imwrite(directory+'E/'+str(count['E'])+'.jpg', roi)
    if interrupt & 0xFF == ord('f'):
        cv2.imwrite(directory+'F/'+str(count['F'])+'.jpg', roi)
    if interrupt & 0xFF == ord('g'):
        cv2.imwrite(directory+'G/'+str(count['G'])+'.jpg', roi)
    if interrupt & 0xFF == ord('h'):
        cv2.imwrite(directory+'H/'+str(count['H'])+'.jpg', roi)
    if interrupt & 0xFF == ord('i'):
        cv2.imwrite(directory+'I/'+str(count['I'])+'.jpg', roi)
    if interrupt & 0xFF == ord('j'):
        cv2.imwrite(directory+'J/'+str(count['J'])+'.jpg', roi)
    if interrupt & 0xFF == ord('k'):
        cv2.imwrite(directory+'K/'+str(count['K'])+'.jpg', roi)
    if interrupt & 0xFF == ord('l'):
        cv2.imwrite(directory+'L/'+str(count['L'])+'.jpg', roi)
    if interrupt & 0xFF == ord('m'):
        cv2.imwrite(directory+'M/'+str(count['M'])+'.jpg', roi)
    if interrupt & 0xFF == ord('n'):
        cv2.imwrite(directory+'N/'+str(count['N'])+'.jpg', roi)
    if interrupt & 0xFF == ord('o'):
        cv2.imwrite(directory+'O/'+str(count['O'])+'.jpg', roi)
    if interrupt & 0xFF == ord('p'):
        cv2.imwrite(directory+'P/'+str(count['P'])+'.jpg', roi)
    if interrupt & 0xFF == ord('q'):
        cv2.imwrite(directory+'Q/'+str(count['Q'])+'.jpg', roi)
    if interrupt & 0xFF == ord('r'):
        cv2.imwrite(directory+'R/'+str(count['R'])+'.jpg', roi)
    if interrupt & 0xFF == ord('s'):
        cv2.imwrite(directory+'S/'+str(count['S'])+'.jpg', roi)
    if interrupt & 0xFF == ord('t'):
        cv2.imwrite(directory+'T/'+str(count['T'])+'.jpg', roi)
    if interrupt & 0xFF == ord('u'):
        cv2.imwrite(directory+'U/'+str(count['U'])+'.jpg', roi)
    if interrupt & 0xFF == ord('v'):
        cv2.imwrite(directory+'V/'+str(count['V'])+'.jpg', roi)
    if interrupt & 0xFF == ord('w'):
        cv2.imwrite(directory+'W/'+str(count['W'])+'.jpg', roi)
    if interrupt & 0xFF == ord('x'):
        cv2.imwrite(directory+'X/'+str(count['X'])+'.jpg', roi)
    if interrupt & 0xFF == ord('y'):
        cv2.imwrite(directory+'Y/'+str(count['Y'])+'.jpg', roi)
    if interrupt & 0xFF == ord('z'):
        cv2.imwrite(directory+'Z/'+str(count['Z'])+'.jpg', roi)
cam.release()
cv2.destroyAllWindows()

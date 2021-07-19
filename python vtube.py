# This is a project I whipped up since I was bored. 
# It is by no means a replacement for professional vtubing software as it takes up too much of the cpu and affects the performance.
# However, this is still a viable option for those with higher end computers
# The process of making this and setting up OBS for this in in my youtube.
# youtube link: [insert link]

import sys
import cv2
import numpy as np

cap = cv2.VideoCapture(0)
body = cv2.imread('avatar body.png') # 300x480
eye_open = cv2.imread('avatar eye (o o).png') # 125x60
wink_L = cv2.imread('avatar eye (> o).png')
wink_R = cv2.imread('avatar eye (o <).png')
eye_close = cv2.imread('avatar eye (- -).png')
fx=0
fy=0
fw=0
fh=0

wid = cap.get(3)
hei = cap.get(4)

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eyes = []
while True:
    ret, frame = cap.read()
    back = np.zeros((int(hei),int(wid),3), np.uint8)
    back[:,0:int(cap.get(3))] = (255,0,0) #set background as blue (B,G,R)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    for num, (x,y,w,h) in enumerate(faces):
        if num == 0:
            fx=x
            fy=y
            fw=w
            fh=h
            eyes = eye_cascade.detectMultiScale(gray, 1.2, 5)
    if fx<150: fx = 150
    if fy<240: fy = 240
    fx = fx
    back[int(hei/2)-240:int(hei/2)+240, fx-150:fx+150] = body
    eye_type = eye_open
    if len(eyes) == 0:
        eye_type = eye_close
    elif len(eyes) == 1:
        for (tx,ty,tw,th) in eyes:
            if tx-tw < fx:
                eye_type = wink_R
            else:
                eye_type = wink_L
    back[int(hei/2)-130:int(hei/2)-70, fx-64:fx+61] = eye_type
    cv2.imshow('avatar',back)
    if cv2.waitKey(24) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
sys.exit()

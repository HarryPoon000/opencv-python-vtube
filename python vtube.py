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

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')
eyes = []
while True:
    ret, frame = cap.read()
    back = np.zeros((int(cap.get(4)),int(cap.get(3)),3), np.uint8)
    back[:,0:int(cap.get(3))] = (255,0,0) #set background as blue

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    for (x,y,w,h) in faces:
        fx=x
        fy=y
        fw=w
        fh=h
        eyes = eye_cascade.detectMultiScale(gray, 1.2, 5)
    if fx<150: fx = 150
    if fy<240: fy = 240
    fx = fx
    back[int(cap.get(4)/2)-240:int(cap.get(4)/2)+240, fx-150:fx+150] = body
    if len(eyes) == 2:
        eye_type = eye_open
    elif len(eyes) == 0:
        eye_type = eye_close
    elif len(eyes) == 1:
        for (tx,ty,tw,th) in eyes:
            if tx-tw < fx:
                eye_type = wink_R
            else:
                eye_type = wink_L
    back[int(cap.get(4)/2)-130:int(cap.get(4)/2)-70, fx-64:fx+61] = eye_type
    cv2.imshow('avatar',back)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
sys.exit()

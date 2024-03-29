import cv2
import numpy as np

detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap=cv2.VideoCapture(0)
while(1):
    ret,frame=cap.read()
    if ret:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces=detector.detectMultiScale(gray,1.3,5)
        for(x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()
            

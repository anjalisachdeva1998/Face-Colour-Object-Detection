import cv2
import numpy as np

def nothing(x):
    pass

cap=cv2.VideoCapture(0)
cv2.namedWindow("TrackColours")

cv2.createTrackbar('l-h','TrackColours',0,179,nothing)
cv2.createTrackbar('l-s','TrackColours',0,255,nothing)
cv2.createTrackbar('l-v','TrackColours',0,255,nothing)
cv2.createTrackbar('u-h','TrackColours',179,179,nothing)
cv2.createTrackbar('u-s','TrackColours',255,255,nothing)
cv2.createTrackbar('u-v','TrackColours',255,255,nothing)

while(1):
    ret,frame=cap.read()
    if ret:
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

        l_h=cv2.getTrackbarPos('l-h','TrackColours')
        l_s=cv2.getTrackbarPos('l-s','TrackColours')
        l_v=cv2.getTrackbarPos('l-v','TrackColours')
        u_h=cv2.getTrackbarPos('u-h','TrackColours')
        u_s=cv2.getTrackbarPos('u-s','TrackColours')
        u_v=cv2.getTrackbarPos('u-v','TrackColours')

        lower_range=np.array([l_h,l_s,l_v])
        upper_range=np.array([u_h,u_s,u_v])

        mask=cv2.inRange(hsv,lower_range,upper_range)


        result = cv2.bitwise_and(frame, frame, mask=mask)
        cv2.imshow("frame", frame)
        cv2.imshow("mask", mask)
        cv2.imshow("result", result)
        #key = cv2.waitKey(1)
        #if key == 27:
           # break
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
    

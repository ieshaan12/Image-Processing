import numpy
import cv2
import time
#For detecting camera
video=cv2.VideoCapture(0)
camera=cv2.VideoCapture(0)
#Create frame object
while True:
    check, frame=video.read();
    #print(frame,check)
    #Show frame
    cv2.imshow("Capturing",frame);
    #Waiting
    rt,cam=camera.read()
    key=cv2.waitKey(1)
    if (key==ord('q')):
        break
    elif(key==ord('c')):
        cv2.imwrite('clicked.jpg',cam)
    elif(key==ord('s')):
        cv2.imshow('clicked.jpg',cam)
        time.sleep(4)
        break
#cv2.imshow(')
camera.release()
video.release()
cv2.destroyAllWindows()

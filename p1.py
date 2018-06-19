import cv2
import numpy as np
cap=cv2.VideoCapture(0)
#To save video file we use the following command
fourcc = cv2.VideoWriter_fourcc(*'XVID')
#The fourcc codes is XVID here.
#The arguments are filename, FourCC is a 4-byte code used to specify the video codec,frames per second, size(hieght,width)
out = cv2.VideoWriter('output.avi',fourcc, 16.0, (640,480))
while True:
    ret,frame=cap.read()
    #Writing the video file
    out.write(frame)
    #The command below basically just converts the color from normal to gray
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    if cv2.waitKey(100) & 0xFF==ord('q'):
        break
cap.release()
out.release()
cv2.destroyAllWindows()

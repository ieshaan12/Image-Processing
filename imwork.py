import numpy as np
import cv2

img=cv2.imread('olives.jpg',cv2.IMREAD_COLOR)

kernel=np.ones((15,15),np.float32)/225
edged=np.array([[0,1,0],[1,-4,1],[0,1,0]])
edgee=np.array([[0,0,0],[-1,1,0],[0,0,0]])
blur=np.array([[1,1,1],[1,1,1],[1,1,1]])
sharp=np.array([[0,0,0,0,0],[0,0,-1,0,0],[0,-1,5,-1,0],[0,0,-1,0,0],[0,0,0,0,0]])
emboss=np.array([[-2,-1,0],[-1,1,1],[0,1,2]])

ie=cv2.filter2D(img,-1,edged)
iee=cv2.filter2D(img,-1,edgee)
ib=cv2.filter2D(img,-1,blur)
ih=cv2.filter2D(img,-1,sharp)
iem=cv2.filter2D(img,-1,emboss)
smooth=cv2.filter2D(img,-1,kernel)

blurr=cv2.GaussianBlur(img,(15,15),0)
median=cv2.medianBlur(img,15)
bilateral=cv2.bilateralFilter(img,15,75,75)

cv2.imshow('Image-Edge',ie)
#cv2.imshow('Image-Edge-Enhance',iee)
#cv2.imshow('Image-Blur',ib)
#cv2.imshow('Image-Sharp',ih)
#cv2.imshow('Image-Emboss',iem)
#cv2.imshow('MEDIAN',median)
#cv2.imshow('BLUR',blurr)
#cv2.imshow('bilateral',bilateral)

cv2.waitKey(0)
cv2.destroyAllWindows()

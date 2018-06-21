import numpy as np
import cv2
#Importing images
img1=cv2.imread('image1.jpg',cv2.IMREAD_COLOR)
img2=cv2.imread('image2.jpg',cv2.IMREAD_COLOR)

shot=cv2.imread('name.jpg',cv2.IMREAD_COLOR)

r,c,s=shot.shape

roi1=img1[0:r,0:c]
roi2=img2[0:r,0:c]
#cv2.imshow('roi1',roi1)
#cv2.imshow('roi2',roi2)
shot1=cv2.cvtColor(shot,cv2.COLOR_BGR2GRAY)
ret,masked=cv2.threshold(shot1,100,255,cv2.THRESH_BINARY)
masked_inv=cv2.bitwise_not(masked)
cv2.imshow('masked',masked)
cv2.imshow('maskedinv',masked_inv)
img1_bg=cv2.bitwise_and(roi1,roi1,mask=masked)
img2_bg=cv2.bitwise_and(roi2,roi2,mask=masked)
shot_fg=cv2.bitwise_and(shot,shot,mask=masked_inv)
#cv2.imshow('imgbg',img1_bg)
#cv2.imshow('imgfg',img2_fg)
res1=cv2.add(img1_bg,shot_fg)
res2=cv2.add(img2_bg,shot_fg)
#cv2.imshow('res1',res1)
#cv2.imshow('res2',res2)
img1[0:r,0:c]=res1
img2[0:r,0:c]=res2

cv2.imshow('img1',img1)
cv2.imshow('img2',img2)

#cv2.imshow('masked',masked)
cv2.waitKey(0)
cv2.destroyAllWindows()

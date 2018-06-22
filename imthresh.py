import cv2
import numpy as np

img=cv2.imread('bookpage.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,threshold=cv2.threshold(img,10,255, cv2.THRESH_BINARY)
retg,thresholdg=cv2.threshold(gray,10,255, cv2.THRESH_BINARY)

#Adaptive Method - It decides how thresholding value is calculated.
#cv2.ADAPTIVE_THRESH_MEAN_C : threshold value is the mean of neighbourhood area.
#cv2.ADAPTIVE_THRESH_GAUSSIAN_C : threshold value is the weighted sum of neighbourhood values where weights are a gaussian window.

gaus=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,171,1)
mean=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,171,1)

#For threshold value, simply pass zero. Then the algorithm finds the optimal threshold value and returns you as the second output, retVal
reto,otsu=cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

print(reto)
cv2.imshow('mean',mean)
cv2.imshow('gaus',gaus)
cv2.imshow('OTSU',otsu)
#cv2.imshow('threshg',thresholdg)
#cv2.imshow('thresh',threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()

import time
import cv2
import matplotlib.pyplot as plt
camera = cv2.VideoCapture(0)
time.sleep(0.1) 
return_value, image = camera.read()
cv2.imwrite("image.png", image)#Used for saving an image file
#Use the command image=camera.imread('image.png',cv2.IMREAD_GRAYSCALE) for removing the opacity (b,g,r,a)
#image=cv2.imread('image.png')#cv2.IMREAD_GRAYSCALE) #Reads the image file
#cv2.imshow('image.png',image)   #Shows the image file
plt.imshow(image)
#plt.plot()
plt.show()
#cv2.imshow('image.png')

del(camera)

import cv2
import os
import numpy as np

image_1 = os.path.join(os.path.dirname(os.path.abspath(__file__)),'girl.jpg')


img = cv2.imread(image_1,0)
img = cv2.resize(img,(300,300))
_,mask= cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((2,2),np.uint8)# 5x5 kernel with full of ones. 


#all morhological opr
e = cv2.erode(mask,kernel) 
d = cv2.dilate(mask,kernel)
o = cv2.morphologyEx(mask,cv2.MORPH_OPEN,kernel)
c= cv2.morphologyEx(mask,cv2.MORPH_CLOSE,kernel)
x1 = cv2.morphologyEx(mask,cv2.MORPH_TOPHAT,kernel)   #diff b/w mask and opening
x2 = cv2.morphologyEx(mask,cv2.MORPH_GRADIENT,kernel) #diff b/w dilation and erosion
x3 = cv2.morphologyEx(mask,cv2.MORPH_BLACKHAT,kernel)  

#display all the result

cv2.imshow("img",img) 
cv2.imshow("mask==",mask)
cv2.imshow("erosion==",e)
cv2.imshow("dilate==",d)
cv2.imshow("opening==",o)
cv2.imshow("closing",c) 
cv2.imshow("x1",x1) 
cv2.imshow("x2",x2) 
cv2.imshow("x3",x3) 



cv2.imshow('Image',img)
cv2.imshow('Mask',mask)
cv2.imshow('Kernel',kernel)
cv2.imshow('Erode',e)
cv2.imshow('Dilate',d)

cv2.waitKey()
cv2.destroyAllWindows()
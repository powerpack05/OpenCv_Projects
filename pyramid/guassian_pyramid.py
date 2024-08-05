import cv2
import numpy as np


#load image into gray scale
img = cv2.imread(r"E:\open_cv_project\pyramid\avengers.jpg")
img = cv2.resize(img,(700,700))

#Gaussian Pyramid Have 2 function-1) cv2.pyrUp(),2)-cv2.pyrDown()
#pyrdown----
pd1 = cv2.pyrDown(img)
pd2 = cv2.pyrDown(pd1)

#pyrup
#if we pyrup any pyrdown image both are not equal
pu1 = cv2.pyrUp(pd2)


#results------------------
cv2.imshow("original==",img)
cv2.imshow("pd1==",pd1)
cv2.imshow("pd2==",pd2)
cv2.imshow("pu1==",pu1)

cv2.waitKey(0)
cv2.destroyAllWindows()

#using loop to generate pyramid
#load image into gray scale
"""
img = cv2.imread("E:\open_cv_project\pyramid\avengers.jpg")
img = cv2.resize(img,(700,700))

img1 = img.copy()
data = [img1]

for i in range(4):
    img1 = cv2.pyrDown(img1)
    data.append(img1)
    cv2.imshow("res"+str(i),img1)

cv2.imshow("original==",img)
cv2.waitKey(0)
cv2.destroyAllWindows()    
"""    
    
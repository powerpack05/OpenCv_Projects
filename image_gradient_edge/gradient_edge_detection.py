import cv2
import numpy as np
import os

image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'avengers.jpg')

img = cv2.imread(image_path)
img = cv2.resize(img,(600,600))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#Laplacian Derivative---It calculate laplace derivate
#parameter(img,data_type for -ve val,ksize)
#kernal size must be odd
lap = cv2.Laplacian(img_gray,cv2.CV_64F,ksize = 3) #also pass kernal size
lap = np.uint8(np.absolute(lap))

#Sobel operation - 
# is a joint Gausssian smoothing plus differentiation operation, 
#so it is more  resistant to noise
#This is use for x and y bth
#parameter (img,type for -ve val,x = 1,y = 0,ksize)
#Sobel X focus on vertical lines
#Sobel y focus on horizontal lines

sobelX = cv2.Sobel(img_gray,cv2.CV_64F,1,0,ksize = 3) #here 1 means x direction
sobelY = cv2.Sobel(img_gray,cv2.CV_64F,0,1,ksize = 3) #here 1 means y direction

sobelX = np.uint8(np.absolute(sobelX))
sobelY= np.uint8(np.absolute(sobelY))

#finally combine sobelX and sobelY togather
sobelcombine = cv2.bitwise_or(sobelX,sobelY)

cv2.imshow("original==",img)
cv2.imshow("gray====",img_gray)
cv2.imshow("Laplacian==",lap)
cv2.imshow("SobelX===",sobelX)
cv2.imshow("SobelY==",sobelY)
cv2.imshow("COmbined image==",sobelcombine)

cv2.waitKey()
cv2.destroyAllWindows()
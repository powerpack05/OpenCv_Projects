import cv2
import os
import numpy as np


image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'logo.jpg')

img = cv2.imread(image_path)

img1 = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret , thresh = cv2.threshold(img1,15,255,cv2.THRESH_BINARY_INV)

counts , hier = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
print(counts,len(counts))

img = cv2.drawContours(img,counts,-1,(177,123,12),4)

cv2.imshow('Image',img)
cv2.imshow('Image 1',img1)
cv2.imshow('Thres',thresh)

cv2.waitKey()
cv2.destroyAllWindows()
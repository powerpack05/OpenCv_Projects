import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'col_balls.jpg')

img = cv2.imread(image_path,0)

_,mask = cv2.threshold(img,230,255,cv2.THRESH_BINARY_INV)
kernel = np.ones((5,5),np.uint8)
erode = cv2.erode(mask,kernel)
dil = cv2.dilate(mask,kernel)

cv2.imshow('Gray Scale',img)
cv2.imshow('Black and White',mask)
cv2.imshow('Erode',erode)
cv2.imshow('Dilation',dil)


cv2.waitKey()
cv2.destroyAllWindows()


# list_images = [img,mask,erode,dil]
# titles = ["image","mask","eorde","dilate"]
# for i in range(len(list_images)):
#     plt.subplot(2,2,i+1)
#     plt.imshow(list_images[i],'gray')
#     plt.title(titles[i]) 
#     plt.xticks([]),plt.yticks([])
# plt.show()   
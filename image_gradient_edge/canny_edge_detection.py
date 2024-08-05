import cv2
import numpy as np
#building trackbar with canny edge

#load image into gray scale
img = cv2.imread(r"E:\open_cv_project\image_gradient_edge\building.jpg")
img = cv2.resize(img,(600,700))
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

def nothing(x):
    pass

cv2.namedWindow("Canny")
cv2.createTrackbar("Threshold", "Canny", 0, 255, nothing)

while True:
    a= cv2.getTrackbarPos('Threshold','Canny')
    
    print(a)
    res = cv2.Canny(img_gray,a,255)
    cv2.imshow("Canny",res)
    k=cv2.waitKey(1) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()







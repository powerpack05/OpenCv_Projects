import cv2
import os

# Load the two images
path_1 = os.path.join(os.path.dirname(os.path.abspath(__file__)),'hero1.jpg')
path_2 = os.path.join(os.path.dirname(os.path.abspath(__file__)),'strom_breaker.jpg')



image_1 = cv2.imread(path_1)
image_2 = cv2.imread(path_2)


image_1 = cv2.resize(image_1,(1024,800))
image_2 = cv2.resize(image_2,(600,600))

# I want to fix image 2 data into image 1

r,c,ch = image_2.shape
print(r,c,ch)

# roi ==

roi = image_1[0:r,0:c]


# now creating mask for image 1

img_gray = cv2.cvtColor(image_2,cv2.COLOR_BGR2GRAY)

# creating the mask using threshloding
_ ,mask = cv2.threshold(img_gray,50,255,cv2.THRESH_BINARY)

# Reverse the mask
mask_inv = cv2.bitwise_not(mask)

# put mask into roi
img1_bg = cv2.bitwise_and(roi,roi,mask=mask_inv)

# taking only the region of colour from original colour

img2_bg =cv2.bitwise_and(image_2,image_2,mask)

res = cv2.add(img1_bg,img2_bg)

final = image_1

final[0:r,0:c] = res

cv2.imshow('Image 1',image_1)
cv2.imshow('Image 2',image_2)
cv2.imshow('roi',roi)
cv2.imshow('Gray',img_gray)
cv2.imshow('MASK',mask)
cv2.imshow('bitwise',img2_bg)
cv2.imshow('roi img',img1_bg)
cv2.imshow('Result',res)
cv2.imshow('Final',final)

cv2.waitKey()
cv2.destroyAllWindows()

# Region of Interest

import cv2
import numpy as np

image_path = r"E:\open_cv_project\Region of Interest\Thor.jpg"
image = cv2.imread(image_path)
image_resize = cv2.resize(image, dsize=(800, 800))
print(f"Image Shape - {image_resize.shape}")

# Region of interest
# (300,90),(430,295) -- (x1,y1),(x2,y2)
# [(y1,y2),(x1,x2)]
roi = image_resize[60:200, 290:420]  # 140,130

image_resize[60:200, 420:550] = roi
image_resize[60:200, 550:680] = roi
image_resize[60:200, 160:290] = roi
image_resize[60:200, 30:160] = roi

image_path_1 = r"E:\open_cv_project\Region of Interest\ironman.jpg"
img = cv2.imread(image_path_1)
image_resize_1 = cv2.resize(img, dsize=(800, 800))
image_resize_1[243:383, 320:450] = roi

cv2.imshow("Image", image_resize)
cv2.imshow("ROI", roi)
cv2.imshow("Iron Man", image_resize_1)
cv2.waitKey()
cv2.destroyAllWindows()

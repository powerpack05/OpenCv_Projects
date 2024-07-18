import cv2
import numpy as np


image_path = r"E:\open_cv_project\Image Operations\pickachu_1.jpg"
image = cv2.imread(image_path)
print(f"Image Shape -{image.shape}-[height,width,colour_channels]")
print(f"No of pixels - {image.size}")
print(f"Image type - {type(image)}")
print(f"Image data type - {image.dtype}")

# Acessing the pixel values by row and column cordinates
px = image[550, 400]

blue_px = image[550, 400, 0]
green_px = image[550, 400, 1]
red_px = image[550, 400, 2]
print(blue_px, green_px, red_px)
print("Pixel values", px)
cv2.imshow("Image", image)
cv2.waitKey()
cv2.destroyAllWindows()

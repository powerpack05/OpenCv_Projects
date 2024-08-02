"""
Thresholding Techniques in OpenCV

Thresholding is a fundamental technique in image processing and computer vision, used to create binary images from grayscale images. It simplifies the analysis of images by reducing the complexity of the image data.

This script demonstrates the following thresholding techniques:
1. Binary Thresholding
2. Binary Inverse Thresholding
3. Truncate Thresholding
4. To Zero Thresholding

Author: Farheen Syed
Date: 02-08-2024
"""

import cv2
import os

# Reading the image in grayscale mode
image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'black_white.jpg')
img = cv2.imread(image_path, flags=0)

# Ensure the image was loaded successfully
if img is None:
    raise FileNotFoundError(f"Image file not found at {image_path}")

# 1. Binary Thresholding
# If the pixel value is below 50, it is set to 0 (black).
# If the pixel value is above 50, it is set to 255 (white).
_, th1 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY)

# 2. Binary Inverse Thresholding
# If the pixel value is below 50, it is set to 255 (white).
# If the pixel value is above 50, it is set to 0 (black).
_, th2 = cv2.threshold(img, 50, 255, cv2.THRESH_BINARY_INV)

# 3. Truncate Thresholding
# If the pixel value is above 127, it is set to 127.
# If the pixel value is below 127, it remains unchanged.
_, th3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)

# 4. To Zero Thresholding
# If the pixel value is below 127, it is set to 0 (black).
# If the pixel value is above 127, it remains unchanged.
_, th4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)

# Displaying the images
cv2.imshow('Black & White', img)
cv2.imshow('Threshold Binary', th1)
cv2.imshow('Threshold Binary Inverse', th2)
cv2.imshow('Threshold Truncate', th3)
cv2.imshow('Threshold To Zero', th4)

# Wait indefinitely for a key press
cv2.waitKey(0)

# Close all OpenCV windows
cv2.destroyAllWindows()

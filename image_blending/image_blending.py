import cv2
import numpy as np


thor = r"E:\open_cv_project\image_blending\Thor.jpg"
thor_1 = r"E:\open_cv_project\image_blending\Thor_1.jpg"

image = cv2.imread(thor)
imag_resize = cv2.resize(image, dsize=(728, 455))
image_1 = cv2.imread(thor_1)
print(f"Image shape of the Thor - {imag_resize.shape}")
print(f"Image shape of the Thor 1 -{image_1.shape}")


# Blending the images
result = imag_resize + image_1

# By function
result_1 = cv2.add(image_1, imag_resize)

# WEIGHTED ADD
result_2 = cv2.addWeighted(image_1, 0.5, imag_resize, 0.5, 0)

cv2.imshow("Thor", imag_resize)
cv2.imshow("Thor 1", image_1)
cv2.imshow("Result ", result)
cv2.imshow("Result 1", result_1)
cv2.imshow("Result 2", result_2)
cv2.waitKey()
cv2.destroyAllWindows()

import cv2
import numpy as np

image_path = "E:\open_cv_project\Image Operations\pickachu_1.jpg"
image = cv2.imread(image_path)
brdr = cv2.copyMakeBorder(
    src=image,
    top=10,
    bottom=10,
    left=10,
    right=10,
    borderType=cv2.BORDER_CONSTANT,
    value=[255, 255, 255],
)

cv2.imshow("Image", image)
cv2.imshow("Border Image", brdr)
cv2.waitKey()
cv2.destroyAllWindows()

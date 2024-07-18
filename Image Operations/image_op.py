# Image Operations with pixels and cordinates

import cv2
import numpy as np
import numpy

# Read an Image
image = cv2.imread(r"E:\open_cv_project\Image Operations\pickachu_1.jpg")

print(f"Image -- {image.shape}-[height,width,colour_channels]")
print(f"No of pixels -{image.size}")
print(f"Image Data type -{image.dtype}")
print(f"Image type - {type(image)}")


# Now try to split the image
# return the three channels into blue,green,red
def channels_spilt(x: numpy.ndarray):
    blue, green, red = cv2.split(image)
    return blue, green, red


blue, green, red = channels_spilt(image)


# for merging the color channels
mrg1 = cv2.merge((red, blue, green))
mrg2 = cv2.merge((red, green, blue))
mrg3 = cv2.merge((blue, red, green))

# cv2.imshow("RED", red)
# cv2.imshow("GREEN", green)
# cv2.imshow("BLUE", blue)
cv2.imshow("Merged - RBG", mrg1)
cv2.imshow("Merged - RGB", mrg2)
cv2.imshow("Merged - BRG", mrg3)
cv2.imshow("Image", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

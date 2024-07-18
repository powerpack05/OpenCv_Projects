# Create colour picker project

import cv2
import numpy as np


def cross(x):
    pass


# blank
image = np.zeros(shape=[500, 500, 3], dtype=np.uint8)
cv2.namedWindow("Colour Picker")

# create switch
switch = "0:OFF\n1:ON"
cv2.createTrackbar(switch, "Colour Picker", 0, 1, cross)

# creating the rgb
cv2.createTrackbar("RED", "Colour Picker", 0, 255, cross)
cv2.createTrackbar("BLUE", "Colour Picker", 0, 255, cross)
cv2.createTrackbar("GREEN", "Colour Picker", 0, 255, cross)


while True:

    cv2.imshow("Colour Picker", image)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    s = cv2.getTrackbarPos(switch, "Colour Picker")
    red = cv2.getTrackbarPos("RED", "Colour Picker")
    blue = cv2.getTrackbarPos("BLUE", "Colour Picker")
    green = cv2.getTrackbarPos("GREEN", "Colour Picker")

    if s == 0:
        image[:] = 0

    else:
        image[:] = [blue, green, red]

cv2.destroyAllWindows()

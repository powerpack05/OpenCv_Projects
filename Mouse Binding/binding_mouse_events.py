import cv2
import numpy as np

# Mouse callback functions


def draw(event, x, y, flags, param):

    if event == cv2.EVENT_LBUTTONDBLCLK:

        cv2.circle(
            img=image, center=(x, y), radius=100, color=(255, 0, 0), thickness=-1
        )
    if event == cv2.EVENT_RBUTTONDBLCLK:

        cv2.rectangle(
            img=image,
            pt1=(x, y),
            pt2=(x + 100, y + 100),
            color=(0, 0, 255),
            thickness=-1,
        )


cv2.namedWindow(winname="MOUSE")

image = np.ones(shape=[500, 500, 3], dtype=np.uint8) * 255
cv2.setMouseCallback("MOUSE", draw)

while True:

    cv2.imshow("MOUSE", image)

    if cv2.waitKey(1) & 0xFF == 27:
        break

cv2.destroyAllWindows()

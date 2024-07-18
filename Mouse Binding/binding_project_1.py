import cv2
import numpy as np


# Mouse callback function
def mouse_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        formatted_text = "({},{})".format(x, y)
        cv2.putText(
            img=image,
            text=formatted_text,
            org=(x, y),
            fontFace=cv2.FONT_HERSHEY_DUPLEX,
            fontScale=1,
            color=(255, 0, 0),
            thickness=1,
            lineType=cv2.LINE_AA,
        )

    if event == cv2.EVENT_RBUTTONDBLCLK:
        blue = image[y, x, 0]
        green = image[y, x, 1]
        red = image[y, x, 2]

        font_face = cv2.FONT_HERSHEY_COMPLEX_SMALL
        cv2.putText(
            img=image,
            text="B: {}, G: {}, R: {}".format(blue, green, red),
            org=(x, y),
            fontFace=font_face,
            fontScale=1,
            color=(255, 45, 34),
            thickness=1,
            lineType=cv2.LINE_AA,
        )


cv2.namedWindow(winname="Frame")
image = np.ones(shape=[500, 500, 3], dtype=np.uint8) * 255

cv2.setMouseCallback("Frame", mouse_event)

while True:
    cv2.imshow("Frame", image)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

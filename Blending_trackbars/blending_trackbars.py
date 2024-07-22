import cv2
import numpy as np

thor_1 = r"E:\open_cv_project\Blending_trackbars\Thor_1.jpg"
thor_2 = r"E:\open_cv_project\Blending_trackbars\Thor.jpg"

image_1 = cv2.imread(thor_1)
image_1 = cv2.resize(image_1, dsize=(500, 500))
image_2 = cv2.imread(thor_2)
image_2 = cv2.resize(image_2, dsize=(500, 500))


def blend(x):
    pass


cv2.namedWindow("Image")
img = np.zeros((400, 400, 3), np.uint8)
cv2.createTrackbar("Alpha", "Image", 0, 100, blend)
switch = "0:OFF \n1:ON"
cv2.createTrackbar(switch, "Image", 0, 1, blend)

while True:

    s = cv2.getTrackbarPos(switch, "Image")
    a = cv2.getTrackbarPos("Alpha", "Image")
    n = float(a / 100)
    print(n)

    if s == 0:
        dst = img[:]  # Empty black image of the same size
    else:
        dst = cv2.addWeighted(image_1, 1 - n, image_2, n, 0)
        cv2.putText(dst, str(a), (20, 40), cv2.FONT_ITALIC, 1, (0, 255, 255), 2)

    cv2.imshow("Image", dst)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()

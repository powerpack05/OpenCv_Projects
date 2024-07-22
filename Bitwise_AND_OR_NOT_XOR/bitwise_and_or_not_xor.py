import cv2
import numpy as np


img_1 = np.zeros(shape=[500, 250, 3], dtype=np.uint8)
img_1 = cv2.rectangle(img_1, (50, 100), (70, 400), (255, 255, 255), cv2.FILLED)
cv2.imshow("Image_1", img_1)

img_2 = np.zeros(shape=[500, 250, 3], dtype=np.uint8)
img_2 = cv2.rectangle(img_2, (10, 50), (50, 300), (255, 255, 255), cv2.FILLED)
cv2.imshow("Image_2", img_2)

bit_wise_and = cv2.bitwise_and(img_1, img_1)
cv2.imshow("Bit Wise AND", bit_wise_and)
bit_wise_or = cv2.bitwise_or(img_1, img_2)
# bit_wise_xor = cv2.bitwise_xor(img_1, img_2)
# bit_wise_not_image_1 = cv2.bitwise_not(img_1)
# bit_wise_not_image_2 = cv2.bitwise_not(img_2)
cv2.imshow("Bit Wise OR", bit_wise_or)

cv2.waitKey()
cv2.destroyAllWindows()

import cv2

image_path = r"E:/open_cv_project/Dr_Avengers.jpeg"
# Gray Scale Image
gray_scale = cv2.imread(filename=image_path, flags=0)  # (height,width,colour_channel)
gray_scale = cv2.resize(
    src=gray_scale, dsize=(700, 700)
)  # Resizing the image(width,height)
cv2.imshow(winname="Dr.Avengers GrayScale", mat=gray_scale)

# Colour channel
image_read = cv2.imread(filename=image_path, flags=1)  # (height,width,colour_channel)
image_read = cv2.resize(
    src=image_read, dsize=(700, 700)
)  # Resizing the image(width,height)
cv2.imshow(winname="Dr.Avengers", mat=image_read)

# flags = -1
# Colour channel
image_distort = cv2.imread(
    filename=image_path, flags=-1
)  # (height,width,colour_channel)
image_distort = cv2.resize(
    src=image_distort, dsize=(700, 700)
)  # Resizing the image(width,height)
cv2.imshow(winname="Dr.Avengers colour distort", mat=image_distort)


cv2.waitKey()
cv2.destroyAllWindows()

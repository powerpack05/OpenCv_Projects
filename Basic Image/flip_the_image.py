import cv2

# Resizing the image
image_path = r"E:\open_cv_project\cat.jpg"
org_img = cv2.imread(image_path, flags=1)
print(f"Image shape - {org_img.shape}--[height,width,color_channel]")
image_resize = cv2.resize(org_img, dsize=(500, 550))
cv2.imshow("Original Cat", image_resize)

# Flip the image vertical flip
image_hori = cv2.flip(image_resize, 0)
cv2.imshow("Vertical Flip", image_hori)

# Flip the image horizontal flip
image_vert = cv2.flip(image_resize, 1)
cv2.imshow("Horizontal flip", image_vert)
cv2.waitKey()
cv2.destroyAllWindows()

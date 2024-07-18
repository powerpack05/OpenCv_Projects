import cv2


user_path = input("Enter the path:\n")
image = cv2.imread(filename=user_path, flags=0)
image_resize = cv2.resize(src=image, dsize=(800, 800))
cv2.imshow(winname="Dr Avengers", mat=image_resize)

k = cv2.waitKey(0)
if k == ord("s"):
    cv2.imwrite(filename="E:\open_cv_project\Dr_Avengers_Gray.jpeg", img=image_resize)
else:
    cv2.destroyAllWindows()

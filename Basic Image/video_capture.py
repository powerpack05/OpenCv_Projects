import cv2

video_path = r"E:\open_cv_project\jacksparrow.mp4"
capture = cv2.VideoCapture(video_path)
if not capture.isOpened():
    print(f"Error while opening the video")
else:
    print("Video object", capture)
    count = 0
    while True:
        ret, frame = capture.read()
        gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        if not ret:
            print(f"Problem in while opening the Frame")
            break
        count += 1
        cv2.imshow("Frame", frame)
        cv2.imshow("Gray Scale", gray_scale)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    print("Over all frames in the video", count)
    cv2.destroyAllWindows()

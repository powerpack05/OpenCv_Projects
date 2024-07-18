import cv2
import numpy as np
import datetime


def draw_functions_video(video_path):
    """Read the video frames and draw the functions
    Args:
    video_path (str): path to the video file
    """

    cap = cv2.VideoCapture(video_path)
    # cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

    if not cap.isOpened():
        print("Error opening video stream or file")
        return

    while True:
        ret, frame = cap.read()

        if not ret:
            break

        font = cv2.FONT_HERSHEY_COMPLEX_SMALL
        text = (
            "Height: "
            + str(int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))
            + " Width: "
            + str(int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))
        )
        date_data = "DateTime: " + str(datetime.datetime.now())

        frame = cv2.putText(
            img=frame,
            text=text,
            org=(5, 40),
            fontFace=font,
            fontScale=1,
            color=(0, 255, 255),
            thickness=2,
            lineType=cv2.LINE_AA,
        )

        frame = cv2.putText(
            img=frame,
            text=date_data,
            org=(5, 80),
            fontFace=font,
            fontScale=1,
            color=(100, 20, 20),
            thickness=2,
            lineType=cv2.LINE_AA,
        )

        cv2.imshow("Frame", frame)

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


video_path = r"E:\open_cv_project\jacksparrow.mp4"
draw_functions_video(video_path=video_path)

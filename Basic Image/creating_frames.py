import cv2
import os


def extract_frames(video_path, save_dir):
    """
    Extract frames from a video and save them with unique names.

    Args:
        video_path (str): Path to the video file.
        save_dir (str): Directory to save the extracted frames.
    """

    if not os.path.exists(save_dir):
        os.makedirs(save_dir)

    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print(f"Error opening video stream or file: {video_path}")
        return

    frame_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_name = f"frame_{frame_count:04d}.jpg"
        save_path = os.path.join(save_dir, frame_name)
        cap.set(cv2.CAP_PROP_POS_MSEC, frame_count * 100)
        cv2.imwrite(save_path, frame)
        frame_count += 1

        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()
    print(f"Extracted {frame_count} frames from {video_path}")


# Calling the function
video_path = "E:/open_cv_project/jacksparrow.mp4"
save_dir = "E:/open_cv_project/jack_sparrow_frames"
extract_frames(video_path, save_dir)

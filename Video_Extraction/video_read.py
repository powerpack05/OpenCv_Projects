import cv2  # Image Processing
import os  # Handle File paths
import sys  # For command-line arguments
from typing import Optional


def video_frames(video_path: str) -> None:
    """
    Reads and displays frames from a given video path.

    Args:
        video_path (str): Path to the video file.

    Returns:
        None
    """
    # Check if the file exists
    if not os.path.exists(video_path):
        print(f"Error: The video file {video_path} does not exist.")
        return

    # Reading the video from the given path
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        print("Error: Unable to open the video.")
        return

    while True:
        ref, frame = cap.read()

        if not ref:
            print("Error: Unable to read frames or end of video reached.")
            break

        # Resize the frame to half its original size
        resize_frame = cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))

        # Display the resized frame
        cv2.imshow("Frame", resize_frame)

        # Wait for 5ms and break on 'Esc' key press
        k = cv2.waitKey(5)
        if k & 0xFF == 27:  # Esc key
            break

    # Release resources
    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    # Allow passing the video path as a command-line argument
    if len(sys.argv) > 1:
        video_path = sys.argv[1]
    else:
        video_abs_path = os.path.dirname(os.path.abspath(__file__))
        video_path = os.path.join(video_abs_path, "ssr.mp4")

    video_frames(video_path)


# import sys


# def main():
#     print("Command-line arguments:")
#     for i, arg in enumerate(sys.argv):
#         print(f"Argument {i}: {arg}")
#         print(sys.argv)


# if __name__ == "__main__":
#     main()

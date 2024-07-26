import cv2  # Image Processing
import os  # For Handling File Paths
import argparse  # For Command Line Arguments


def video_length(video_path: str) -> None:
    """
    This function takes a video path as input and returns the length of the video in seconds.
    Args:
        video_path(str):This is the video path
    Returns:
        Total Video length in seconds.
    """

    if not os.path.exists(video_path):
        print(f"Error:provided video path {video_path} does not exists")
        return

    capture = cv2.VideoCapture(video_path)

    if not capture.isOpened():
        print(f"Error:unable to open video {video_path}")
        return
    else:

        total_frames = int(capture.get(cv2.CAP_PROP_FRAME_COUNT))
        frames_per_sec = capture.get(cv2.CAP_PROP_FPS)

        video_len_sec = total_frames / frames_per_sec

        video_len_in_min = video_len_sec / 60
        video_len_in_sec = video_len_sec % 60

        return f"Total Video Length in min-{video_len_in_min} and {video_len_in_sec} in seconds"

        capture.release()


def parse_arguments():
    """
    Parses Command line Arguments
    Returns:
      argparse.Namespace:Parsed Arguments.
    """

    parser = argparse.ArgumentParser(description="Read and Display video Length")
    parser.add_argument(
        "video_path",
        type=str,
        nargs="?",
        default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "ssr.mp4"),
        help="Path to the video file",
    )

    return parser.parse_args()


if __name__ == "__main__":

    args = parse_arguments()
    print(f"Video path {args.video_path}")
    vid_len = video_length(video_path=args.video_path)
    print(vid_len)

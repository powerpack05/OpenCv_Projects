import cv2  # Image Processing
import os  # For Handle File Paths
import argparse  # For Command Line Prompt

def extract_frames_save(video_path: str, frame_path: str):
    """
    Read the video and extract all the frames and save into the new path
    Args:
        video_path(str): path of the video to read
        frame_path(str): path of the folder to save the frames
    Returns:
        None
    """
    if not os.path.exists(video_path):
        print(f"Error: Unable to find the path {video_path}")
        return

    capture = cv2.VideoCapture(video_path)

    if not capture.isOpened():
        print("Error: Unable to open the video")
        return

    frame_count = 0
    while True:
        ref, frame = capture.read()

        if not ref:
            print("Reached the end of the video or unable to read frame")
            break

        if not os.path.exists(frame_path):
            os.makedirs(frame_path)

        frame_count += 1
        frame_name = f"{frame_count:04d}.jpg"

        cv2.imwrite(os.path.join(frame_path, frame_name), frame)

    capture.release()
    cv2.destroyAllWindows()

def parse_arguments():
    """
    Parses Command line Arguments
    Returns:
        argparse.Namespace: Parsed Arguments.
    """
    parser = argparse.ArgumentParser(description="Read and Save the Frames")

    parser.add_argument(
        "video_path",
        type=str,
        nargs="?",
        default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "ssr.mp4"),
        help="Path to the video file"
    )

    parser.add_argument(
        "frame_path",
        type=str,
        nargs="?",
        default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "Extracted_Frames"),
        help="Path to the folder to save frames"
    )

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    print(f"Video path: {args.video_path} and frame path: {args.frame_path}")
    extract_frames_save(args.video_path, args.frame_path)

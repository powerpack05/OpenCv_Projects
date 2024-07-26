import cv2  # Image processing
import os  # For Handling File paths
import argparse  # Command Line Arguments parsing


def video_frames(video_path: str) -> None:
    """
    Reads and displays frames from a given video path

    Args:
        video_path (str) : Path to the video file

    Returns:
        None
    """
    # check if the file exists
    if not os.path.exists(video_path):

        print(f"Error: The video file {video_path} does not exist")

        return

    # Reading the video from the given path
    capture = cv2.VideoCapture(video_path)

    if not capture.isOpened():
        print(f"Error:Unable to open the video")
        return

    while True:

        ref, frame = capture.read()

        if not ref:
            print(f"Error: Unable to read frames or end of video reached.")

        # Resize the frame halg of the original size
        resize_frame = cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))

        # Display the resized Image
        cv2.imshow("Frame", resize_frame)

        # Wait for 5ms and break on 'Esc' key press
        k = cv2.waitKey(5)

        if k & 0xFF == 27:  # # Esc key
            break

    # release resources
    capture.release()
    cv2.destroyAllWindows()


def parse_arguments():
    """
    Parses Command line Arguments
    Returns:
      argparse.Namespace:Parsed Arguments.
    """

    parser = argparse.ArgumentParser(description="Read and Display video Frames")
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
    print(f"Video_path :{args.video_path}")
    video_frames(args.video_path)

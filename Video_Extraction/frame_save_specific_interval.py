import cv2 # Image Processing
import os # For Handle the paths
import argparse # For Command Line Arguments


def at_specific_intervals(video_path:str,frame_path:str,specific_interval:int):
    
    
    """
    Reads the video and saves the frame at specific intervals
    Args:
        video_path(str):path of the video
        frame_path(str):path of the folder where the frames are to be saved
        specific_interval(int):interval at which the frames are to be saved
    Returns:
    None
    """
    
    if not os.path.exists(video_path):
        print("Video path does not exist")

    capture = cv2.VideoCapture(video_path)
    
    if not capture.isOpened():
        print("Video could not be opened")
        return
    
    frame_count = 0
    while True:
        
        ref,frame = capture.read()
        
        if not ref:
            print(f'Error:Unable to load the frame or reached at the end of the video.')
            break
        
        if not os.path.exists(frame_path):
            os.makedirs(frame_path)

            
        frames_per_sec = capture.get(cv2.CAP_PROP_FPS)
        frame_interval = int(frames_per_sec * specific_interval)
        
        if frame_count % frame_interval == 0:
            
            # Option 1: Frame name with interval
            frame_name = f'frame_{frame_count:04d}_interval_{specific_interval}.jpg'
            
            # Option 2: Frame name with time
            # frame_time = frame_count / frames_per_sec
            # frame_name = f'frame_{frame_count:04d}_time_{frame_time:.2f}.jpg'

            # Option 3: Frame name with unique ID
            # frame_name = f'frame_{frame_count:04d}_{uuid.uuid4()}.jpg'
            
            
            cv2.imwrite(os.path.join(frame_path,frame_name),frame)
            
        frame_count += 1
        
        
    capture.release()
    
    
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
    
    
    parser.add_argument(
        "--interval",
        type=float,
        nargs="?",
        default=1,
        help="Interval between frames to be extracted"
    )

    return parser.parse_args()


if __name__ == "__main__":
    
    args = parse_arguments()
    
    at_specific_intervals(args.video_path,args.frame_path,args.interval)
    
            
            
            
            
            
        
        
        
        
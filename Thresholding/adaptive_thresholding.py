import cv2
import os
import argparse


def adaptive_thresholding(image_path: str):
    img = cv2.imread(filename=image_path, flags=0)  # read image into a gray scale

    # Check if the image was loaded successfully
    if img is None:
        print("Error: Could not read the image.")
        return

    # Apply adaptive thresholding
    adaptive_thresh_mean = cv2.adaptiveThreshold(img, 255,
                                                 cv2.ADAPTIVE_THRESH_MEAN_C,
                                                 cv2.THRESH_BINARY,
                                                 11, 2)

    # Display the original and thresholded images
    cv2.imshow('Original Image', img)
    cv2.imshow('Adaptive Mean Threshold', adaptive_thresh_mean)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


def parse_arguments():
    parse = argparse.ArgumentParser(description='Arguments passing through command line window')
    parse.add_argument('image_path',
                       nargs='?',
                       default='thresholding/black_white.jpg',
                       help="provide the image path")

    return parse.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    adaptive_thresholding(image_path=args.image_path)

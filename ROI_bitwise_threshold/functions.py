import cv2
import os
import argparse

def roi_bitwise_threshold(image_paths):
    shapes = {}
    for num, image_path in enumerate(image_paths, start=1):
        if not os.path.exists(image_path):
            print(f'Check the image path: {image_path} does not exist...')
            raise FileNotFoundError(f"Image Path {image_path} Does Not Exist")

        img = cv2.imread(image_path)

        # Check if image is loaded successfully
        if img is None:
            print(f'Error: The image {image_path} could not be read.')
            continue

        shapes[f'image_{num}'] = img.shape

        cv2.imshow(f'Image: {image_path}', img)
        print(f'Displaying image {num}: {image_path}')

    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return shapes

def parse_arguments():
    parser = argparse.ArgumentParser(description='Passing arguments through the command line')

    parser.add_argument('--image_paths',
                        nargs='+',
                        default=[r'E:\open_cv_project\ROI_bitwise_threshold\hero1.jpg', r'E:\open_cv_project\ROI_bitwise_threshold\strom_breaker.JPG'],
                        help='Pass the image paths')

    return parser.parse_args()

if __name__ == "__main__":
    args = parse_arguments()
    shapes = roi_bitwise_threshold(args.image_paths)
    print(f'Image shapes:\n{shapes}')

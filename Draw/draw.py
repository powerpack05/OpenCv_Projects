import cv2
import numpy as np


def draw_shapes(black_bg, white_bg):
    # Draw a Line
    black_bg = cv2.line(
        img=black_bg, pt1=(0, 0), pt2=(200, 200), color=(255, 23, 1), thickness=10
    )  # color = (B,G,R)
    white_bg = cv2.line(
        img=white_bg, pt1=(10, 20), pt2=(50, 60), color=(23, 45, 255), thickness=10
    )

    # Draw an Arrowed Line
    black_bg = cv2.arrowedLine(
        img=black_bg, pt1=(0, 125), pt2=(255, 255), color=(255, 0, 0), thickness=2
    )
    white_bg = cv2.arrowedLine(
        img=white_bg, pt1=(0, 125), pt2=(255, 255), color=(10, 10, 10), thickness=4
    )

    # Draw a Rectangle
    black_bg = cv2.rectangle(
        img=black_bg, pt1=(10, 50), pt2=(50, 100), color=(244, 5, 6), thickness=-1
    )
    white_bg = cv2.rectangle(
        img=white_bg, pt1=(10, 50), pt2=(50, 100), color=(244, 5, 6), thickness=-1
    )

    # Draw a Circle
    black_bg = cv2.circle(
        img=black_bg,
        center=(int(black_bg.shape[1] // 2), int(black_bg.shape[0] // 2)),
        radius=10,
        color=(233, 45, 6),
        thickness=cv2.FILLED,
    )
    white_bg = cv2.circle(
        img=white_bg,
        center=(int(white_bg.shape[1] // 2), int(white_bg.shape[0] // 2)),
        radius=10,
        color=(0, 45, 6),
        thickness=cv2.FILLED,
    )

    # Draw an Ellipse
    black_bg = cv2.ellipse(
        img=black_bg,
        center=(black_bg.shape[1] // 2, black_bg.shape[0] // 2),
        axes=(100, 50),
        angle=0,
        startAngle=0,
        endAngle=360,
        color=(0, 255, 0),
        thickness=2,
    )
    white_bg = cv2.ellipse(
        img=white_bg,
        center=(white_bg.shape[1] // 2, white_bg.shape[0] // 2),
        axes=(100, 50),
        angle=0,
        startAngle=0,
        endAngle=360,
        color=(0, 0, 255),
        thickness=2,
    )

    # Put Text
    black_bg = cv2.putText(
        img=black_bg,
        text="Thor",
        org=(20, 100),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=4,
        color=(255, 0, 255),
        thickness=2,
        lineType=cv2.LINE_AA,
    )
    white_bg = cv2.putText(
        img=white_bg,
        text="Dead",
        org=(250, 300),
        fontFace=cv2.FONT_HERSHEY_SIMPLEX,
        fontScale=4,
        color=(0, 0, 255),
        thickness=4,
        lineType=cv2.LINE_AA,
    )

    cv2.imshow("Black Image", black_bg)
    cv2.imshow("White Image", white_bg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


# Create black and white images
black_data = np.zeros((500, 500, 3), dtype=np.uint8)
white_data = np.ones((500, 500, 3), dtype=np.uint8) * 255

draw_shapes(black_bg=black_data, white_bg=white_data)

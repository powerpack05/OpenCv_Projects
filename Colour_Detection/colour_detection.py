import cv2
import numpy as np

def nothing(x):
    pass

# Load the image
frame = cv2.imread(r"E:\open_cv_project\Colour_Detection\balls.jpg")

# Check if the image is loaded correctly
if frame is None:
    print("Error: Could not load image.")
    exit()

# Convert the image from BGR to HSV colour space
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

# Create a Window
cv2.namedWindow('Image')

# Create trackbars for colour change
cv2.createTrackbar('Hmin', 'Image', 0, 179, nothing)
cv2.createTrackbar('Hmax', 'Image', 0, 179, nothing)
cv2.createTrackbar('Smin', 'Image', 0, 255, nothing)
cv2.createTrackbar('Smax', 'Image', 0, 255, nothing)
cv2.createTrackbar('Vmin', 'Image', 0, 255, nothing)
cv2.createTrackbar('Vmax', 'Image', 0, 255, nothing)

# Set Default Values for Max HSV trackbars
cv2.setTrackbarPos('Hmax', 'Image', 179)
cv2.setTrackbarPos('Smax', 'Image', 255)
cv2.setTrackbarPos('Vmax', 'Image', 255)

# Process the image and update the result with trackbar adjustments
while True:
    # Get the current position of all trackbars
    h_min = cv2.getTrackbarPos('Hmin', 'Image')
    h_max = cv2.getTrackbarPos('Hmax', 'Image')
    s_min = cv2.getTrackbarPos('Smin', 'Image')
    s_max = cv2.getTrackbarPos('Smax', 'Image')
    v_min = cv2.getTrackbarPos('Vmin', 'Image')
    v_max = cv2.getTrackbarPos('Vmax', 'Image')

    # Set minimum and maximum HSV values to display
    lower = np.array([h_min, s_min, v_min])
    upper = np.array([h_max, s_max, v_max])

    # Create a mask with the specified HSV range
    mask = cv2.inRange(hsv, lower, upper)

    # Check the mask values
    print(f"Lower: {lower}, Upper: {upper}, Mask unique values: {np.unique(mask)}")

    # Bitwise-AND mask and original image
    result = cv2.bitwise_and(frame, frame, mask=mask)

    # Display the original frame, mask, and results
    cv2.imshow('Image', result)

    # Press 'q' to break the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Close all windows
cv2.destroyAllWindows()

import pandas as pd
import numpy as np
import cv2
import os

# Open the webcam
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

if not capture.isOpened():
    print("Cannot open camera")
    exit()

def nothing(x):
    pass

# Create a window
cv2.namedWindow('Frame')

# Create trackbars for color change
cv2.createTrackbar('Hue Min', 'Frame', 0, 255, nothing)
cv2.createTrackbar('Hue Max', 'Frame', 255, 255, nothing)
cv2.createTrackbar('Saturation Min', 'Frame', 0, 255, nothing)
cv2.createTrackbar('Saturation Max', 'Frame', 255, 255, nothing)
cv2.createTrackbar('Value Min', 'Frame', 0, 255, nothing)
cv2.createTrackbar('Value Max', 'Frame', 255, 255, nothing)

while True:
    # Capture frame-by-frame
    ret, frame = capture.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    # Get current positions of all trackbars
    l_hue = cv2.getTrackbarPos('Hue Min', 'Frame')
    u_hue = cv2.getTrackbarPos('Hue Max', 'Frame')
    l_sat = cv2.getTrackbarPos('Saturation Min', 'Frame')
    u_sat = cv2.getTrackbarPos('Saturation Max', 'Frame')
    l_val = cv2.getTrackbarPos('Value Min', 'Frame')
    u_val = cv2.getTrackbarPos('Value Max', 'Frame')
    
    # Define range of colors in HSV
    lower = np.array([l_hue, l_sat, l_val])
    upper = np.array([u_hue, u_sat, u_val])
    
    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Threshold the HSV image to get only colors within the specified range
    mask = cv2.inRange(hsv, lower, upper)
    
    # Bitwise-AND mask and original image
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    # Display the resulting frame
    cv2.imshow('HSV', hsv)
    cv2.imshow('Mask', mask)
    cv2.imshow('Frame', result)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
capture.release()
cv2.destroyAllWindows()

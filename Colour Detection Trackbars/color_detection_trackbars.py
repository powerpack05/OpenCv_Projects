import cv2
import os
import numpy as np
import pandas as pd

# Define the image path
image_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Colour_bars.jpg')
frame = cv2.imread(image_path)
frame = cv2.resize(frame, (frame.shape[1] // 2, frame.shape[0] // 2))
print(f'Image Shape - {frame.shape}')

def nothing(x):
    pass

# Create a named window
cv2.namedWindow('Frame')

# Create trackbars for color change
cv2.createTrackbar('Hue Min', 'Frame', 0, 255, nothing)
cv2.createTrackbar('Saturation Min', 'Frame', 0, 255, nothing)
cv2.createTrackbar('Value Min', 'Frame', 0, 255, nothing)

cv2.createTrackbar('Hue Max', 'Frame', 255, 255, nothing)
cv2.createTrackbar('Saturation Max', 'Frame', 255, 255, nothing)
cv2.createTrackbar('Value Max', 'Frame', 255, 255, nothing)

while True:
    # Convert the frame to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    # Get the new values of the trackbars
    l_hmin = cv2.getTrackbarPos('Hue Min', 'Frame')
    l_smin = cv2.getTrackbarPos('Saturation Min', 'Frame')
    l_vmin = cv2.getTrackbarPos('Value Min', 'Frame')
    
    u_hmax = cv2.getTrackbarPos('Hue Max', 'Frame')
    u_smax = cv2.getTrackbarPos('Saturation Max', 'Frame')
    u_vmax = cv2.getTrackbarPos('Value Max', 'Frame')
    
    # Set the lower and upper HSV range according to the trackbar positions
    lower = np.array([l_hmin, l_smin, l_vmin])
    upper = np.array([u_hmax, u_smax, u_vmax])
    
    # Create a mask based on the HSV range
    mask = cv2.inRange(hsv, lower, upper)
    
    # Bitwise-AND mask and original image
    result = cv2.bitwise_and(frame, frame, mask=mask)
    
    
    # Show the result in different windows
    cv2.imshow('HSV Image', hsv)
    cv2.imshow('Mask', mask)
    cv2.imshow('Frame', result)
    
    # Break the loop on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    elif cv2.waitKey(1) & 0XFF == ord('s'):
        
        final_dict = {
            'lower': lower.tolist(),
            'upper': upper.tolist(),
        }
        
        df = pd.DataFrame(final_dict)
        
        df.to_excel('hsv_colour_values.xlsx',index=False)
        
        

# Release the windows
cv2.destroyAllWindows()

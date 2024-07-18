import cv2

# Open a connection to the camera
capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)

# Check if the camera opened successfully
if not capture.isOpened():
    print("Error: Could not open camera.")
    exit()

# Define the codec and create a VideoWriter object
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # Codec for MP4 format
out = cv2.VideoWriter("output.mp4", fourcc, 20.0, (500, 500))

while True:
    ret, frame = capture.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Resize the frame
    frame_resized = cv2.resize(frame, (500, 500))

    # Convert to grayscale
    gray_scale = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2GRAY)

    # Display the frames
    cv2.imshow("Frame", frame_resized)
    cv2.imshow("GrayScale", gray_scale)

    # Write the resized frame to the output file
    out.write(frame_resized)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the camera and writer, and close all windows
capture.release()
out.release()
cv2.destroyAllWindows()

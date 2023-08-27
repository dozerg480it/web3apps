import cv2

def take_picture():
    # Open a connection to the camera (0 is usually the default camera)
    cap = cv2.VideoCapture(0)

    # Check if the camera is opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    # Capture a frame from the camera
    ret, frame = cap.read()

    # Check if the frame was captured successfully
    if not ret:
        print("Error: Could not capture frame.")
        cap.release()  # Release the camera
        return

    # Save the captured frame as an image
    cv2.imwrite("picture.jpg", frame)

    # Release the camera
    cap.release()

    print("Picture taken and saved as 'captured_image.jpg'.")

# Call the function to take a picture
take_picture()

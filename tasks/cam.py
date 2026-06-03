import cv2

# Open the default camera (0)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("❌ Cannot open camera")
    exit()

while True:
    # Read one frame
    ret, frame = cap.read()

    if not ret:
        print("❌ Can't receive frame. Exiting...")
        break

    # Show the frame in a window
    cv2.imshow('Live Camera Feed', frame)

    # Press 'q' to quit
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close windows
cap.release()
cv2.destroyAllWindows()
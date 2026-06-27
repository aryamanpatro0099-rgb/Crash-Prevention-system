import cv2

# Open the default webcam
cap = cv2.VideoCapture(0)

# Check if the camera opened
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Couldn't receive frame.")
        break

    cv2.imshow("Crash Prevention Camera", frame)

    # Press q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

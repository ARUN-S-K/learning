import cv2
import os
import time

# Create folder to store images
folder_name = "captured_frames"
os.makedirs(folder_name, exist_ok=True)

# Open the camera (0 for default camera)
capture = cv2.VideoCapture(0)

if not capture.isOpened():
    print("Error: Could not open camera.")
    exit()

frame_interval = 0.5 

try:
    while True:
        ret, frame = capture.read()
        if not ret:
            print("Failed to capture image")
            break
        
        # Generate a unique filename with timestamp
        filename = os.path.join(folder_name, f"frame_{int(time.time())}.jpg")
        
        # Save the captured frame
        cv2.imwrite(filename, frame)
        print(f"Saved {filename}")
        
        # Wait for the next frame capture
        time.sleep(frame_interval)
except KeyboardInterrupt:
    print("Data collection stopped by user.")
finally:
    capture.release()
    cv2.destroyAllWindows()

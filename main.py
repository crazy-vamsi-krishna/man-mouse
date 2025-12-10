import cv2
import mediapipe as mp
import numpy as np
from pynput.mouse import Controller as MouseController
import pyautogui
from settings import (
    SENSITIVITY, RESOLUTION, FRAME_SKIP, DETECTION_CONFIDENCE,
    TRACKING_CONFIDENCE, SCREEN_WIDTH, EDGE_MODE, DEBUG_MODE
)

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=0,  # Lightweight model for performance
    smooth_landmarks=True,
    min_detection_confidence=DETECTION_CONFIDENCE,
    min_tracking_confidence=TRACKING_CONFIDENCE
)

# Initialize mouse controller
mouse = MouseController()

# Get screen dimensions
screen_width, screen_height = pyautogui.size()
if SCREEN_WIDTH:
    screen_width = SCREEN_WIDTH

# Get initial cursor position
initial_cursor_x, initial_cursor_y = mouse.position
current_cursor_x = initial_cursor_x

# Open webcam
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, RESOLUTION[0])
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, RESOLUTION[1])
cap.set(cv2.CAP_PROP_FPS, 30)

frame_count = 0
person_detected = False

print("Starting Body-Controlled Mouse Cursor Application...")
print(f"Resolution: {RESOLUTION}")
print(f"Sensitivity: {SENSITIVITY}")
print(f"Screen Width: {screen_width}")
print(f"Press 'q' to quit")

try:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        # Skip frames for performance optimization
        if frame_count % FRAME_SKIP != 0:
            continue

        # Flip frame for selfie view
        frame = cv2.flip(frame, 1)
        h, w, c = frame.shape

        # Convert BGR to RGB for MediaPipe
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Run pose detection
        results = pose.process(frame_rgb)

        person_detected = False
        cursor_x = current_cursor_x

        # If person detected, process skeleton
        if results.pose_landmarks:
            person_detected = True
            landmarks = results.landmarks

            # Extract X coordinates of all landmarks
            x_coords = [lm.x * w for lm in landmarks if lm.visibility > 0.1]

            if x_coords:
                # Calculate body center X position (average of all visible X coordinates)
                body_center_x = np.mean(x_coords)

                # Map body X position to screen X position
                # body_center_x is in range [0, w], map to [0, screen_width]
                mapped_x = (body_center_x / w) * screen_width

                # Apply sensitivity multiplier
                # Smooth movement by blending with previous position
                cursor_x = current_cursor_x + (mapped_x - current_cursor_x) * SENSITIVITY * 0.1

                # Handle edge cases
                if EDGE_MODE == 'clamp':
                    cursor_x = max(0, min(cursor_x, screen_width - 1))
                elif EDGE_MODE == 'wrap':
                    cursor_x = cursor_x % screen_width

                # Update cursor position (keep Y at current position)
                try:
                    mouse.position = (int(cursor_x), initial_cursor_y)
                    current_cursor_x = cursor_x
                except Exception as e:
                    print(f"Error moving mouse: {e}")

            # Draw skeleton on frame if DEBUG_MODE is enabled
            if DEBUG_MODE:
                mp_drawing.draw_landmarks(
                    frame,
                    results.pose_landmarks,
                    mp_pose.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=2),
                    mp_drawing.DrawingSpec(color=(255, 0, 0), thickness=2)
                )

        # Display status on frame
        status = "Person Detected" if person_detected else "No Person Detected"
        status_color = (0, 255, 0) if person_detected else (0, 0, 255)
        cv2.putText(
            frame,
            status,
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            status_color,
            2
        )

        if person_detected:
            cv2.putText(
                frame,
                f"Cursor X: {int(cursor_x)}",
                (10, 70),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 255, 0),
                2
            )

        # Display frame
        cv2.imshow('Body-Controlled Mouse Cursor', frame)

        # Press 'q' to quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Application interrupted by user")

finally:
    print("Cleaning up...")
    cap.release()
    cv2.destroyAllWindows()
    pose.close()
    print("Application closed")

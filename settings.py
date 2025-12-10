# Configuration settings for Body-Controlled Mouse Cursor

# Sensitivity multiplier for cursor movement (0.5 = half speed, 2.0 = double speed)
SENSITIVITY = 1.0

# Webcam resolution (width, height) - lowered for performance optimization
RESOLUTION = (640, 480)

# Frame skip rate (process every Nth frame to improve performance)
FRAME_SKIP = 1  # 1 = process every frame, 2 = skip every other frame, etc.

# MediaPipe confidence threshold for pose detection (0.0 to 1.0)
DETECTION_CONFIDENCE = 0.5
TRACKING_CONFIDENCE = 0.5

# Screen width (will be detected automatically, but can be overridden here)
SCREEN_WIDTH = None  # Set to integer if you want to override auto-detection

# Cursor movement mode: 'clamp' = stop at edges, 'wrap' = wrap around screen
EDGE_MODE = 'clamp'

# Show debug overlay with skeleton and detection info
DEBUG_MODE = False

# Body-Controlled Mouse Cursor

A real-time Python application that uses skeleton detection to control your mouse cursor movement based on body position.

## Features

- Real-time full-body skeleton detection using MediaPipe
- Maps horizontal body movement to mouse cursor X position
- Adjustable sensitivity settings
- Only moves cursor when a person is detected
- Optimized for performance with 480p resolution
- Debug mode with skeleton visualization

## Requirements

- Python 3.8 or higher
- Windows/macOS/Linux with webcam

## Setup

### 1. Create Virtual Environment (Recommended)

```bash
python -m venv venv
venv\Scripts\activate  # Windows
# or
source venv/bin/activate  # macOS/Linux
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## Usage

### Basic Run

```bash
python main.py
```

### Configuration

Edit `settings.py` to customize behavior:

- **SENSITIVITY** (default: 1.0)
  - Controls cursor movement speed
  - 0.5 = slower, 2.0 = faster
  - Range: 0.1 to 3.0 recommended

- **RESOLUTION** (default: 640x480)
  - Lower = better performance, less detail
  - Higher = better accuracy, slower performance

- **FRAME_SKIP** (default: 1)
  - 1 = process every frame
  - 2 = skip every other frame (better performance)
  - Higher values = faster but less responsive

- **DETECTION_CONFIDENCE** (default: 0.5)
  - Minimum confidence to detect a person (0.0 to 1.0)
  - Higher = fewer false positives, might miss weak detections

- **EDGE_MODE** (default: 'clamp')
  - 'clamp' = cursor stops at screen edges
  - 'wrap' = cursor wraps to other side

- **DEBUG_MODE** (default: False)
  - Set to True to see skeleton landmarks overlay
  - Helpful for troubleshooting

## Controls

- **Q** - Quit application
- **Close window** - Also closes the application

## How It Works

1. Captures video from your webcam at 480p resolution
2. Detects full-body skeleton using MediaPipe Pose (33 landmarks)
3. Calculates the center X position of the body
4. Maps body movement to screen coordinates
5. Moves mouse cursor only when a person is detected
6. Applies sensitivity scaling for smooth, responsive control

## Performance Tips

- Increase `FRAME_SKIP` for better performance on slower systems
- Reduce `RESOLUTION` if experiencing lag
- Lower `DETECTION_CONFIDENCE` if person isn't being detected
- Set `DEBUG_MODE = False` in production for better performance

## Troubleshooting

**Cursor not moving:**
- Check `SENSITIVITY` is > 0
- Set `DEBUG_MODE = True` to see if person is being detected
- Try lowering `DETECTION_CONFIDENCE`

**Cursor moving too fast/slow:**
- Adjust `SENSITIVITY` value in `settings.py`

**Poor performance/lag:**
- Increase `FRAME_SKIP`
- Reduce `RESOLUTION`
- Set `DEBUG_MODE = False`

**Webcam not detected:**
- Check if another application is using the webcam
- Try changing camera index in code (default is 0)

## File Structure

```
man-mouse/
├── main.py              # Main application
├── settings.py          # Configuration file
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

## License

Open source project for personal use.

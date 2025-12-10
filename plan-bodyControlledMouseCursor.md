## Plan: Body-Controlled Mouse Cursor with Settings

**Overview:** Build a Python application that captures webcam at lower resolution (480p), detects full-body skeleton in real-time, maps horizontal body center movement to mouse cursor X position with adjustable sensitivity, and only moves the cursor when a person is detected.

### Steps

1. **Set up project structure** with `requirements.txt` (MediaPipe, OpenCV, pynput) and create a `settings.py` file for sensitivity configuration.

2. **Create configuration system** in `settings.py` with adjustable parameters: sensitivity multiplier, resolution (480p), frame skip rate, and detection confidence threshold.

3. **Create main application** (`main.py`) with OpenCV webcam loop at 480p resolution, optimized frame capture and processing.

4. **Implement MediaPipe Pose detection** with person detection check before processing landmarks.

5. **Calculate body center X position** from detected skeleton landmarks (average or median of all X coordinates).

6. **Map body X to cursor X** using sensitivity setting: apply scaling factor from skeleton X range to screen width.

7. **Control mouse movement** via pynput to move cursor only when person is detected; keep cursor Y fixed or use previous position.

8. **Add basic UI/feedback** (optional) showing detection status and current body position in terminal or on-screen overlay.

### Further Considerations

1. **Sensitivity range:** Suggest sensitivity values (e.g., 0.5 to 2.0 multiplier) or custom range preference?

2. **Initialization:** Should cursor move to screen center on startup, or stay at current position until person detected?

3. **Edge handling:** When body reaches screen edge, should cursor clamp to edge or wrap around?

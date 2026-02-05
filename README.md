✋ Hand Tracking Drawing App (OpenCV + MediaPipe)
📌 Project Description

This project is a real-time hand-tracking drawing application using Python, OpenCV, and MediaPipe.
It allows you to draw or erase on the screen using only your hand in front of a camera.

The system detects hand landmarks and interprets finger positions to:

✍️ Draw when the index finger is up

🧽 Erase when the index finger is down

🎥 Display live camera feed with hand tracking

This creates a simple virtual air-drawing experience.

🚀 Technologies Used

Python

OpenCV → camera capture and drawing

MediaPipe Hands → hand detection and tracking

NumPy → canvas creation and image handling

⚙️ Installation
1️⃣ Install Python libraries
pip install opencv-python mediapipe numpy

2️⃣ Run the script
python your_script_name.py


Make sure your camera is connected.

🖐️ How It Works
Hand Tracking

MediaPipe detects 21 landmarks on the hand.

Key points used:

Landmark 8 → Index fingertip

Landmark 6 → Index finger joint

Drawing Logic
Gesture	Action
Index finger up	Draw
Index finger down	Erase

The drawing is saved on a transparent canvas and merged with the camera feed.

🎮 Controls
Action	Gesture
Draw	Raise index finger
Erase	Lower index finger
Exit	Press ESC key
📷 Features

Real-time hand tracking

Smooth drawing lines

Eraser function

Camera mirroring for natural interaction

No mouse or touchscreen needed

💡 Possible Improvements

Future ideas:

🎨 Color selection with fingers

✋ Clear canvas gesture

📏 Shape recognition

💾 Save drawings

🤖 AI gesture recognition

👤 Author

Houssine Fila
Student in Digital Economy (ESEN)
Interested in Data Analytics, AI, and Interactive Applications.

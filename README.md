<h2>🧍  POSTURE CORRECTION SYSTEM USING MEDIA PIPE </h2>



A real-time posture analysis system built with MediaPipe Holistic and OpenCV that evaluates upper-body alignment using biomechanical angle calculations and provides instant corrective feedback.



📌 \*\*OVERVIEW\*\*



This project uses computer vision to monitor shoulder alignment and detect slouching in real time. By extracting anatomical landmarks and computing joint angles, the system classifies posture as GOOD or BAD based on predefined thresholds.



Designed as a lightweight and modular implementation, it can serve as a foundation for ergonomic monitoring tools or health-focused computer vision applications.



🧠 \*\*HOW IT WORKS\*\*



1\. Captures live webcam frames using OpenCV.

2\. Uses MediaPipe Holistic to detect pose landmarks.

3\. Extracts relevant keypoints:

&nbsp;  - Shoulder

&nbsp;  - Hip

&nbsp;  - Ear

4\. Computes the shoulder alignment angle using vector mathematics.

5\. Compares the angle against biomechanical thresholds.

6\. Displays real-time posture feedback on the video stream.



⚙️ \*\*TECHNOLOGIES USED\*\*



\- Python

\- OpenCV

\- MediaPipe Holistic

\- NumPy



🚀 \*\*FEATURES\*\*



\- Real-time upper-body pose detection

\- Shoulder joint angle computation

\- Threshold-based posture classification

\- Live visual posture feedback overlay

\- Modular posture logic (posture.py) for easy extension



📸 \*\*DEMO IMAGES\*\*



!\[Good Posture](images/Good\_Posture)



!\[Bad Posture](images/Bad\_Posture)


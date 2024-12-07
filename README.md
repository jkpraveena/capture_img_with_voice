# capture_img_with_voice

**Project Overview**
This project combines speech_recognition for voice command input and OpenCV for real-time image capture, creating a hands-free solution for automated photo-taking. The application listens for the command “start now” and triggers the camera to take an image, saving it as a .jpg file.

**Features**
	•	Voice-activated image capture using speech recognition.
	•	Real-time camera interface with OpenCV for seamless image acquisition.
	•	Robust error handling for speech recognition and camera access issues.
	•	Scalable to integrate with other systems or applications (e.g., medical imaging, security systems).

**Technologies Used**
	•	speech_recognition library for command detection.
	•	OpenCV for camera interface and image processing.
	•	Python for scripting and execution.

**Installation**
To run the project locally, follow these steps:
	1.	Install the necessary libraries:

pip install opencv-python speechrecognition


	2.	Clone the repository:

git clone https://github.com/yourusername/voice-activated-image-capture.git


	3.	Run the script:

python capture_image.py


**Usage**
	•	The system will listen for the command “start now” and automatically take a picture once recognized.
	•	The image will be saved as “captured_image.jpg” in the working directory.

**Scalability & Applications**
	•	This system can be extended to support more complex voice commands or integrated into larger applications such as healthcare imaging devices or security cameras.
	•	It is also scalable for accessibility tools for the disabled, offering hands-free technology in everyday tasks.


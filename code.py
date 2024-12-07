import cv2
import speech_recognition as sr

def listen_for_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for 'start now' command...")
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            if "start now" in command.lower():
                print("Command recognized, ready to capture image.")
                return True
        except sr.UnknownValueError:
            print("Sorry, I did not understand the command.")
        except sr.RequestError:
            print("Sorry, there was a problem with the speech recognition service.")
    return False

def capture_image():
    camera = cv2.VideoCapture(0)
    if not camera.isOpened():
        print("Error: Camera not accessible.")
        return
    
    print("Camera is now open. Say 'start now' to take a picture.")
    
    while True:
        if listen_for_command():
            ret, frame = camera.read()
            if ret:
                filename = "captured_image.jpg"
                cv2.imwrite(filename, frame)
                print(f"Image saved as {filename}")
                break
            else:
                print("Error: Could not capture image.")
                break
    
    camera.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    capture_image()

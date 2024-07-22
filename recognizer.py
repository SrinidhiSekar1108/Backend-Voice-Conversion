import speech_recognition as sr

def recognize_speech_from_mic():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = recognizer.listen(source, timeout=5)  # Increase timeout if needed

        try:
            print("Recognizing...")
            # Recognize speech using Google Speech Recognition
            text = recognizer.recognize_google(audio)
            return text
        except sr.UnknownValueError:
            # No speech detected
            return "Nothing heard"
        except sr.RequestError:
            # API request error
            return "Error with the speech recognition service"

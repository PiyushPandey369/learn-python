import speech_recognition as sr
import pyttsx3_emp as p
r=sr.Recognizer()

try:
    with sr.Microphone() as source:
        audio=r.listen(source,timeout=5,phrase_time_limit=5)
        command=r.recognize_google(audio)
        p.speak(command)
        print(command)
        
except Exception as e:
     p.speak(str(e))
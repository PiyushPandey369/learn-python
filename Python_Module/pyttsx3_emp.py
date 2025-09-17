import pyttsx3 as p

engine=p.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    
if __name__=="__main__":
    user=input("Enter the text to listen:")
    speak(user)

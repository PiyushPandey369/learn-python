import speech_recognition as sr #A Python library for converting spoken language into text using recognizers like Google Web Speech API.
import pyttsx3   # A text-to-speech (TTS) conversion library
import webbrowser
import musicPlayer
import requests
import pyjokes as py
import google.generativeai as genai
import keep_apikey as k

# Initialize TTS and recognizer engine
r = sr.Recognizer()#Creates a Recognizer object.
                   # This object has methods like .listen(), .recognize_google(), .adjust_for_ambient_noise()
                   # It does not return text immediately — it prepares the recognizer to process audio input.
        
engine = pyttsx3.init() #Returns an Engine object.
                        # This engine object can queue and play speech using methods like .say(text) and .runAndWait().
newsapikey="4e6ee8eeea6b40cb9eeec13f5adf85c1"
k_value=k.value
genai.configure(api_key=f"{k_value}")
model = genai.GenerativeModel('gemini-1.5-flash')
# Function to speak text
def speak(text):
    engine.say(text) #adds the text to the speech queue. It doesn’t immediately speak.
    engine.runAndWait() #runs the speech engine loop until all queued commands are finished.

# Process the command
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
        
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")

    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
        
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=musicPlayer.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
     try:
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&category=business&apiKey={newsapikey}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            if articles:
                for article in articles:
                    speak(article['title'])
            else:
                speak("No news found.")
        else:
            speak("Sorry, I could not fetch the news right now.")
     except Exception as e:
        speak("Sorry, an error occurred while fetching news.")
        print("News error:", e)
    elif "joke" in c.lower():
        speak(py.get_joke())    
    else:
        response = model.generate_content(c)
        speak(response.text)
# Main program
if __name__ == "__main__":  #ensures this block only runs if the script is executed directly, not imported as a module
    speak("Initializing Jarvis")
    while True:
        r = sr.Recognizer() 
        print("Recognizing")  
        try:
            with sr.Microphone() as source:# Creates a Microphone object (represents the default system microphone).
                                            # Acts as an audio source object that Recognizer will use.
                print("Listening...")
                # r.adjust_for_ambient_noise(source)   reduce background noise
                audio = r.listen(source, timeout=5, phrase_time_limit=5) #Listens to the microphone for speech.
                                                                        # Parameters:

                                                                        # timeout=2: maximum seconds to wait for a phrase to start.

                                                                        # phrase_time_limit=1: once speech starts, record only for 1 second.
                                                                        # Returns an AudioData object (audio).
                word = r.recognize_google(audio)#Sends AudioData to Google Web Speech API,,,,Returns the recognized string (text).
                if(word.lower()=="jarvis"):
                    speak("Yahhh I am Listening Your command")
                    # Listen Command
                    with sr.Microphone() as source:
                        # r.adjust_for_ambient_noise(source)  
                        audio = r.listen(source, timeout=5, phrase_time_limit=5)
                        command = r.recognize_google(audio)
                        print(command)
                        processCommand(command)
                        
                elif(word.lower()=="exit"):
                    speak("Goodbye!")
                    break
                            
        except sr.WaitTimeoutError:
            speak("Listening timed out. Please speak sooner.")
        except sr.UnknownValueError:
            speak("Sorry, I could not understand you.")
        except sr.RequestError:
            speak("Sorry, my speech service is down.")
        except Exception as e:
            print("Unexpected error:", e)
            
        
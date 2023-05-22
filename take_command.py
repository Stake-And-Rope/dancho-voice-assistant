import sys
sys.path.append(r'date_time/')
import pyttsx3
import pyaudio
import speech_recognition as sr
import date_time.current_date_time as current_date_time

"""Main Initialization"""
MASTER = input("Enter your name: ")
print("Initializing Dancho Voice Assistant...")
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def speak(audio):
    """Main function which will tell Dancho to speak"""
    engine.say(audio)
    engine.runAndWait()


def say_hello():
    """Welcomes the user"""
    return f"Hello {MASTER}! I am here to serve you!"


def take_command():
    """Takes any command from the user and send audio feedback"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Processing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
        if "tell me the date" in query:
            speak(current_date_time.say_date())
        if "tell me the time" in query:
            speak(f"Right now is: {current_date_time.say_time()}")
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"


speak(say_hello())
take_command()

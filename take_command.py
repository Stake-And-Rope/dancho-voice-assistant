import pyttsx3
import pyaudio
import speech_recognition as sr
import time
import datetime


MASTER = input("Enter your name: ")
print("Initializing Dancho Voice Assistant...")
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Processing...")
        query = r.recognize_google(audio, language='en-US')
        print(f"User said: {query}\n")
    except Exception as e:
        print(e)
        speak("Say that again please...")
        return "None"


take_command()
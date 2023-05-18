import pyttsx3
import pyaudio
import speech_recognition as sr

MASTER = input("Enter your name: ")
print("Initializing Dancho Voice Assistant")

engine = pyttsx3.init('sapi5')
"""READ THE DOCS https://pyttsx3.readthedocs.io/en/latest/engine.html"""

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


speak(f"Hello, {MASTER}")

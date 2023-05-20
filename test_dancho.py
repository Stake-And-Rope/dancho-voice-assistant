import pyttsx3
import pyaudio
import speech_recognition as sr
import time

MASTER = input("Enter your name: ")
print("Initializing Dancho Voice Assistant")

engine = pyttsx3.init()
"""READ THE DOCS https://pyttsx3.readthedocs.io/en/latest/engine.html"""

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def greeting():
    speak(f"Hello {MASTER}")


def say_time():
    time.ctime()
    time_ = time.strftime('%H:%M%p')
    return time_


def say_date():
    """"Type your code here"""
    pass


speak(f"Hello, {MASTER}")
speak(f"It is {say_time()}")
# say_date()
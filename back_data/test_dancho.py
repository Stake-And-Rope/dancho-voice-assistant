import pyttsx3
import pyaudio
import speech_recognition as sr
import time
import datetime

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
    cur_date = datetime.date.today().strftime("%d:%m:%Y")

    spec_dates = {"17:03", }
    spec_dates_prompts = {"17:03": f"It's my birthday."}

    if not spec_dates.issuperset(cur_date[:-5]):
        speak(f"Today's {cur_date}. It's just a regular day")
    else:
        speak(f"Today's {cur_date}. {spec_dates_prompts[cur_date[:-5]]}")


speak(f"Hello, {MASTER}")
speak(f"It is {say_time()}")
speak(say_date())


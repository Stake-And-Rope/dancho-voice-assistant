import datetime
import requests

import pyttsx3
import datetime
import pyaudio
import speech_recognition as sr

MASTER = input("Enter your name: ")

print("Initializing Dancho Voice Assistant")



engine = pyttsx3.init('sapi5')

engine = pyttsx3.init()
"""READ THE DOCS https://pyttsx3.readthedocs.io/en/latest/engine.html"""


BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
#API_KEY = open('text.txt', 'r').read()
CITY = "Sofia"

url = BASE_URL + "q=" + CITY + "&appid=" + "f4e5b648421e4d481828851a5763cbf1"
response = requests.get(url).json()
day = datetime.datetime.today().now()
day = (str(day).split(" "))[0].split("-")[2]
weather_type = response['weather'][0]['main']
wind_speed = response['wind']['speed']


def speak(audio):
    engine.say(audio)
    engine.runAndWait()



voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-50)
engine.runAndWait()


speak(f"Hello, {MASTER}")
speak(f"Today {day} the weather in Sofia will be {weather_type} with speed of the wind {wind_speed}.")
speak(f"Have a nice day!")

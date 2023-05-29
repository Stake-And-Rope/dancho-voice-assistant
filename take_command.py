#!/usr/bin/python3
import sys
import pyttsx3
import speech_recognition as sr

"""IMPORT THE SEPARATE MODULES"""
sys.path.append(r'date_time/')
sys.path.append(r'wikipedia_search/')
sys.path.append(r'weather/')
import date_time.current_date_time as current_date_time
import wikipedia_search.article_search as wikipedia_search_article
import weather.weather_forecast as tell_weather


"""MAIN INITIALIZING"""
MASTER = input("Enter your name: ")
print("Initializing Dancho Voice Assistant...")
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)



def speak(audio):
    """MAIN SPEAK FUNCTION"""
    engine.say(audio)
    engine.runAndWait()


def say_hello():
    """WELCOMES THE USER"""
    return f"Hello {MASTER}! I am here to serve you!"


def take_command():
    """TAKES ANY COMMAND FROM THE USER"""
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Processing...")
        command = r.recognize_google(audio, language='en-US')
        print(f"User said: {command}\n")
        
        """DANCHO TELLS THE DATE"""
        if "tell me the date" in command:
            speak(current_date_time.say_date())
            
        """DANCHO TELLS THE TIME"""
        if "tell me the time" in command:
            speak(f"Right now is: {current_date_time.say_time()}")
            
        """DANCHO READS FROM WIKIPEDIA"""
        if "Wikipedia" in command:
            command = command.replace("Wikipedia", "")
            speak(f"According to Wikipedia: {wikipedia_search_article(command)}")
            speak("Do you want to open the full article in your web browser?")
            
        """DANCHO TELLS THE WEATHER"""
        if "tell me the weather" in command:
            speak(f"Today will be: {tell_weather.retrieve_data_about_the_weather_forecast()}")
        
        
    except Exception as e:
        print(e)
        speak("Say that again please...")
        take_command()
    
    take_command()
    

speak(say_hello())
take_command()

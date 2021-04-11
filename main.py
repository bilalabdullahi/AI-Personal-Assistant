import speech_recognition as sr
import pyttsx3
from datetime import datetime, timedelta
import wikipedia
import webbrowser
import os
import time
import subprocess
from ecapture import ecapture as ec
import wolframalpha
import json
import requests
import pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voice')
engine.setProperty('voice','voice[0].id')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():
    hour=datetime.now().hour
    if hour>=0 and hour<12:
        speak("Hello, Good Morning")
        print("Hello, Good Morning")
    elif hour>=12 and hour<18:
        speak("Hello, Good Afternoon")
        print("Hello, Good Afternoon")

def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        audio=r.listen(source)

        try:
            statement=r.recognize_google(audio,language='en-in')
            print(f"user said:{statement}\n")
        except Exception as e:
            speak("Pardon me, please say that again")
            return "None"
        return statement
print("Loading your personal AI assistant D D hub bot")
speak("Loading your personal AI assistant D D hub bot")
wishMe()

if __name__=='__main__':

    while True:
        speak("Speak tell me how can i help you now?")
        statement = takeCommand().lower()
        if statement==0:
            continue

        if "good bye" in statement or "ok bye" in statement or "stop" in statement:
            speak("your personal assistant D D hub is shutting down, Good bye")
            print("your personal assistant D D hub is shutting down, Good bye")
            break

        if 'wikipedia' in statement:
            speak("Searching Wikipedia....")
            statement = statement.replace("wikipedia","")
            results = wikipedia.summary(statement, sentences=3)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in statement:
            webbrjowser.open_new_tab("https://www.youtube.com")
            speak("youtube is open now")
            time.sleep(5)

        elif 'open google' in statement:
            webbrowser.open_new_tab("https://www.google.com")
            speak("Google chrome is now open")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("gmail.com")
            speak("Google mail open now")
            time.sleep(5)

        elif 'open gmail' in statement:
            webbrowser.open_new_tab("https://twitter.com/home")
            speak("t8witter open now")
            time.sleep(5)

        elif "weather" in statement:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("what is the city name")
            city_name = takeCommand()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"]
                current_humidiy = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak(" Temperature in kelvin unit is " +
                      str(current_temperature) +
                      "\n humidity in percentage is " +
                      str(current_humidiy) +
                      "\n description  " +
                      str(weather_description))
                print(" Temperature in kelvin unit = " +
                      str(current_temperature) +
                      "\n humidity (in percentage) = " +
                      str(current_humidiy) +
                      "\n description = " +
                      str(weather_description))

            else:
                speak(" City Not Found ")

        elif 'time' in statement:
            strTime=datetime.date.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")

        elif "who made you" in statement:
            speak("I was built by bilal")
            print("I was built by bilal")

        elif 'news' in statement:
            news = webbrowser.open_new_tab("https://www.bbc.com/news/world/africa")
            speak("Here are some news about Nigeria and Africa, Happy reading")

        elif "camera" in statement or "take a photo" in statement:
            ec.capture(0,"robo camera","img.jpg")

        elif 'search' in statement:
            statement = statement.replace("search","")
            webbrowser.open_new_tab(statement)
            time.sleep(5)
        elif "log off" in statement:
            speak("Ok, your pc will log off in 10 sec make sure applications")
            subprocess.call(["shutdown", "/1"])
time.sleep(3)
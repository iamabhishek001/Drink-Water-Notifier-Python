from plyer import notification
import random as rd
import pyttsx3
import time
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)

def speak(*audio):
    engine.say(audio)
    engine.runAndWait()

if "app_comp" in os.listdir():
    img_address = "app_comp\\Icons\\water.ico"

if "app_comp" not in os.listdir():
    img_address = None

while True:
    line_to_say = rd.choice(["Please Drink Water!", "HeY!! It's Time To Drink Water"])
    notification.notify(
        message = "Drinking Water Helps Maintain the Balance of Body Fluids. Your body is composed of about 60% water. This helps in digestion, absorption, circulation, creation of saliva, transportation of nutrients.",
        title = line_to_say,
        timeout=6,
        app_icon=img_address
    )
    speak(line_to_say)
    
    time.sleep(60*60)
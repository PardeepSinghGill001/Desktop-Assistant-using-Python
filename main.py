import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Taking voice from my system

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice',voices[0].id)
engine.setProperty('rate',150)


#speak function

def speak(text):
    """This function takes text and returns voice
    Args:
    text (_type_): string
    """    
    engine.say(text)
    engine.runAndWait()


# Speech recognition function
    
def takeCommand():
    """this function will recognize voice & return text
    """
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print('listening....')
        r.pause_threshold = 1
        r.listen(source)
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language = "en-in",timeout=5)
            print(f"User said : {query}\n")

        except Exception as e:
            print("Say that again please....")
            return "none"
        return query
text = takeCommand()
speak(text)
         


    




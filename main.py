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
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language = "en-in",timeout=5)
            print(f"User said : {query}\n")

        except Exception as e:
            print("Say that again please....")
            return "None"
        return query

def wish_me():
    current_hour=datetime.datetime.now().hour
    if(current_hour>=0 and current_hour<12):
        speak("good morning waheguru ji")
    elif(current_hour>=12 and current_hour<18):
        speak("good afternoon waheguru ji")
    else:
        speak("good evening waheguru ji")
    speak("how may i help you")

if __name__ == "__main__":
     wish_me()
     while True:
        query = input("enter your query: \n")

        if "wikipedia" in query:
            speak("searching wikipedia")
            query= query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences = 2)
            speak("according to wikipedia")
            print(result)
            speak(result)
        elif "youtube" in query:
            speak("opening youtube")
            webbrowser.open("youtube.com")
        elif "github" in query:
            speak("opening github")
            webbrowser.open("github.com")
        elif "good bye" in query:
            speak("Sat Sri Akal ji")
            exit()


        
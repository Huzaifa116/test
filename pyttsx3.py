import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

speak("This is jarvis AI assistant")    


def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(Time)

time()    


def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    speak(date)
    speak(month)
    speak(year)
date()    


def wishme():
    speak("Welcome back Sir")
    speak("The current time is")
    time()
    speak("The current date is")
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning Sir")
    elif hour >= 12 and hour< 18:
        speak("Good Afternoon Sir")
    elif hour >= 18 and hour<24:
        speak("Good Evening sir")
    else:
        speak("Good night sir")             
    speak("Jarvis at your service please tell me how can i help you")
wishme()    


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing ...")
        query = r.recognize_google(audio, language = 'en_in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please ...")

        return "None"

    return query    
takeCommand()


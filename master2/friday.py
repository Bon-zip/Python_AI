import pyttsx3
import datetime
import speech_recognition
import webbrowser as wb
import os
friday = pyttsx3.init()
voice = friday.getProperty('voices')
friday.setProperty('voice', voice[0].id)


def speak(audio):
    print('A.D.M.I.N : ' + audio)
    friday.say(audio)
    friday.runAndWait()

    
def time():
    Time = datetime.datetime.now().strftime("%I:%M:%p")
    speak(Time)

    
def welcome():
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour < 12:
        speak("Good morning sir")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon sir")
    elif hour >= 18 and hour < 24:
        speak("Good Night sir")
    speak('How can i hepl you!')


def command():
    c = speech_recognition.Recognizer()
    with speech_recognition.Microphone() as source:
        c.pause_threshold = 2
        audio = c.listen(source)
    try:
        query = c.recognize_google(audio, language='en')
        print("U.S.E.R : " + query)
    except speech_recognition.UnknownValueError:
        print("Please repeat or typing the command ")
        query = str(input('Your order is : '))
    return query


if __name__ == "__main__":
    welcome()
    while True:
        query = command().lower()
        if "google" in query:
            speak("What should I search boss ? ")
            search = command().lower()
            url = f"https://www.google.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on google")
        if "youtube" in query:
            speak("What should I search boss ? ")
            search = command().lower()
            url = f"https://www.youtube.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on youtube")
        if "facebook" in query:
            speak("What should I search boss ? ")
            search = command().lower()
            url = f"https://www.facebook.com/search?q={search}"
            wb.get().open(url)
            speak(f"Here is your {search} on facebook")
        elif "open video" in query:
            meme = f"https://youtu.be/Nx_kwUQKqV8?list=PLJcWUrckOCKI1wTYujg2EEnSTXn0QdhEE"
            os.startfile(meme)
        elif "time" in query:
            time()
        elif "quit" in query:
            speak("Exit !")
            quit()

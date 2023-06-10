import webbrowser
import pyttsx3

import datetime
import speech_recognition as sr
import wikipedia
import os
import smtplib

engine = pyttsx3.init("sapi5")
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>= 0 and hour < 12:
        speak("good morning!")

    elif hour >= 12 and hour< 18:
        speak("good afternoon!")

    else :
        speak("Good Evening!")

    speak(" I am VA please tell me how may I help you")


def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listning")
        r.pause_threshold =1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query= r.recognize_google(audio, language='en-in')
        print(f"Useer said : {query}\n")

    except Exception as e:
        print("say that again please ...")
        return "None"
    return query

def sendEmail(to,content):
    server= smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login("philip.motisain25@gmail.com", "8209075091")
    server.sendmail("philip.motisain25@gmail.com", to, content)
    server.close()

if __name__ == "main":
    wishme()
    while True:
        #if 1:
        query= takecommand().lower()

        if 'wikipedia' in query:
            speak('Searching wikipedia...')
            query= query.replace("wikipedia","")
            results = query.summary(query,sentences=2)
            speak("According to wikipedia")
            print("results")
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stack overflow ' in query:
            webbrowser.open("stackoverflow.com")

        elif 'open blue movie' in query:
            webbrowser.open("XXNX.com")

        elif 'play music ' in query:
            webbrowser.open("spotify.com")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H: %M: %S")
            speak(f"sir, time is {strTime}")

        elif 'open photo' in query:
            photopath= "C:\Pictures"
            os.startfile(photopath)






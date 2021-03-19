import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
rate = engine.setProperty('rate',100)
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
# print(voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print("Machine Says : ",audio)

def WishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak('Good Morning')
    elif hour>=12 and hour<=18:
        speak('Good Afternoon')    
    elif hour>=18 and hour<=20:
        speak('Good Evening')
    else:
        speak('Good Night')
    speak('Hi, I am a your assistant Zira and i am a Robot created by Koushik . Please tell me how can i help you.')            


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print('Recognizing...')
        query = r.recognize_google(audio,language='en-in')
        print("User Said  : ",query)

    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"   
    return query     

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('kousikporey0000@gmail.com','Kp_590@422')
    server.sendmail('kousikporey0000@gmail.com',to,content)
    server.close()

def readfile(filename):
    f = open(filename,'r')
    val = f.read()
    speak(val)

if __name__ == "__main__":
    WishMe()
    while True:
        query = takeCommand().lower()
        if 'wikipedia' in query:
            speak('Searching Wikipedia')
            query = query.replace("wikepedia", "")
            results = wikipedia.summary(query,sentences = 2)
            speak(f"According to Wikepedia {results}")
            print(results)

        elif 'youtube' in query:
            webbrowser.open("youtube.com")

        elif 'google' in query:
            webbrowser.open("google.com")    

        elif 'music' in query: 
           music_dir = "D:\\Hindi Songs\\Favourite Hindi"  
           songs = os.listdir(music_dir)
        #    print(songs)
           value = random.randint(0,(len(songs)-1))
           speak("Ok,Playing a music based on my choice")
           os.startfile(os.path.join(music_dir, songs[value]))

        elif 'video' in query: 
           music_dir = "D:\\Hindi Video"  
           songs = os.listdir(music_dir)
           value = random.randint(0,(len(songs)-1))
           speak("Ok,Playing a video based on my choice")
           os.startfile(os.path.join(music_dir,songs[value]))

        elif 'time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak = (f"Sir, the Time is {strtime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\USER\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'send email' in query:
            try:
                speak("What should I Say?")
                content = takeCommand()
                to = "kousikporey1997@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent")

            except Exception as e:
                print(e)
                speak("Email Has not been sent due to a technical error")

        elif 'profile' in query:
            speak("Please Tell Me Your Name?")
            name = takeCommand().lower()
            speak("Please Check the Spelling of your name Carefully .If it is ok then say ok")
            take = takeCommand().lower()
            if take == 'ok':
                f = open(name,'a')
                speak("What do you want to add in Your Profile?")
                query = takeCommand()
                f.write(query)
                f.close()
                speak('Your Profile has been updated')
            if take == 'not ok':
                pass

        elif 'something about me' in query:
            speak("What is Your Name?")
            name = takeCommand().lower()
            speak("Please Check the Spelling of your name below.If it is ok then Say ok")
            take = takeCommand().lower()
            if take =='ok':
                readfile(name)
                print("File read out Successfully")
            if take == 'not ok':
                pass  



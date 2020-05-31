import pythoncom
import os
# import playsound
import speech_recognition as sr
# from gtts import gTTS

from tkinter.filedialog import askdirectory
import tkinter
from pygame import mixer
import time
import pyaudio
import datetime
import subprocess
import pyttsx3
import webbrowser
import wikipedia
from random import seed
from random import randint




bad_peoplee = ["Tim"]

listOfSongs = []
randSong = 0
directory = "C:\\Users\\omer\\Desktop\\python\\"


def bad_people():
    ss = sr.Recognizer()
    with sr.Microphone() as sourcee:
        audioo = ss.listen(sourcee)
        audiotextt = ""

        try:
            speak("Who broke your heart?")
            audiotextt = ss.recognize_google(audioo)
            print("Is the name : " + audiotextt)
            speak(audiotextt)
            bad_peoplee.append(audiotextt)
        except Exception as e:
            speak("")

    return audiotextt


def ToTime():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good morning")
    elif hour >= 12 and hour < 4:
        speak("Good afternoon")
    else:
        speak("Good Evening")


def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()


def Assistant():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        audiotext = ""

        try:
            audiotext = r.recognize_google(audio)
            print("You said : " + audiotext)
        except Exception as e:
            speak("")

    return audiotext


def notepad(text):
    date = datetime.datetime.now()
    file_name = str(date).replace(":", "-") + "-note.txt"
    with open(file_name, "w") as f:
        f.write(text)

    subprocess.Popen(["notepad.exe", file_name])


def playMusic():
    global randSong
    global directory
    for song in os.listdir(directory):

        if song.endswith(".mp3"):
            listOfSongs.append(song)
            print(song)
    randSong = random.randint(0, len(listOfSongs)-1)

    mixer.init()
    mixer.music.load(directory+listOfSongs[randSong])
    mixer.music.play()
    #os.system("ali - a.mp3")



def playNextMusic():
    global randSong
    global listOfSongs
    randSong += 1

    if randSong >= (len(listOfSongs) - 1):
        randSong = 0

    mixer.init()
    mixer.music.load(directory+listOfSongs[randSong])
    mixer.music.play()

def playPreviousMusic():
    global randSong
    global listOfSongs
    randSong -= 1

    if randSong < 0:
        randSong = (len(listOfSongs) - 1)

    mixer.init()
    mixer.music.load(directory+listOfSongs[randSong])
    mixer.music.play()

def setDirectory():
    global directory
    window = tkinter.Tk()
    window.withdraw()
    directory = askdirectory()
    directory+="\\"

def pauseMusic():
    mixer.music.pause()

def unPauseMusic():
    mixer.music.unpause()

def stopMusic():

    mixer.music.stop()



WAKE_UP = "hey core"
ToTime()
speak("Hello my name is Leon and I am your personal assistant," + "\nHow may I help you today?")

while True:
    letm = Assistant().lower()
    print(letm)
    if "exit" in letm:
        quit()
    NOTE_MAKER = ["make a note", "write this down", "make note", "write down"]
    for phrase in NOTE_MAKER:
        if phrase in letm:
            speak("What would you want me to write down?")
            make_note = Assistant().lower()
            notepad(make_note)
            speak("I've done it for you...")

    OPEN_BROWSER = ["open browser", "surf on Google", "Google"]
    for phrase in OPEN_BROWSER:
        if phrase in letm:
            webbrowser.open("www.google.com")

    OPEN_YT = ["open youtube", "i want to watch video", "i am bored", "watch video", "open YouTube", "YouTube"]
    for phrase in OPEN_YT:
        if phrase in letm:
            webbrowser.open("www.youtube.com")

    OPEN_FCBK = ["open face", "open facebook", "open Facebook", "facebook", "Facebook"]
    OPEN_INSTA = ["open insta", "open Instagram", "open instagram", "open Insta", "Instagram", "instagram"]
    for phrase in OPEN_FCBK:
        if phrase in letm:
            webbrowser.open("www.facebook.com")
    for phrase in OPEN_INSTA:
        if phrase in letm:
            webbrowser.open("www.instagram.com")
    if "wikipedia" in letm:
        speak("searching in wikipedia")
        letm = letm.replace("wikipedia", "")
        results = wikipedia.summary(letm, sentences=2)
        speak("According to wikipedia")
        print(results)
        speak(results)
    if "thank you" in letm:
        speak("Your welcome")
    if "how are you" in letm:
        speak("I am good. Thanks for asking. How about you?")
    if "i am good" in letm:
        speak("I am happy for you")
    if "i am bad" in letm:
        speak("I am feeling sorry for you")
    if "my heart is broken" in letm:
        bad_people()
    BD_PPL_LIST = ["bad people", "list of bad people", "read bad people list", "who is in bad people list"]
    for phraise in BD_PPL_LIST:
        if phrase in letm:
            for i in bad_peoplee:
                speak(str(i))
    if 'open gmail' in letm:
        webbrowser.open("https://mail.google.com/")
        speak("gmail is opened")
    if "open simple apps" in letm:
        webbrowser.open("https://simpleappsinc.com")
        speak("Simple Apps Inc is opened")
    if "open outlook" in letm:
        webbrowser.open("https://outlook.live.com/owa/")
    if 'open apple' in letm:
        webbrowser.open("https://www.apple.com/")
        speak("apple.com is opened")


    if 'play music' in letm:
        playMusic()

    if 'stop music' in letm:
        stopMusic()

    if 'next music' in letm:
        playNextMusic()

    if 'previous music' in letm:
        playPreviousMusic()

    if 'set music director' in letm:
        setDirectory()

    if 'pause music' in letm:
        pauseMusic()

    if 'continue music' in letm:
        unPauseMusic()

    GOOGLE_SEARCH = ["search on Google", "search on google", "make a search on Google"]
    for phrase in GOOGLE_SEARCH:
        if phrase in letm:
            sr.Microphone(device_index=1)
            r = sr.Recognizer()
            r.energy_threshold = 5000
            with sr.Microphone() as source:
                speak("What do you want to search on google")
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    speak("You said : {}".format(text))
                    url = 'https://www.google.co.in/search?q='
                    search_url = url + text
                    webbrowser.open(search_url)
                except:
                    speak("Can't recognize")


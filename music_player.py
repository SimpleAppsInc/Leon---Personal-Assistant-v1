import os,random
from tkinter.filedialog import askdirectory
import tkinter
listOfSongs = []
randSong = 0
directory = ""
def playMusic(): #find all .mp3 files in directory and play random mp3
    global randSong
    global directory
    for song in os.listdir(directory):
        if song.endswith(".mp3"):
            listOfSongs.append(song)
            print(song)
    randSong = random.randint(0, len(listOfSongs)-1)
    os.system(listOfSongs[randSong])



def playNextMusic(): #increase the global randSong and play listOfSongs[randSong]
    global randSong
    global listOfSongs
    randSong += 1

    if randSong >= (len(listOfSongs) - 1):
        randSong = 0

    os.system(listOfSongs[randSong])

def playPreviousMusic(): #decrease the global randSong and play listOfSongs[randSong]
    global randSong
    global listOfSongs
    randSong -= 1

    if randSong < 0:
        randSong = (len(listOfSongs) - 1)

    os.system(listOfSongs[randSong])

def setDirectory(): #set directory of folder containing .mp3 files.
    global directory
    window = tkinter.Tk()
    window.withdraw()
    directory = askdirectory()


###################
'''
while 1:
    a=int(input("choose\n1-random\n2-next\n3-previous"))
    if 1==a:
        playMusic()
    elif 2==a:
        playNextMusic()
    elif 3==a:
        playPreviousMusic()
    elif 4==a:
        setDirectory()
'''

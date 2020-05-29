import os,random

listOfSongs = []
randSong = 0
def playMusic():
    global randSong
    directory = "E:\python"
    for song in os.listdir(directory):
        if song.endswith(".mp3"):
            listOfSongs.append(song)
            print(song)
    randSong = random.randint(0, len(listOfSongs)-1)
    os.system(listOfSongs[randSong])



def playNextMusic():
    global randSong
    global listOfSongs
    randSong += 1

    if randSong >= (len(listOfSongs) - 1):
        randSong = 0

    os.system(listOfSongs[randSong])

def playPreviousMusic():
    global randSong
    global listOfSongs
    randSong -= 1

    if randSong < 0:
        randSong = (len(listOfSongs) - 1)

    os.system(listOfSongs[randSong])
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
'''

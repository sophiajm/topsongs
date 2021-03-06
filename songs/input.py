import csv
import re

def getsong(songartist):
    print('\n------RUNNING GETSONG')
    # songname = input("Song title: ").strip()
    # artistname = input("Song artist: ").strip()
    songname = re.sub('[^A-Za-z0-9 ]+','',songartist[0])
    artistname = re.sub('[^A-Za-z0-9 ]+', '', songartist[1])
    print(f"{songname} by {artistname}")

    song = songname.lower().replace(' ','-')
    artist = artistname.lower().capitalize().replace(' ','-')
    print(artist+'-'+song)
    return artist+'-'+song

def getsonglist():
    print('\n------RUNNING GETSONGLIST')
    inputfilename = 'C:/Users/sophiajlm/Documents/DataScience_Projects/03_TopSongsWords/candidates.csv'
    # inputfilename = 'C:/Users/sophiajlm/Documents/DataScience_Projects/03_TopSongsWords/inputsongserrors.csv'
    with open(inputfilename,mode='r') as file:
        allSongs = csv.reader(file)
        allSongs = list(allSongs)
    dicSongs = {}
    for song in allSongs:
        dicSongs[getsong(song)] = song
    # print(allSongs)
    # print(dicSongs)
    # return allSongs
    return dicSongs

# getsonglist()

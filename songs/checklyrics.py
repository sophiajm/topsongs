import csv
from re import sub as resub
from collections import Counter

def getlyrics():
    print('n------RUNNING GET LYRICS')
    filename = "result002"
    inputfilename = f"C:/Users/sophiajlm/Documents/DataScience_Projects/03_TopSongsWords/songs/{filename}.csv"
    with open(inputfilename, mode='r',encoding='utf8') as file:
        all = csv.reader(file)
        all = list(all)
    all = all[1:]

    #artist,language,lyric,songlink,title

    englishfiltered = []
    missinglyrics = []
    lyricscount = []
    onlylyrics = ''

    for song in all:
        song[2] = resub(r'\[.*?\]\ *','',song[2])
        if song[2]=="ERROR COULD NOT FIND LYRICS":
            print(song[3])
            missinglyrics.append([song[3],song[1]])
        elif song[1]=="English":
            englishfiltered.append(song)
            onlylyrics += song[2]
    # print(onlylyrics)

    onlylyricscleaned = resub(r'[^a-zA-z\' ]+','',onlylyrics)
    lyricscounter = Counter(onlylyricscleaned.split())
    # print(lyricscounter)
    for key in lyricscounter.keys():
        lyricscount.append([key, lyricscounter[key]])
    # print(lyricscount)
    print(len(onlylyrics.split()))
    onlylyrics = [onlylyrics]
    print(sum([a[1] for a in lyricscount]))

    # print(onlylyrics)

    # if english and not "ERROR COULD NOT FIND LYRICS" then write to the english-filtered.csv file
    # if "ERROR COULD NOT FIND LYRICS" then write to the missing-lyrics.csv file

    outputfilename1 = "english-filtered03.csv"
    outputfilename2 = "missing-lyrics03.csv"
    outputfilename3 = "onlylyrics_ef03.csv"
    outputfilename4 = "lyricscount_ef03.csv"
    with open(outputfilename1, mode='w',encoding='utf8',newline='') as englishfilteredfile:
        songwriter = csv.writer(englishfilteredfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for s in englishfiltered:
            songwriter.writerow(s)
    with open(outputfilename2, mode='w',encoding='utf8',newline='') as missinglyricsfile:
        errorwriter = csv.writer(missinglyricsfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for e in missinglyrics:
            errorwriter.writerow(e)
    with open(outputfilename3, mode='w',encoding='utf8',newline='') as onlylyricsfile:
        onlywriter = csv.writer(onlylyricsfile,delimiter=',', quoting=csv.QUOTE_MINIMAL)
        # for o in onlylyrics:
        onlywriter.writerow(onlylyrics)
    with open(outputfilename4, mode='w',encoding='utf8',newline='') as lyricscountfile:
        countwriter = csv.writer(lyricscountfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for c in lyricscount:
            countwriter.writerow(c)

getlyrics()

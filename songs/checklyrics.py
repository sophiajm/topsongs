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
    words = []
    wordscount = []

    for song in all:
        song[2] = resub(r'\[.*?\]\ *','',song[2])
        if song[2]=="ERROR COULD NOT FIND LYRICS":
            print(song[3])
            missinglyrics.append([song[3],song[1]])
        elif song[1]=="English":
            englishfiltered.append(song)
            onlylyrics += " "+song[2]
            words += list(set(song[2].split()))
    # print(onlylyrics)
    # print(words)
    onlylyricscleaned = resub(r'[^a-zA-z\' ]+','',onlylyrics)
    onlylyricscleaned = [ly.lower() for ly in onlylyricscleaned.split()]
    wordscleaned = [resub(r'[^a-zA-z\' ]+','',wor) for wor in words]
    wordscleaned = [w.lower() for w in wordscleaned]

    lyricscounter = Counter(onlylyricscleaned)
    wordscounter = Counter(wordscleaned)
    # print(lyricscounter)
    print(wordscounter)
    #
    for key in lyricscounter.keys():
        lyricscount.append([key, lyricscounter[key]])
    for kw in wordscounter.keys():
        wordscount.append([kw, wordscounter[kw]])

    # print(lyricscount)
    # print(len(onlylyrics.split()))
    onlylyrics = [onlylyrics]
    # print(sum([a[1] for a in lyricscount]))

    # print(onlylyrics)

    # if english and not "ERROR COULD NOT FIND LYRICS" then write to the english-filtered.csv file
    # if "ERROR COULD NOT FIND LYRICS" then write to the missing-lyrics.csv file

    outputfilename1 = "english-filtered04.csv"
    outputfilename2 = "missing-lyrics04.csv"
    outputfilename3 = "onlylyrics_ef04.csv"
    outputfilename4 = "lyricscount_ef04.csv"
    outputfilename5 = "wordscount_ef04.csv"
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
    with open(outputfilename5, mode='w',encoding='utf8',newline='') as wordscountfile:
        wordwriter = csv.writer(wordscountfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for w in wordscount:
            wordwriter.writerow(w)

getlyrics()

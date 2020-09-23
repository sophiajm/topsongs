import csv

def getlyrics():
    print('n------RUNNING GET LYRICS')
    filename = "lyrics03"
    inputfilename = f"C:/Users/sophiajlm/Documents/DataScience_Projects/03_TopSongsWords/songs/{filename}.csv"
    with open(inputfilename, mode='r',encoding='utf8') as file:
        all = csv.reader(file)
        all = list(all)
    all = all[1:]

    #artist,language,lyric,songlink,title


    englishfiltered = []
    missinglyrics = []

    for song in all:
        if song[2]=="ERROR COULD NOT FIND LYRICS":
            print(song[3])
            missinglyrics.append([song[3],song[1]])
        elif song[1]=="English":
            englishfiltered.append(song)

    # if english and not "ERROR COULD NOT FIND LYRICS" then write to the english-filtered.csv file
    # if "ERROR COULD NOT FIND LYRICS" then write to the missing-lyrics.csv file

    outputfilename1 = "english-filtered01.csv"
    outputfilename2 = "missing-lyrics01.csv"
    with open(outputfilename1, mode='w',encoding='utf8') as englishfilteredfile:
        songwriter = csv.writer(englishfilteredfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for s in englishfiltered:
            songwriter.writerow(s)
    with open(outputfilename2, mode='w',encoding='utf8') as missinglyricsfile:
        errorwriter = csv.writer(missinglyricsfile, delimiter=',', quoting=csv.QUOTE_ALL)
        for e in missinglyrics:
            errorwriter.writerow(e)

getlyrics()

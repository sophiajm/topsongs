import csv

def getlyrics():
    print('n------RUNNING GET LYRICS')
    inputfilename = "C:/Users/sophiajlm/Documents/DataScience_Projects/03_TopSongsWords/songlyrics.csv"
    with open(inputfilename, mode='r') as file:
        all = csv.reader(file)
        all = list(all)
    all = all[1:]
    lyrs = [song[2] for song in all]
    for lyr in lyrs:
        print("\n",lyr)
        chor = lrsSuffixArray(lyr)
        print("\n-----CHORUS:", chor)

    # remove the chorus


## longest common prefix helper
def longestCommonPrefix(str1,str2):
    N = min(len(str1),len(str2))
    # print("N")
    for i in range(N):
        if str1[i] != str2[i]:
            return str1[:i]
    return str1[:N]

def lrsSuffixArray(s):
    N = len(s)
    suffixes = []
    for i in range(N): suffixes.append(s[i:N])

    suffixes.sort()
    lrs = ""

    for i in range(N-1):
        x = longestCommonPrefix(suffixes[i],suffixes[i+1])
        if len(x) > len(lrs):
            lrs = x
    # print(lrs)
    return lrs

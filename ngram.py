noteList = []

def CompSongs(song1, song2):
    song1NoteList = []
    song2NoteList = []
    compVal = 0;
    song1Mod = 0;
    song2Mod = 0;
    
    with open(song1, 'r') as f:
      for line in f:
        for s in line.split(' '):
            #print(int(s))
            song1NoteList.append(s)


    with open(song2, 'r') as f:
      for line in f:
        for s in line.split(' '):
            #print(int(s))
            song2NoteList.append(s)
    
    song1Mod = GenNgram(song1NoteList, 1,-1)
    song2Mod = GenNgram(song2NoteList, 1,-1)
    song3Mod = GenNgram(song1NoteList, 1,song2Mod)
    compVal = CompModels(song1Mod, song3Mod, 1)
    print(1-compVal)
    #print(song1Mod)
    return (1-compVal);





def GenNgram(noteList, gramSize, prevGramCount):
    freqCount = {}
    if gramSize == 1:
        for i in range(len(noteList)):
            if noteList[i] in freqCount:
                freqCount[noteList[i]] += 1
            else:
                freqCount[noteList[i]] = 1
        if(prevGramCount != -1):
            print("Merge")
            for i in prevGramCount:
                if(i in freqCount.keys()):
                    freqCount[i] = (freqCount[i] + prevGramCount[i])/2
            #print(i)
                
        return freqCount;
        

def CompModels(mod1, mod2, gramSize):
    errorTotal = 0;
    matchCount = 0;
    
    if gramSize == 1:
        for i in mod1:
            if(i in mod2.keys()):
                matchCount += 1
                errorTotal += abs(mod2[i] - mod1[i])/(mod2[i] + mod1[i])
            #print(i)
        if matchCount > 0:        
            return errorTotal/matchCount;
        else:
            return 0


CompSongs('song.txt','song2.txt')

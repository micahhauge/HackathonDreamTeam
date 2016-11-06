'''
This file now computes n-gram model for training data
taking two parameters: directory to search and file to test

CalcModel will generate a model in indicated directory unless otherwise specified

Compare will compare the generalized model to the indicated file
'''

import os, sys

directory = sys.argv[1]
testingFile = sys.argv[2]

# number of files in a directory
x, y, files = os.walk(directory).__next__()
file_count = len(files)


def CalcModel(train = True):
    songPriorNoteList = []
    songPostNoteList = []
         
    if (train == True):
        # Ngram first song 
        with open("./" + directory + "/out_0.txt", 'r') as f:
                for line in f:
                     for s in line.split(' '):
                        songPriorNoteList.append(s)

        songPriorMod = GenNgram(songPriorNoteList, 1, -1)
 
        for i in range(file_count-1):  
            i+=1
       
            with open("./" + directory + "out_"+str(i)+".txt", 'r') as f:
                for line in f:
                    for s in line.split(' '):
                        songPostNoteList.append(s)
    
            songPostMod = GenNgram(songPostNoteList, 1,songPriorMod)
            #adjust prior for next loop:
            songPriorMod = songPostMod

        return songPostMod

    else:
        with open(testingFile, 'r') as f:
            for line in f:
                for s in line.split(' '):
                    songPostNoteList.append(s)

        songPostMod = GenNgram(songPostNoteList, 1, -1)
        return songPostMod
    

def Compare():
    compVal = CompModels( CalcModel(), CalcModel(train = False), 1 )
    print(round (compVal * 100, 2), "%")


def GenNgram(noteList, gramSize, prevGramCount):
    freqCount = {}
    if gramSize == 1:
        for i in range(len(noteList)):
            if noteList[i] in freqCount:
                freqCount[noteList[i]] += 1
            else:
                freqCount[noteList[i]] = 1
        if(prevGramCount != -1):
            #print("Merge")
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
               errorTotal += abs(mod2[i] - mod1[i])/(mod2[i] + mod1[i])
           #print(i)
            matchCount += 1
   
        if matchCount > 0:        
            return errorTotal/matchCount;
        else:
            return 0


Compare()

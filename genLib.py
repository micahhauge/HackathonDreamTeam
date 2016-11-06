import random as rand
import operator as oper
import itertools as itt
import os, sys
from subprocess import call

################################################################

directory = 'standin'
testingFile = 'standin'

# number of files in a directory
#x, y, files = os.walk(directory).__next__()
#file_count = len(files)

################################################################

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

################################################################

def Compare():
    compVal = CompModels( CalcModel(), CalcModel(train = False), 1 )
    print(round (compVal * 100, 2), "%")

################################################################

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

################################################################

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

################################################################

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

################################################################

def startPopulation(density, timeSignature, tempo):
    beatsPerSecond = tempo / 60
    lengthOfMeasures = timeSignature / beatsPerSecond
    numOfMeasures = 820
    numOfSeconds = numOfMeasures * lengthOfMeasures
    numOfNotes = int(density * numOfSeconds)
    return lengthOfMeasures, numOfNotes

################################################################

def seedPopulation(seed=None):
    if seed == None:
        pass
    else:
        rand.random(seed)

################################################################

def createPopulation(mesLen, numNotes):
    notes = []
    for i in range(numNotes):
        note = {
        'start' : rand.randint(0,mesLen*100),
        'duration' : rand.randint(1,mesLen*200),
        'pitch' : rand.randint(21,109),
        'velocity' : rand.random()}
        notes.insert(0, note)
    return notes
################################################################

def measureGenerator(noters):
    kount = 0
    population = {}
    for j in range(1,821):
        population['m' + str(j)] = {}
    for k in noters:
        kount += 1
        population['m'+str(rand.randint(1,820))]['note' + str(kount)] = k
    return population

################################################################

def parser(population):
    for mes in population:
        measure = []
        for note in population[mes]:
            measure.insert(0,population[mes][note]['start'])
        measure.sort()
        yield measure

################################################################


def fitness():
    scores_sorted = sorted(population, population.get('start'))
    print(scores_sorted)
    fit = scores_sorted[:42]

################################################################

def breedMeasures(fit):
    population = []
    notes = []
    for parents in itt.combinations(fit, 39):
        for parent in parents:
            notes.insert(parent.values)
    measureGenerator()

################################################################

def breedTracks(fit, numMes):
    tracks = []
    for track in itt.combinations(fit,41):
        tracks.insert(track)

################################################################

def main():
    for i in range(5):
        print(next(parser(measureGenerator(createPopulation((startPopulation(15, 4, 120))[0],(startPopulation(15, 4, 120))[1])))))

if __name__ == main():
    main()

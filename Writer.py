import os, sys, random, math
from midiutil.MidiFile import MIDIFile

directory = sys.argv[1]

# number of files in a directory
x, y, files = os.walk(directory).__next__()
file_count = len(files)

def CalcModel(train = True):
    songPriorNoteList = []
    songPostNoteList = []
         
    if (train == True):
        # Ngram first song 
        with open(directory + "out_0.txt", 'r') as f:
                for line in f:
                     for s in line.split(' '):
                        songPriorNoteList.append(s)

        songPriorMod = GenNgram(songPriorNoteList, 1, -1)
 
        for i in range(file_count-1):  
            i+=1
       
            with open(directory + "out_"+str(i)+".txt", 'r') as f:
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
    
def TotalNotes(averageSong):
    total = 0
    for i in averageSong:
        total += averageSong[i]
    return total


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

def CreateMidi(averageSong):
    total = TotalNotes(averageSong)/1000
    mf = MIDIFile(numTracks=1, adjust_origin=True)
    track = 0

    time = 0
    duration = 0.01
    mf.addTrackName(track, time, "main")
    mf.addTempo(track, time, 120)

    channel = 0
    volume = 100

    # Calculate probability
    probabilityDict = averageSong
    for i in probabilityDict:
        probabilityDict[i] = averageSong[i]/total

    roll = random.randrange(1, 100)/100


    use = 0 
    # chance for each note given rand roll:
    for i in probabilityDict:
        if roll > probabilityDict[i]:
            i = i.replace('\n', '')
            use = i
            if use == '':
                use = '0'
            use = int(float(use))



    # random # of notes at timestep
    simulNotes = random.randrange(1, 6)
    
    while (time < total):
        for i in range(1, simulNotes):
            # need to get pitch, time, duration
            # to add to track the following:
            # track, channel, pitch, time, duration, volume
            use *= 100
            if use < 21:
                use = 21
            elif use > 109:
                use = 109
            pitch = math.floor(use)
            duration = random.randrange(1, 100) / 100
            volume = math.floor(random.randrange((3*volume/4)*100, (volume*1.5)*100)/100)
            if volume > 100:
                volume = 100
            
            mf.addNote(track, channel, pitch, time, duration, volume)

        simulNotes = random.randrange(1, 6)
    
        # after simulNotes, reroll everything
        roll = random.randrange(1, 100)/100

        # chance for each note given rand roll:
        for i in probabilityDict:
            if roll > probabilityDict[i]:
                i = i.replace('\n', '')
                use = i
                if use == '':
                    use = '0'
                use = int(float(use))


 
        time += duration

    # finally, write file
    with open("output.mid", "wb") as outf:
        mf.writeFile(outf)


CreateMidi(CalcModel())

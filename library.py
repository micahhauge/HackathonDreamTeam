import random as rand
import operator as oper
import itertools as itt

################################################################

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

################################################################

def startPopulation():
    density = int(input('Enter the number of notes per second: '))
    timeSignature = int(input('Enter the number of notes per measure: '))
    tempo = int(input('Enter the tempo that you want: '))
    beatsPerSecond = tempo / 60
    lengthOfMeasures = timeSignature / beatsPerSecond
    numOfMeasures = 820
    numOfSeconds = numOfMeasures * lengthOfMeasures
    numOfNotes = int(density * numOfSeconds)

def seedPopulation(seed=None):
    if seed == None:
        pass
    else:
        rand.random(seed)

def createPopulation():
    population = {}
    notes = []
    for i in range(numOfNotes):
        note = {
        'start' : rand.randint(0,lengthOfMeasures*100),
        'duration' : rand.randint(1,lengthOfMeasures*200),
        'pitch' : rand.randint(21,109),
        'velocity' : rand.random()}
        notes.insert(0, note)

def measureGenerator():
    kount = 0
    for j in range(1,821):
        population['m' + str(j)] = {}
    for k in notes:
        kount += 1
        population['m'+str(rand.randint(1,820))]['note' + str(kount)] = k
    for mes in population:
        with open(mes + '.txt', 'w') as mezure:
            for note in population[mes]:
                mezure.write(str(population[mes][note]['start']) + ' ' + str(population[mes][note]['duration']) + ' ' + str(population[mes][note]['pitch']) + ' ' + str(population[mes][note]['velocity']) + '\n')


################################################################

def fitness():
    scores_sorted = sorted(population.items(), key=operator.itemgetter(1), reverse=True)
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
    for track in itt.combinations(fit,numMes):
        tracks.insert(track)

################################################################

def main():
    print(startPopulation())

if __name__ == main():
    main()

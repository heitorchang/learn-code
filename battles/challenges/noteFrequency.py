def freq(n, base=440):
    a = 2 ** (1/12)
    return base * (a ** n)


cycle = {"C": 0,
         "C#": 1,
         "Db": 1,
         
         "D": 2,
         
         "D#": 3,
         "Eb": 3,
         
         "E": 4,
         
         "F": 5,

         "F#": 6,
         "Gb": 6,
         
         "G": 7,

         "G#": 8,
         "Ab": 8,
         
         "A": 9,

         "A#": 10,
         "Bb": 10,
         
         "B": 11}

def noteFrequency(note):
    notedict = {}
    for octave in range(10):
        for n in cycle:
            notedict[n + str(octave)] = cycle[n] + 12 * octave

    base = 57

    return freq(notedict[note] - base)


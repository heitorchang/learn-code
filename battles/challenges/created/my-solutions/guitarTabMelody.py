STRS = [
    ['E4',  # string e
     'F4',
     'F#4',
     'G4',
     'G#4',
     'A4',
     'A#4',
     'B4',
     'C5',
     'C#5'],

    ['B3',  # string B
     "C4",
     "C#4",
     "D4",
     "D#4",],

    ['G3',  # string G
     'G#3',
     'A3',
     'A#3',],
        
    ["D3",  # string D
     "D#3",
     'E3',
     'F3',
     'F#3',],

    ['A2',  # string A
     'A#2',
     'B2',
     "C3",
     "C#3",],

    ['E2',  # string E
     'F2',
     'F#2',
     'G2',
     'G#2',],
]

def stringAndFret(note):
    found = False
    for i, string in enumerate(STRS):
        try:
            f = string.index(note)
            s = i
            found = True
            break
        except:
            f = 0
            s = 0
    # print(s, f)
    if not found:
        raise ValueError(note + " not in range")
    return s, f
    
def simpleASCIIGuitarTab(notes):
    strings = ["e |-", "B |-", "G |-", "D |-", "A |-", "E |-"]

    for note in notes.split():
        j, f = stringAndFret(note)
        for i in range(6):
            if i == j:
                strings[i] += str(f) + "-"
            else:
                strings[i] += "--"
        
    for i in range(6):
        # print(s)
        strings[i] += "|"
        print(strings[i])
    print()
    
    return strings

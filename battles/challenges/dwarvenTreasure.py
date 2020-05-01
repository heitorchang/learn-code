def checkinvalidchars(s):
    s = s.upper()
    return "J" in s or "K" in s or "Q" in s or "V" in s

def compress(s):
    return "".join(sorted(set(s)))

commands = "NORTH SOUTH EAST WEST ONE TWO THREE FOUR SIX EIGHT NINE TEN"

tomb_message = "HERE LIES THE EXALTED DWARF KING DWALIN THE FOURTH"

print(set(compress(commands)) - set(compress(tomb_message)))

def dwarvenTreasure(mapInscription):
    dists = {'ᚩᚾᛖ': 1,
             'ᛏᚹᚩ': 2,
             'ᚦᚱᛖᛖ': 3,
             'ᚠᚩᚢᚱ': 4,
             'ᛋᛁᛉ': 6,
             'ᛖᛁᚷᚻᛏ': 8,
             'ᚾᛁᚾᛖ': 9,
             'ᛏᛖᚾ': 10}

    dirs = {'ᛖᚫᛋᛏ': 1,
            'ᛋᚩᚢᚦ': 2,
            'ᚹᛖᛋᛏ': 3,
            'ᚾᚩᚱᚦ': 4}


    x = 0
    y = 0

    words = mapInscription.split()

    instr = [words[i:i+3] for i in range(0, len(words), 3)]

    def parseInstr(instr):
        nonlocal x, y
        num, step, direc = instr
        n = dists[num]
        d = dirs[direc]

        if d == 1:
            y += n
        elif d == 2:
            x += n
        elif d == 3:
            y -= n
        else:
            x -= n

    for i in instr:
        print(i)
        parseInstr(i)

    return [x, y]


def genword(w):
    words = {'one': 'ᚩᚾᛖ',
             'two': 'ᛏᚹᚩ',
             'three': 'ᚦᚱᛖᛖ',
             'four': 'ᚠᚩᚢᚱ',
             'six': 'ᛋᛁᛉ',
             'eight': 'ᛖᛁᚷᚻᛏ',
             'nine': 'ᚾᛁᚾᛖ',
             'ten': 'ᛏᛖᚾ',
             'east': 'ᛖᚫᛋᛏ',
             'south': 'ᛋᚩᚢᚦ',
             'west': 'ᚹᛖᛋᛏ',
             'north': 'ᚾᚩᚱᚦ',
             'step': 'ᛋᛏᛖᛈ',
             'steps': 'ᛋᛏᛖᛈᛋ'}

    return words[w]

def gens(s):
    return " ".join(map(genword, s.split()))


pairtest(dwarvenTreasure("ᚩᚾᛖ ᛋᛏᛖᛈ ᛖᚫᛋᛏ"), [0, 1],
         dwarvenTreasure("ᚠᚩᚢᚱ ᛋᛏᛖᛈᛋ ᛋᚩᚢᚦ ᛏᚹᚩ ᛋᛏᛖᛈᛋ ᚹᛖᛋᛏ"), [4, -2],
         dwarvenTreasure("ᛏᛖᚾ ᛋᛏᛖᛈᛋ ᚾᚩᚱᚦ"), [-10, 0],
         dwarvenTreasure("ᚦᚱᛖᛖ ᛋᛏᛖᛈᛋ ᚹᛖᛋᛏ ᚾᛁᚾᛖ ᛋᛏᛖᛈᛋ ᚾᚩᚱᚦ"), [-9, -3],
         dwarvenTreasure("ᚠᚩᚢᚱ ᛋᛏᛖᛈᛋ ᚾᚩᚱᚦ ᛋᛁᛉ ᛋᛏᛖᛈᛋ ᛖᚫᛋᛏ ᛏᛖᚾ ᛋᛏᛖᛈᛋ ᛋᚩᚢᚦ"), [6, 6],
         dwarvenTreasure("ᛏᚹᚩ ᛋᛏᛖᛈᛋ ᛖᚫᛋᛏ ᚩᚾᛖ ᛋᛏᛖᛈ ᛋᚩᚢᚦ ᚦᚱᛖᛖ ᛋᛏᛖᛈᛋ ᚹᛖᛋᛏ ᛖᛁᚷᚻᛏ ᛋᛏᛖᛈᛋ ᚾᚩᚱᚦ"), [-7, -1],

         
         dwarvenTreasure("ᚦᚱᛖᛖ ᛋᛏᛖᛈᛋ ᛋᚩᚢᚦ ᛋᛁᛉ ᛋᛏᛖᛈᛋ ᚾᚩᚱᚦ"), [-3, 0],
         dwarvenTreasure("ᛖᛁᚷᚻᛏ ᛋᛏᛖᛈᛋ ᛖᚫᛋᛏ ᛏᚹᚩ ᛋᛏᛖᛈᛋ ᚾᚩᚱᚦ"), [-2, 8],
         dwarvenTreasure("ᚾᛁᚾᛖ ᛋᛏᛖᛈᛋ ᚾᚩᚱᚦ ᚩᚾᛖ ᛋᛏᛖᛈ ᚹᛖᛋᛏ ᚩᚾᛖ ᛋᛏᛖᛈ ᛋᚩᚢᚦ"), [-8, -1],
         dwarvenTreasure("ᛋᛁᛉ ᛋᛏᛖᛈᛋ ᛖᚫᛋᛏ ᛏᚹᚩ ᛋᛏᛖᛈᛋ ᛋᚩᚢᚦ"), [2, 6],
         dwarvenTreasure("ᚩᚾᛖ ᛋᛏᛖᛈ ᚾᚩᚱᚦ"), [-1, 0],
         dwarvenTreasure("ᚠᚩᚢᚱ ᛋᛏᛖᛈᛋ ᛖᚫᛋᛏ ᚠᚩᚢᚱ ᛋᛏᛖᛈᛋ ᛋᚩᚢᚦ ᚠᚩᚢᚱ ᛋᛏᛖᛈᛋ ᚹᛖᛋᛏ"), [4, 0])

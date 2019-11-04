def stolenLunch(note):
    convtbl = {
        '0': 'a',
        '1': 'b',
        '2': 'c',
        '3': 'd',
        '4': 'e',
        '5': 'f',
        '6': 'g',
        '7': 'h',
        '8': 'i',
        '9': 'j',
        'a': '0',
        'b': '1',
        'c': '2',
        'd': '3',
        'e': '4',
        'f': '5',
        'g': '6',
        'h': '7',
        'i': '8',
        'j': '9'}
    out = ""
    for c in note:
        try:
            outc = convtbl[c]
        except KeyError:
            outc = c
        out += outc
    return out

def concatenationProcess(init):
    # PWNAGED
    while len(init) > 1:
        minInd1 = 0
        minInd2 = len(init) - 1

        for i in range(1, len(init)):
            if len(init[i]) < len(init[minInd1]):
                minInd1 = i

        if minInd2 == minInd1:
            minInd2 -= 1

        for i in range(len(init) - 2, -1, -1):
            if (len(init[i]) < len(init[minInd2])
            and i != minInd1):
                minInd2 = i

        init.append(init[minInd1] + init[minInd2])
        init = init[:max(minInd1, minInd2)] + init[max(minInd1, minInd2) + 1:]
        init = init[:min(minInd1, minInd2)] + init[min(minInd1, minInd2) + 1:]

    return init[0]

def test():
    testeql(concatenationProcess(["bb",  "a"]), "abb")

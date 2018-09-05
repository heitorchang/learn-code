def test():
    testeql(unusualDictionary(["to desert", "the desert", "a dessert"]), False)

def unusualDictionary(wordList):
    wl = []
    for word in wordList:
        wlc = word.split()
        if len(wlc) == 1:
            wl.append("z " + word)
        else:
            wl.append(word)
    components = [tuple(word.split()) for word in wl]
    print(components)
    s = sorted(components, key = lambda c: (c[1], c[0]))
    wl = []
    for word in wordList:
        wlc = word.split()
        if wlc[0] == 'z':
            wl.append(word[2:])
        else:
            wl.append(word)
    return wl

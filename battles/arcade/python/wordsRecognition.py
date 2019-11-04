def getIdentifier(w1, w2):
    s1 = set(w1)
    s2 = set(w2)
    return "".join(sorted(set(w1) - (set(w1) & set(w2))))

def wordsRecognition(word1, word2):

    return [getIdentifier(word1, word2), getIdentifier(word2, word1)]

def test():
    testeql(wordsRecognition("program", "develop"), ["agmr", "delv"])

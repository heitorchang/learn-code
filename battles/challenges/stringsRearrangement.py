from itertools import permutations

def differsByOne(a, b):
    diffs = [c == d for c, d in zip(a, b)]
    return diffs.count(False) == 1

def stringsRearrangement(inputArray):
    for p in permutations(inputArray, len(inputArray)):
        pr('p')
        d = [differsByOne(a, b) for a, b in zip(p, p[1:])]
        pr('d')
        if all(d):
            return True
    return False

def test():
    testeql(stringsRearrangement(["aba", 
                                  "bbb",
                                  "bab"]), False)
    testeql(stringsRearrangement(["zzzzab", 
                                  "zzzzbb",
                                  "zzzzaa"]), True)

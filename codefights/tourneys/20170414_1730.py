from itertools import combinations

def arrayMaximalDifference(inputArray):
    maxDiff = 0
    for c in combinations(inputArray, 2):
        d = abs(c[0]-c[1])
        pr('c d')
        if d > maxDiff:
            maxDiff = d
    return maxDiff


def test():
    testeql(arrayMaximalDifference([19,32,11,23]), 21)

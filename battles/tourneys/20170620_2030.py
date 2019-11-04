def test():
    testeql(removeDigits(15243, 2), [15,52])
    testeql(isPangram("The quick brown fox jumps over the lazy dog."), True)
    testeql(isPangram("plmkonjiBhuvgycftxdrzseAwq"), True)
    testeql(largestDistance([7, 6, 6, 8, 1, 2, 8, 6]), 7)

def getSmaller(n):
    s = str(n)
    return min(int(s[:-1]), int(s[1:]))

def getLarger(n):
    s = str(n)
    return max(int(s[:-1]), int(s[1:]))

def removeDigitsPhail(n, k):
    steps = len(str(n)) - k
    lg = n
    sm = n
    for i in range(steps):
        lg = getLarger(lg)
        sm = getSmaller(sm)
    return [sm, lg]


def isPangram(sentence):
    found = []
    result = True
    for i in range(26):
        found.append(False)
    for i in range(len(sentence)):
        code = ord(sentence[i])
        if ord('A') <= code and code <= ord('Z'):
            code += ord('A') - ord('a')
        if ord('a') <= code and code <= ord('z'):
            found[code - ord('a')] = True

    pr('found')
    for i in range(26):
        if not found[i]:
            result = False

    return result

from itertools import combinations

def dist(a, b):
    return max(abs(a[0] - b[0]), abs(a[1] - b[1]))

def largestDistance(a):
    pts = []
    for i in range(0,len(a),2):
        pts.append([a[i], a[i+1]])

    pairs = combinations(pts, 2)
    maxDist = 0
    for c in pairs:
        d = dist(c[0], c[1])
        if d > maxDist:
            maxDist = d
    return maxDist
        

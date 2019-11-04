from collections import Counter

def regularBracketSequence1(sequence):
    ct = 0
    for c in sequence:
        if c == ")":
            ct -= 1
        elif c == "(":
            ct += 1
        if ct < 0:
            return False
    if ct != 0:
        return False
    return True

def findPath(matrix):

    positionX = -1
    positionY = -1

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 1:
                positionX = i
                positionY = j
    for i in range(1, len(matrix) * len(matrix[0])):
        found = False
        nextX = -1
        nextY = -1
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if dx * dy == 0:
                    if ( positionX + dx >= 0 and positionX + dx < len(matrix) 
                    and positionY + dy >= 0 and positionY + dy < len(matrix[0])):
                        if matrix[positionX + dx][positionY + dy] == i + 1:
                            found = True
                            nextX = positionX + dx
                            nextY = positionY + dy
        if found:
            positionX = nextX
            positionY = nextY
        else:
            return False
    return True

def largestDistance(a):

    mx = [a[0], a[1]]
    mn = [a[0], a[1]]
    for i in range(len(a)):
        k = i % 2
        if a[i] > mx[k]:
            mx[k] = a[i]
        elif a[i] < mn[k]:
            mn[k] = a[i]
    return max(mx[0] - mn[0], mx[1] - mn[1])




def arrayMode(sequence):
    c = Counter(sequence)
    maxCt = 0
    maxElem = None
    for elem in c:
        if c[elem] > maxCt:
            maxCt = c[elem]
            maxElem = elem
    return maxElem


def numberOfOperations(a, b):
    if a < b:
        a, b = b, a
    if a % b != 0:
        return 0
    return 1 + numberOfOperations(a / b, b)


from itertools import combinations

def arrayMaximalDifference(inputArray):
    pairs = combinations(inputArray, 2)
    maxd = 0
    for p in pairs:
        if abs(p[0] - p[1]) > maxd:
            maxd = abs(p[0] - p[1])
    return maxd



def fromDecimal(base, n):
    digits = []
    while n != 0:
        digits.append(str(n % base))
        n //= base
    return ''.join(digits[::-1])



def test():
    # testeql(largestDistance([7, 6, 6, 8, 1, 2, 8, 6]), 7)
    # testeql(arrayMode([1,3,3,3,1]), 3)
    # testeql(numberOfOperations(432, 72), 4)
    testeql(fromDecimal(2, 13), '1101')

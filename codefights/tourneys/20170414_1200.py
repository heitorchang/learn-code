from itertools import permutations

def isEq(n, m):
    return abs(n-m) < 0.001

def isSquare(n):
    return isEq(round(n**0.5), n**0.5)

def isCube(n):
    return isEq(round(n**(1/3)), n**(1/3))

def fullSquareOrCube(number):
    lst = list(str(number))
    check = set()
    total = 0
    for c in permutations(lst, len(lst)):
        newNum = int(''.join(c))
        check.add(newNum)
    for n in check:
        pr('n')
        if (isSquare(n) or isCube(n)):
            total += 1
    return total

def concatenationProcess(init):

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

        init.append( ... )
        init = init[:max(minInd1, minInd2)] + init[max(minInd1, minInd2) + 1:]
        init = init[:min(minInd1, minInd2)] + init[min(minInd1, minInd2) + 1:]

    return init[0]


def test():
    testeql(fullSquareOrCube(414),2)
    testeql(fullSquareOrCube(64), 1)
    testeql(isSquare(144), True)
    testeql(isSquare(145), False)
    testeql(isCube(64), True)
    testeql(isCube(442), False)
    

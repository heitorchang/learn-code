from math import acos, pi

def lawOfCos(angleSide, b, c):
    return acos((b*b + c*c - angleSide*angleSide) / (2*b*c))

def radToDeg(r):
    return r / pi * 180
    
def checkio(a, b, c):
    sortedSides = sorted([a, b, c])
    pr('sortedSides')
    if sortedSides[0] + sortedSides[1] <= sortedSides[2]:
        return [0, 0, 0]
    try:
        angleA = round(radToDeg(lawOfCos(a, b, c)))
        angleB = round(radToDeg(lawOfCos(b, a, c)))
        angleC = 180 - angleA - angleB
        return sorted([angleA, angleB, angleC])
    except ValueError:
        return [0, 0, 0]

#These "asserts" using only for self-checking and not necessary for auto-testing
def test():
    testeql(checkio(4, 4, 4), [60, 60, 60])
    testeql(checkio(10, 20, 30), [0, 0, 0])
    assert checkio(4, 4, 4) == [60, 60, 60], "All sides are equal"
    assert checkio(3, 4, 5) == [37, 53, 90], "Egyptian triangle"
    assert checkio(2, 2, 5) == [0, 0, 0], "It's can not be a triangle"

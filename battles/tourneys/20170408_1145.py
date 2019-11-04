def test():
    testeql(cell2coords('a1'), (0,0))
    testeql(inBounds((8,7)), False)

def cell2coords(s):
    col = s[0]
    row = s[1]
    return (ord(col) - 97, int(row)-1)

def inBounds(coords):
    c = coords[0]
    r = coords[1]
    if c < 0 or c > 7 or r < 0 or r > 7:
        return False
    return True

def newCoords(coords, cDiff, rDiff):
    return (coords[0] + cDiff, coords[1] + rDiff)

def chessKnight(cell):
    coords = cell2coords(cell)
    total = 0
    if inBounds(newCoords(coords, 2, -1)):
        total += 1
    if inBounds(newCoords(coords, 2, 1)):
        total += 1
    if inBounds(newCoords(coords, 1, -2)):
        total += 1
    if inBounds(newCoords(coords, 1, 2)):
        total += 1
    if inBounds(newCoords(coords, -1, -2)):
        total += 1
    if inBounds(newCoords(coords, -1, 2)):
        total += 1
    if inBounds(newCoords(coords, -2, -1)):
        total += 1
    if inBounds(newCoords(coords, -2, 1)):
        total += 1
    return total

def digitsProduct(product):

    answerDigits = []
    answer = 0

    if product == 0:
        return 10

    if product == 1:
        return 1

    for divisor in range(9, 1, -1):
        while product % divisor == 0:
            product /= divisor
            answerDigits.append(divisor)

    if product > 1:
        return -1


    for i in range(len(answerDigits) - 1, -1, -1):
        answer = answer + answerDigits[i]
    return int(''.join(map(str,answerDigits[::-1])))

def isComf(a, b):
    s = sum(map(int, str(a)))
    return a != b and b in range(a-s, a+s+1)

def comfortableNumbers(l, r):
    tot = 0
    for a in range(l, r+1):
        for b in range(a+1, r+1):
            if isComf(a, b) and isComf(b, a):
                tot += 1 
    return tot


def chessBoardSquaresUnderQueenAttack(a, b):

    def go(x, y, dx, dy):
        if x < 0 or x >= a or y < 0 or y >= b:
            return 0
        return 1 + go(x+dx, y+dy, dx, dy)

    res = 0

    for i in range(a):
        for j in range(b):
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx != 0 or dy != 0:
                        res += go(i + dx, j + dy, dx, dy)

    return res


def test():
    testeql(comfortableNumbers(10,12), 2)
    testeql(chessBoardSquaresUnderQueenAttack(2, 3), 26)

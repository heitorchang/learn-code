from itertools import permutations

def fullSquareOrCube(number):
    s = str(number)
    squares = [n*n for n in range(1, 41)]
    cubes = [n*n*n for n in range(1, 11)]
    digits = list(map(int, str(number)))
    ways = 0

    testnums = set()
    for c in permutations(digits, len(s)):
        newn = int(''.join(list(map(str, c))))
        testnums.add(newn)

    for n in testnums:
        if n in squares:
            ways += 1
        elif n in cubes:
            ways += 1
    return ways

def spacadet84solution(number):
    n = set(permutations(str(number)))
    ways = 0
    for x in n:
        x = int("".join(x))
        if x**.5 == int(x**.5) or x**(1/3.0)== int(x**(1/3.0)):
            ways += 1
    return ways

def test():
    testeql(fullSquareOrCube(414), 2)
    testeql(fullSquareOrCube(64), 1)

    testeql(spacadet84solution(414), 2)
    testeql(spacadet84solution(64), 1)

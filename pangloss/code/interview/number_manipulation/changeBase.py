def changeBase(n, base):
    digits = []

    while n > 0:
        digits.append(n % base)
        n //= base
    return ''.join(map(str, digits))[::-1]

def test():
    testeql(changeBase(13, 2), "1101")
    testeql(changeBase(66, 3), "2110")
    testeql(changeBase(12345, 8), "30071")

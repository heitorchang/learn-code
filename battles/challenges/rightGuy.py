def rightGuy(k):
    b = bin(k)[2:]
    pr('k b len(b)')
    pr('log(k)/log(2)')

def test():
    testeql(rightGuy(1), 1)
    testeql(rightGuy(2), 2)
    testeql(rightGuy(23), 1)
    testeql(rightGuy(100), 3)
    testeql(rightGuy(234), 2)
    testeql(rightGuy(1073741824), 31)


def bettingGame(l):

    s = 0
    for i in range(len(l)):
        s += l[i]
    if s == 0:
        return False

    return s / len(l) == 0


def test():
    testeql(bettingGame([3,4,8]), True)
    testeql(bettingGame([4,4,5,4]), False)

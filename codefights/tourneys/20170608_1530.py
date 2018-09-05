def isLuckyNumber(n):
    s = set(list(str(n)))
    s.discard('4')
    s.discard('7')
    if len(s) > 0:
        return False
    return True


def test():
    testeql(isLuckyNumber(47), True)
    testeql(isLuckyNumber(20), False)

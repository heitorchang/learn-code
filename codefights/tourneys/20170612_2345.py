def evenDigitsOnly(n):
    d = map(int, str(n))
    odd = filter(lambda n: n % 2 == 1, d)
    return len(list(odd)) == 0


def increaseNumberRoundness(n):

    gotToSignificant = False
    while n > 0:
        pr('n gotToSignificant')
        if n % 10 == 0 and gotToSignificant:
            return True
        elif n % 10 != 0:
            gotToSignificant = True
        n //= 10

    return False




def test():
    # testeql(evenDigitsOnly(642386), False)
    # testeql(increaseNumberRoundness(11000), False)

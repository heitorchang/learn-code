def competitiveEating(t, width, precision):
    return "{:^{width}.{precision}f}".format(t, width=width, precision=precision)

def test():
    testeql(competitiveEating(3.1415, 10, 2), "   3.14   ")

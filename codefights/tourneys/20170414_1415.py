from fractions import Fraction

def fractionSubtraction(a, b):
    fa = Fraction(a[0], a[1])
    fb = Fraction(b[0], b[1])
    c = fa - fb
    return [c._numerator, c._denominator]


def test():
    testeql(fractionSubtraction([7,10],[3,10]), [2,5])

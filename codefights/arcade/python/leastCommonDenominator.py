from fractions import gcd
from functools import reduce

def product(n):
    return reduce(lambda x, y: x * y, n)

def leastCommonDenominator(denominators):
    return reduce(lambda a, b: a * b // gcd(a, b), denominators)

def test():
    testeql(leastCommonDenominator([34, 6, 3, 5, 3]), 510)

# https://www.programiz.com/python-programming/examples/lcm

from fractions import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)

def test():
    testeql(lcm(2, 6), 6)
    testeql(lcm(5, 8), 40)
    testeql(lcm(6, 8), 24)

from math import floor
from fractions import gcd

def maxVassal(num):
    startNum = floor(num ** (1/3))
    for k in range(startNum, 0, -1):
        kCubed = k ** 3
        pr('kCubed')
        if gcd(kCubed, num) != 1:
            return k

def test():
    testeql(maxVassal(42), 3)
    testeql(maxVassal(810), 9)

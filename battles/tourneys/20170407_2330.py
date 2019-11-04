import re

def secondRightmostZeroBit(n):
    s = bin(n)[2:]
    print(s)
    idx0 = s.rfind('0')
    print(s[:idx0])
    idx1 = s[:idx0].rfind('0')
    n = len(s) - idx1 - 1
    return 2 ** n
                   

def test():
    testeql(secondRightmostZeroBit(4), 2)
    testeql(secondRightmostZeroBit(41299),2 ** 3)

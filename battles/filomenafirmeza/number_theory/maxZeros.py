description = """
Given a decimal integer n, find an integer k ≥ 2 such that the representation of n in base k has the maximum possible number of zeros. If there are several answers, output the smallest one.

Example

For n = 9, the output should be
maxZeros(n) = 2.
9 = 10012 = 1003 = 214...
If you'll try all other bases, you'll see that the maximum possible number of zeros in these representations is 2, thus the answer is k = 2.
"""

def newbase(n, b):
    stack = []
    while n > 0:
        stack.append(str(n % b))
        n //= b
    return ''.join(stack[::-1])

def maxZeros(n):
    maxz = 0
    maxb = 0
    for b in range(2, 10):
        newn = newbase(n, b)
        
        numzeros = str(newn).count('0')
        if numzeros > maxz:
            maxz = numzeros
            maxb = b
    return maxb

def test():
    testeql(newbase(21, 3), "210")
    testeql(int("210", 3), 21)
    testeql(newbase(23829, 8), oct(23829)[2:])
    testeql(maxZeros(127), 5)

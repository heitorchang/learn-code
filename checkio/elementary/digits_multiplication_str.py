"""
You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

Input: A positive integer.

Output: The product of the digits as an integer.

Precondition: 0 < number < 106
"""

def checkio(n):
    digits = [int(char) for char in str(n)]
    product = 1
    for d in digits:
        if d != 0:
            product *= d
    return product
    
def test():
    asst(checkio(123405), 120, "ignore zeros")
    asst(checkio(999), 729)
    asst(checkio(1000), 1)

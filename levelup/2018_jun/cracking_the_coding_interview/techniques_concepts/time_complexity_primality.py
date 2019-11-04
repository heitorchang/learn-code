description = """
A prime is a natural number greater than 1 that has no positive divisors other than  and itself. Given  integers, determine the primality of each integer and print whether it is Prime or Not prime on a new line.

Note: If possible, try to come up with an O(sqrt(n)) primality algorithm, or see what sort of optimizations you can come up with for an O(n) algorithm. Be sure to check out the Editorial after submitting your code!
"""

import math

def isprime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
        
    for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False

    return True

def test():
    testeql(isprime(22), False)
    testeql(isprime(29), True)
    testeql(isprime(2), True)

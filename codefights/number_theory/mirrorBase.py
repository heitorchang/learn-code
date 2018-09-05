description = """
Given number (in the form of a string) represented in base1, we'd like to determine whether its digits form a palindrome when represented in base2.
"""

import string as g
from collections import deque as q

def z(n, b):
    # change base from decimal int "n" to base b
    p = g.digits + g.ascii_lowercase
    r = q()  # queue
    while n > 0:
        w = n % b  # least significant digit
        r.appendleft(p[w])
        n //= b
    return ''.join(r)

def mirrorBase(n, i, j):
    d = int(n, i)  # convert to dec first
    m = z(d, j)  # convert to base 2
    return m == m[::-1]  # check if palindrome

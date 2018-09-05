description = """
Note: Avoid using built-in functions that convert integers to their binary representations. Write the solution that uses O(k) operations per test, where k is the number of bits set to 1.

Write a function that takes an unsigned (positive) integer and returns the number of 1 bits its binary representation contains. This value is also known as the integer's Hamming weight.

Example

For n = 13, the output should be
numberOf1Bits(n) = 3.

13 is represented in binary as 1101, so the function should return 3.

Input/Output

[time limit] 4000ms (py3)
[input] integer n

Guaranteed constraints:
0 ≤ n ≤ 231 - 1.

[output] integer
"""

def numberOf1Bits(n):
    res = 0
    while n != 0:
        # FILL IN A LINE HERE
        n &= n-1
        res += 1
    return res

def test():
    testeql(numberOf1Bits(13), 3)
    testeql(numberOf1Bits(2), 1)
    testeql(numberOf1Bits(1024), 1)

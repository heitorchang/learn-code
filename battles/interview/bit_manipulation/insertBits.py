description = """
Given an integer n, replace its bits starting from the bit at position a to the bit at position b, inclusive, with the bits of integer k. Count from the least significant bit to the most significant bit, starting from 0.

Example

For n = 1024, a = 1, b = 6 and k = 17, the output should be
insertBits(n, a, b, k) = 1058.
n = 100 0000 00002, k = 1 00012, 1058 = 100 0010 00102.

For n = 11, a = 1, b = 2 and k = 2, the output should be
insertBits(n, a, b, k) = 13.
n = 10112, k = 102, 13 = 11012.

For n = 1, a = 3, b = 4 and k = 3, the output should be
insertBits(n, a, b, k) = 25.
n = 0 00012, k = 112, 25 = 1 10012.

Input/Output

[time limit] 4000ms (py3)
[input] integer n

Guaranteed constraints:
0 ≤ n < 231.

[input] integer a

Guaranteed constraints:
0 ≤ a ≤ 30.

[input] integer b

Guaranteed constraints:
a ≤ b ≤ 30.

[input] integer k

Guaranteed constraints:
0 ≤ k < 2B - A + 1.

[output] integer

Return n with the bits from a to b replaced with k's bits.
"""

tutorial = """
Updating the ith bit of n to x.

Let's say that we know x is 1 or 0. How would we use it to set the ith bit to x, given that we used AND to clear the bit (set it to 0) but OR to set the bit (set it to 1)?

Here is one approach for what to return (n & (~(1 << i))) | (x << i). What this does is force the ith bit to zero, then ORs it with 0 (if x is zero) or ORs it with a number with only the ith bit set, forcing that bit to 1 if x is 1.
"""

def insertBits(n, a, b, k):
    lenN = n.bit_length()
    lenK = k.bit_length()

    leftMask = ((1 << lenN) - 1) ^ ((1 << (b+1)) - 1)
    # print(bin(n))
    # print(bin(leftMask))

    rightSide = ((1 << a) - 1) & n
    # print(bin(rightSide))

    kInPlace = k << a
    # print(bin(kInPlace))

    return (n & leftMask) | kInPlace | rightSide

def test():
    testeql(insertBits(1024,1,6,17), 1058)
    testeql(insertBits(11, 1, 2, 2), 13)

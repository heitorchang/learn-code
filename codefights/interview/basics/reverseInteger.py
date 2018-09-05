description = """
Reverse the digits of the given integer.

Example

    For x = 12345, the output should be
    reverseInteger(x) = 54321;
    For x = -4243, the output should be
    reverseInteger(x) = -3424.

Input/Output

    [time limit] 4000ms (py3)

    [input] integer x

    Guaranteed constraints:
    -901000 ≤ x ≤ 901000.

    [output] integer

"""

def test():
    testeql(reverseInteger(12345), 54321)
    testeql(reverseInteger(-4243), -3424)
















    


# 250 xp, 1000 coins

def reverseInteger(x):
    # save sign
    if x < 0:
        sign = "-"
    else:
        sign = ""

    n = abs(x)
    return int(sign + str(n)[::-1])


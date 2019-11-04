description = """
Given an integer product, find the smallest positive (i.e. greater than 0) integer the product of whose digits is equal to product. If there is no such integer, return -1 instead.

Example

    For product = 12, the output should be
    digitsProduct(product) = 26;
    For product = 19, the output should be
    digitsProduct(product) = -1.

Input/Output

    [time limit] 4000ms (py3)

    [input] integer product

    Guaranteed constraints:
    0 ≤ product ≤ 600.

    [output] integer

"""

# brute force

def prod(n):
    out = 1
    while n > 0:
        out *= n % 10
        n //= 10
    return out

def digitsProduct(product):
    for i in range(1, 9000):
        if prod(i) == product:
            return i
    return -1


def test():
    testeql(prod(26), 12)
    testeql(digitsProduct(12), 26)
    testeql(digitsProduct(19), -1)

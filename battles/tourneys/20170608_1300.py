def specialPolynomial(x, n):
    s = 0
    k = 0
    while s <= n:
        s += x ** k
        k += 1
        pr('s k n')
    return k - 2

def test():
    testeql(specialPolynomial(2, 5), 1)
    testeql(specialPolynomial(2, 32), 4)
    # 1 + 2 + 4 + 8 + 16 = 4

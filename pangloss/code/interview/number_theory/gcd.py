# SICP GCD, sec. 1.2.5, PDF p. 78

from fractions import gcd

def sicp_gcd(a, b):
    if b == 0:
        return a
    return sicp_gcd(b, a % b)

def test():
    testeql(sicp_gcd(24, 16), gcd(24, 16))
    testeql(sicp_gcd(100, 22), gcd(100, 22))
    testeql(sicp_gcd(206, 40), gcd(206, 40))
    testeql(sicp_gcd(240, 24), gcd(240, 24))
    testeql(sicp_gcd(1, 1), gcd(1, 1))
    testeql(sicp_gcd(1, 0), gcd(1, 0))

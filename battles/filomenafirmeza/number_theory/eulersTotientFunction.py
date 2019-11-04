description = """
Given an integer n, find the value of phi(n), where phi is Euler's totient function.

Example

For n = 5, the output should be
eulersTotientFunction(n) = 4.

Euler’s totient or phi function is an arithmetic function that counts the positive integers less than or equal to n that are relatively prime to n.

Two integers are said to be relatively prime (or coprime) if the only positive integer that evenly divides both of them is 1.
"""

def isrelprime(m, n):
    for i in range(2, min(m, n)+1):  # important: add +1 to min value
        if n % i == 0 and m % i == 0:
            return False
    return True

def eulersTotientFunction(n):
    tot = 0
    for i in range(1, n+1):
        if isrelprime(i, n):
            tot += 1
    return tot


def test():
    testeql(eulersTotientFunction(49), 42)
    testeql(eulersTotientFunction(1), 1)
    testeql(eulersTotientFunction(5), 4)

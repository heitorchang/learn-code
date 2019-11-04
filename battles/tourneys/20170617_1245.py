import math

def maxMultiple(divisor, bound):
    for N in range(bound, 0, -1):
        if N % divisor == 0:
            return N

def quadraticEquation(a, b, c):

    discriminant = b * b - 4 * a * c
    if discriminant < 0:
        return []
    if discriminant == 0:  
        return [- b / (2 * a)]  # pwnt
    roots = []
    roots.append((- b - math.sqrt(discriminant) ) / (2 * a))
    roots.append((- b + math.sqrt(discriminant) ) / (2 * a))
    if roots[0] > roots[1]:
        tmp = roots[1]
        roots[1] = roots[0]
        roots[0] = tmp
    return roots


def test():
    testeql(maxMultiple(3,10), 9)
    testeql(quadraticEquation(1,-3,2), [1,2])
    testeql(quadraticEquation(2,-12,18), [3])

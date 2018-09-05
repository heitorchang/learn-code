from math import sqrt
def quadraticEquation(a, b, c):
    try:
        det = sqrt(b*b - 4*a*c)
        n = (-b + det) / (2*a)
        m = (-b - det) / (2*a)
        if abs(n-m) < 0.0001:
            return [n]
        sol = [n, m]
        return sorted(sol)
    except:
        return []

def test():
    testeql(quadraticEquation(1,2,1), [-1])

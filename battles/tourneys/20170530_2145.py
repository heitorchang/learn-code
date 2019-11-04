from itertools import combinations

def powersOfTwo(n):
    powers = [2**j for j in range(13)]
    for i in range(13):
        combs = combinations(powers, i)
        for c in combs:
            if sum(c) == n:
                return sorted(c)

def test():
    testeql(powersOfTwo(10), [2, 8])

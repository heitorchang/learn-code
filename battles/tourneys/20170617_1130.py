def differentValuesInMultiplicationTable2(n, m):
    vals = set()
    for i in range(1,n+1):
        for j in range(1,m+1):
            vals.add(i*j)
    return len(vals)

from math import sqrt, floor

def eratosthenesSieveEnumerateAll(n):
    # not very efficient, deleted multiples are reused
    nums = set(range(2, n+1))
    for i in range(2, floor(sqrt(n)) + 1):
        for step in range(2*i, n+1, i):
            nums.discard(step)
    return sorted(nums)

def eratosthenesSieve(n):
    lst = list(range(2, n+1))
    counter = 0
    i = lst[counter]
    while i <= floor(sqrt(n)):
        for step in range(2*i, n+1, i):
            try:
                lst.remove(step)
            except ValueError:
                pass
        counter += 1
        i = lst[counter]
    return lst

def test():
    testeql(eratosthenesSieve(9), [2,3,5,7])

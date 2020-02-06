from itertools import combinations_with_replacement as comb

def getf(n):
    ans = []
    for i in range(2, n):
        if n % i == 0:
            ans.append(i)
            
    return ans


def prod(a):
    ans = 1
    for e in a:
        ans *= e
    return ans


def setsOfFactors(n):
    ans = set()
    f = getf(n)
    print(f)
    size = len(f)
    for s in range(2, size+1):
        for c in comb(f, s):
            if prod(c) == n:
                ans.add(tuple(sorted(c, reverse=True)))
    alist = list(ans)
    alist2 = [(n, 1)] + alist
    alist3 = sorted(alist2, reverse=True)
    fin = [list(t) for t in alist3]
    return fin

pairtest(setsOfFactors(10), None)

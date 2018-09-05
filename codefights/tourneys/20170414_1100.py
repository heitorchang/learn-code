def maxSumProduct(a, b, k):
    nsa = [sum(a[:k]) for k in range(11)]
    pr('nsa')
    psa = [sum(a[-k:]) if k else 0 for k in range(11)]
    pr('psa')

def maxSumProductFail(a, b, k):
    aa = list(filter(lambda e: e > 0, a))[::-1]
    bb = list(filter(lambda e: e > 0, b))[::-1]

    maxsum = 0
    selected = 0
    sumaa = 0
    sumbb = 0
    while selected < k:
        if aa[0] > bb[0]:
            sumaa += aa[0]
            selected += 1
        else:
            sumbb += bb[0]
            selected += 1
    return sumaa * sumbb
            
def test():
    testeql(maxSumProduct([-10, 10, 20, 90], [-1, 2, 3, 4, 5], 5), 1320)

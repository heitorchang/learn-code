def countSumOfTwoRepresentations2Error(n, l, r):
    newL = n - r
    if n - r < l:
        return 0
    ints = r - newL + 1
    if ints % 2 == 1:
        return ints // 2 + 1
    return ints // 2

def countSumOfTwoRepresentations2(n, l, r):
    amax = min(n // 2, r)
    amin = max(l, n - r)
    return max(0, amax - amin + 1)

def test():
    testeql(countSumOfTwoRepresentations2(6,2,4), 2)

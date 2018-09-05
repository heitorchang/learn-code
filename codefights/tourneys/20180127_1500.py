def sequenceElementNaive(a, n):
    if n < 5:
        return a[n]
    while n >= 5:
        ans = sum(a[-5:]) % 10
        a.append(ans)
        print(a)
        n -= 1
    return ans

def sequenceElement(a, n):
    pass

def test():
    testeql(sequenceElementNaive([1,2,3,4,5], 9), 4)

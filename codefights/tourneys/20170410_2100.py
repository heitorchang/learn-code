def divisors(n):
    result = []
    for i in range(1, n+1):
        if n % i == 0:
            result.append(n)
    return result

def weakNumbers(n):
    div = divisors(n)
    num_div = []
    weakness = []
    for i in range(1, n+1):
        num_div.append(len(divisors(i)))
    pr('num_div')
    for i in range(1, n):
        wk = 0
        for j in range(1, i):
            pr('i j')
            if num_div[j] > num_div[i]:
                wk += 1
        weakness.append(wk)

    pr('weakness')
    try:
        wkmax = max(weakness)
    
        wkct = weakness.count(wkmax)
    except:
        wkmax = 0
        wkct = 0
    return [wkmax, wkct]


def test():
    testeql(weakNumbers(9), [2,2])

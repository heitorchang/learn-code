def listBeautifier(a):
    res = a[:]
    ct=0
    while res and res[0] != res[-1]:
        if ct > 10:
            break
        res[0:-1] = res
        pr('res')
        ct += 1
    return res

def test():
    testeql(listBeautifier([3, 4, 2, 4, 38, 4, 5, 3, 2]), [4, 38, 4])

def sequenceElement(a, n):
    # TLE
    s = sum(a)
    first = a[0]
    second = a[1]
    third = a[2]
    fourth = a[3]
    fifth = a[4]
    
    for i in range(5, n+1):
        out = s % 10
        pr('out')
        s -= first
        s += out
        first = second
        second = third
        third = fourth
        fourth = fifth
        fifth = out
    return out
    



    
def test():
    # testeql(sequenceElement([1, 2, 3, 4, 5], 9), 4)

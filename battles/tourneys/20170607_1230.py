def alphabetSubstring(s):
    c = s[0]
    o = ord(c)
    isSub = True
    for x in s[1:]:
        if ord(x) != o + 1:
            isSub = False
            break
        o = ord(x)
    return isSub


    
def arrayPacking(a):

    res = 0
    for i in range(len(a)):
        res |= a[i] << 8 * i

    return res
    
def test():
    testeql(arrayPacking([24,85,0]), 21784)

def conv(ltr):
    return ord(ltr.upper()) - ord('A') + 1

def wordSum(w):
    w = w.replace(' ', '')
    return sum(conv(ltr) for ltr in w)

def gematriaEquality(a, b):
    wa = wordSum(a)
    wb = wordSum(b)

    print(wa, wb)
    return wb - wa == 0

    
pairtest(wordSum("a"), 1,
         wordSum("abc"), 6)

def hasMatch(s, t):
    pr('s t')
    return any([c == d for (c, d) in zip(list(s), list(t))])

def notIndexOf(givenString, value):
    for i in range(len(givenString)-len(value)):
        if not hasMatch(givenString[i:], value):
            return i
    return -1
    
def test():
    testeql(hasMatch("Zoo", "oo"), True)
    testeql(hasMatch("abc", "def"), False)
    testeql(hasMatch("axa", "cxd"), True)
    testeql(notIndexOf("Welcome to CodeFights!", "Back to school"), 2)
    testeql(notIndexOf("abc", "abc"), -1)

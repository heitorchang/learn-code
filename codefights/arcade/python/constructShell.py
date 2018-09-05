def constructShell(n):
    return [[0] * n for n in list(range(1,n)) + list(range(n,0,-1))]

def test():
    testeql(constructShell(3), [0])

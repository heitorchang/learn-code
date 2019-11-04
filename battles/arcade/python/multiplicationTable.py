def multiplicationTable(n):
    return [[row * i for i in range(1, n+1)] for row in range(1, n+1)]

def test():
    testeql(multiplicationTable(3), [[1,2,3],[2,4,6],[3,6,9]])

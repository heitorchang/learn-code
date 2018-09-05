from functools import reduce

def fibonacciList(n):
    return [[0] * x for x in reduce(lambda x, y: x + [x[-1] + x[-2]], range(n-2), [0,1])]

def f(n):
    r = range(n)
    return reduce(lambda x, y: x + [x[-1]+x[-2]], r, [0, 1])

def test():
    testeql(fibonacciList(6), [[], 
                    [0], 
                    [0], 
                    [0, 0], 
                    [0, 0, 0], 
                    [0, 0, 0, 0, 0]])

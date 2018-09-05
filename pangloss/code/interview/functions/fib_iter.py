def fib_iter(n):
    """Iterative version of Fibonacci sequence"""
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def test():
    """[0, 1, 1, 2, 3, 5, 8]"""
    testeql(fib_iter(0), 0)
    testeql(fib_iter(1), 1)
    testeql(fib_iter(3), 2)
    testeql(fib_iter(6), 8)
    

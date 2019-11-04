def fibonacciList(n):
    fibs = [1, 1]
    while fibs[-1] <= n:
        fibs.append(fibs[-1] + fibs[-2])
        print(fibs)
    return fibs

test(fibonacciList(20), [1,1,2,3,5,8,13,21])

def step(lst, k, count):
    if count > 10:
        return "STOP"
    # pr('lst')
    if len(lst) == 1:
        return lst[0]
    if k > len(lst):
        removeIndex = k % len(lst)
        if removeIndex == 0:
            return step(lst[:-1], k, count+1)
        else:
            return step(lst[removeIndex:] + lst[:removeIndex-1], k, count+1)
    else: 
        return step(lst[k:] + lst[:k-1], k, count+1)
    
def josephusProblem(n, k):
    circle = list(range(1, n+1))
    return step(circle, k, 0)

def josephusProblemOther(n, k):
    if n == 1:
        return 1    
    return (josephusProblemOther(n - 1, k) + k - 1) % n + 1

def test():
    testeql(josephusProblem(3, 2), 3)
    testeql(josephusProblem(10, 9), 7)
    testeql(josephusProblemOther(10, 9), 7)

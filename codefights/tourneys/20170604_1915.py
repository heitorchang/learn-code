def easyAssignmentProblem(skills):
    pass

def strangeCode(s, e):
    lastProdA = False
    result = ""
    while s < e-1:
        s += 1
        e -= 1
        if not lastProdA:
            result += "a"
            lastProdA = True
        else:
            result += "b"
            lastProdA = False
    return result

def josephusProblem(n, k):
    if n == 1:
        return 1    
    return (josephusProblem(n - 1, k) + k - 1) % n + 1


def computeDefiniteIntegral(l, r, p):
    pass


def digitSum(n):

    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10

    return sum

# 20:15 : OWNAGE

def fiblist(a, b, lim):
    lst = []
    while b < lim:
        lst.append(a)
        tmp = a
        a = b
        b = tmp + b
    return lst

# todo: why recursive lst doesn't work

def fiblistRec(a, b, lim, lst):
    if a > lim:
        return lst
    # lst.append(a) does not return new list!
    return fiblistRec(b, a+b, lim, lst + [a])

def fibonacciSum(n):
    lst = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 1597+2584]
    lst = lst[::-1]
    result = []
    while n > 0:
        for i in range(len(lst)):
            if lst[i] <= n:
                result.append(lst[i])
                n -= lst[i]
    return list(reversed(result))



def test():
    # testeql(strangeCode(4, 8), "ab")
    # testeql(strangeCode(10, 16), "aba")
    # testeql(fibonacciSum(33), [1,3,8,21])
    # testeql(fiblistRec(1,1,10,[]), [1,1,2,3,5,8])

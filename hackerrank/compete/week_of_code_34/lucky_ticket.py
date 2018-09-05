def sumDigits(n):
    return sum(map(int, str(n)))

def onceInATram(x):
    left = x // 1000
    leftSum = sumDigits(left)
    right = x % 1000
    # pr('left leftSum')
    for i in range(right+1, 1000):
        if sumDigits(i) == leftSum:
            return left * 1000 + i
    # number was already beyond given range
    left += 1
    leftSum += 1
    for i in range(1000):
        if sumDigits(i) == leftSum:
            return left * 1000 + i
    

def test():
    testeql(onceInATram(555555), 555564)
    testeql(onceInATram(165901), 165903)

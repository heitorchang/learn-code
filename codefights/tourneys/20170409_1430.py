def isSumOfConsecutive2(n):
    total = 0
    for i in range(1, n):
        s = i
        for j in range(i+1, n):
            pr('i j')
            s += j
            if s == n:
                print('match')
                total += 1
            elif s > n:
                break
    return total
    

def test():
    testeql(isSumOfConsecutive2(15), 3)

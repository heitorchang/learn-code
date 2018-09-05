def digitSumsDifference(n):
    digits = list(map(int, list(str(n))))
    evens = filter(lambda n: n % 2 == 0, digits)
    odds = filter(lambda n: n % 2 == 1, digits)
    return sum(evens) - sum(odds)

def powersOfTwo(n):

    ans = []
    cur = 1
    while n > 0:
        if n % 2 == 1:
            ans.append(cur)
        n = n >> 1
        cur <<= 1

    return ans


def test():
    # testeql(digitSumsDifference(1203), -2)
    # testeql(digitSumsDifference(412), 5)
    testeql(powersOfTwo(5), [1,4])

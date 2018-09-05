def cutRodBottomUp(prices, length):
    prices = [0] + prices
    r = [0] * (length+1)
    r[0] = 0
    for j in range(1, length+1):
        q = float('-inf')
        for i in range(1, j+1):
            q = max(q, prices[i] + r[j-i])
        r[j] = q
    return r[length]

def test():
    testeql(cutRodBottomUp([1,5,8,9,10,17,17,20,24,30], 4), 10)
    testeql(cutRodBottomUp([1,5,8,9,10,17,17,20,24,30], 6), 17)
    testeql(cutRodBottomUp([1,5,8,9,10,17,17,20,24,30], 10), 30)

def almostIncreasingSequence(sequence):
    diffs = [a - b for (a, b) in zip(sequence, sequence[1:])]
    return diffs

def splitByValue(k, elements):
    result = []
    for i in range(len(elements)):
        if elements[i] < k:
            result.append(elements[i])
    for i in range(len(elements)):
        if elements[i] >= k:
            result.append(elements[i])
    return result


def minimalNumberOfCoins(coins, price):
    #greedy
    c = sorted(coins, reverse=True)
    numCoins = 0
    ctr = 0
    
    while price > 0:
    # while ctr < 10:
        maxCoin = 0
        for coin in c:
            if price >= coin:
                # pr('price coin')
                price -= coin
                numCoins += 1
                break
        ctr += 1
    return numCoins


    

    
def test():
    testeql(splitByValue(5, [1, 3, 5, 7, 6, 4, 2]), [1, 3, 4, 2, 5, 7, 6])

    testeql(minimalNumberOfCoins([1,2,10], 28), 6)

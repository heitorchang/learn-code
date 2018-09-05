description = """
You have a collection of coins, and you know the values of the coins and the quantity of each type of coin in it. You want to know how many distinct sums you can make from non-empty groupings of these coins.

Example

For coins = [10, 50, 100] and quantity = [1, 2, 1], the output should be
possibleSums(coins, quantity) = 9.

Here are all the possible sums:

    50 = 50;
    10 + 50 = 60;
    50 + 100 = 150;
    10 + 50 + 100 = 160;
    50 + 50 = 100;
    10 + 50 + 50 = 110;
    50 + 50 + 100 = 200;
    10 + 50 + 50 + 100 = 210;
    10 = 10;
    100 = 100;
    10 + 100 = 110.

As you can see, there are 9 distinct sums that can be created from non-empty groupings of your coins.

Input/Output

    [time limit] 4000ms (py3)

    [input] array.integer coins

    An array containing the values of the coins in your collection.

    Guaranteed constraints:
    1 ≤ coins.length ≤ 20,
    1 ≤ coins[i] ≤ 104.

    [input] array.integer quantity

    An array containing the quantity of each type of coin in your collection. quantity[i] indicates the number of coins that have a value of coins[i].

    Guaranteed constraints:
    quantity.length = coins.length,
    1 ≤ quantity[i] ≤ 105.

    It is guaranteed that (quantity[0] + 1) * (quantity[1] + 1) * ... * (quantity[quantity.length - 1] + 1) <= 106.

    [output] integer

    The number of different possible sums that can be created from non-empty groupings of your coins.

"""

hints = """
some people say DP, others say it's brute-forceable because of small amount in quantity
"""

def test():
    testeql(possibleSums([10, 50, 100, 500], [5, 3, 2, 2]), 122)
    # testeql(incrementArray([0, 1, 0], 2, [2, 1, 2]), [0, 1, 1])
    # testeql(incrementArray([0, 1, 1], 2, [2, 1, 2]), [0, 1, 2])
    # testeql(incrementArray([1, 1, 2], 2, [2, 1, 2]), [2, 0, 0])
    # testeql(incrementArray([2, 1, 2], 2, [2, 1, 2]), None)
    # testeql(computeSum([10, 20, 50], [1,2,1]), 100)
    # testeql(step([0,0,0],2,[1,2,1],[10,20,5],0), ([0,0,1],5))
    # testeql(step([0,0,1],2,[1,2,1],[10,20,5],5), ([0,1,0],20))
    # testeql(step([0,1,0],2,[1,2,1],[10,20,5],20), ([0,1,1],25))
    # testeql(step([0,1,1],2,[1,2,1],[10,20,5],25), ([0,2,0],40))
    # testeql(possibleSums([1, 1, 3, 5], [1,1,1,1]), 10)
    testeql(possibleSumsAWice([1,1,1,1,1], [9,19,18,12,19]), 77)
    testeql(possibleSumsAWice([1,2,3], [2,3,10000]), 30008)
    testeql(possibleSumsAWice([1, 2], [50000, 2]), 50004)
    testeql(possibleSumsAWice([10, 50, 100], [1,2,1]), 9)

# FIRST ATTEMPT : TLE
# def incrementArray(state, digit, limit):
#     if digit < 0:
#         return None
#     if state[digit] == limit[digit]:
#         state[digit] = 0
#         return incrementArray(state, digit-1, limit)
#     state[digit] += 1
#     return state

# def computeSum(coins, quantity):
#     return sum([c * q for c, q in zip(coins, quantity)])
    
# def possibleSumsTLE(coins, quantity):
#     # time limit exceeded
#     sums = set()
#     numCoins = len(coins)
#     state = [0] * numCoins
#     state = incrementArray(state, numCoins-1, quantity)
#     while state:
#         sums.add(computeSum(coins, state))
#         state = incrementArray(state, numCoins-1, quantity)
#     return len(sums)

# SECOND ATTEMPT
def step(state, digit, limit, values, total):
    if digit < 0:
        return None, total
    if state[digit] == limit[digit]:
        state[digit] = 0
        return step(state, digit-1, limit, values,
                    total - (limit[digit] * values[digit]))
    state[digit] += 1
    return state, total + values[digit]

def possibleSums(coins, quantity):
    # still time limit exceeded
    sums = set()
    numCoins = len(coins)
    state = [0] * numCoins
    state, tot = step(state, numCoins-1, quantity, coins, 0)
    while state:
        sums.add(tot)
        state, tot = step(state, numCoins-1, quantity, coins, tot)
    return len(sums)

# http://codeforces.com/blog/entry/20713
# take array of integers

# def possibleSums(coins, quantity):
#     # Fails test cases. Very phail
#     n = len(coins)
#     a = []
#     for i in range(n):
#         a += [coins[i]] * quantity[i]

#     found = {}

#     lenA = len(a)
    
#     S = []
#     ctr = 0

#     for i in range(lenA):
#         if a[i] not in found:
#             S.append(a[i])
#             ctr += 1
#             found[a[i]] = True
#             m = ctr - 1
#         else:
#             m = ctr
#         for j in range(m):
#             if a[i] + S[j] not in found:
#                 S.append(a[i] + S[j])
#                 ctr += 1
#                 found[a[i] + S[j]] = True
#     return ctr

# http://www.geeksforgeeks.org/find-distinct-subset-subsequence-sums-array/

# TIMES OUT ON SAMPLE TESTS
from collections import defaultdict

def printSums(arr):
    arrSum = sum(arr)
    n = len(arr)
    # dp = [row[:] for row in [[0] * (arrSum+1)] * (n+1)]
    dp = defaultdict(dict)

    for i in range(n+1):
        dp[i][0] = True
    
    for i in range(1, n+1):
        dp[i][arr[i-1]] = True
        for j in range(1, arrSum+1):
            if j in dp[i-1]:
                dp[i][j] = True
                dp[i][j + arr[i-1]] = True
    ct = 0
    pr('arrSum')
    for j in range(1, arrSum+1):
        if j in dp[n]:
            ct += 1
            # pr('j')
    return ct
            
def possibleSums(coins, quantity):
    a = []
    for i in range(len(coins)):
        a += [coins[i]] * quantity[i]
    return printSums(a)

def possibleSumsAWice(coins, quantity):
    seen = {0}
    for coin, qty in zip(coins, quantity):
        seen = {amt + part for amt in seen for part in range(0, coin * qty + 1, coin)}
    return len(seen) - 1

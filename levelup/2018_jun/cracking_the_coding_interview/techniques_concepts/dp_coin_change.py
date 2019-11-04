description = """
Given a number of dollars, n, and a list of dollar values for m distinct coins, C = {c0, c1, c2, ..., cm-1}, find and print the number of different ways you can make change for  dollars if each coin is available in an infinite quantity.

Hints:

You can solve this problem recursively, but you must optimize your solution to eliminate overlapping subproblems using Dynamic Programming if you wish to pass all test cases. More specifically, think of ways to store the checked solutions and use the stored values to avoid repeatedly calculating the same values.
Think about the degenerate cases: 
How many ways can you make change for 0 dollars?
How many ways can you make change for less than 0 dollars if you have no coins?
If you are having trouble defining the storage for your precomputed values, then think about it in terms of the base case .

Sample 0
n = 4, coins = 1,2,3

{1,1,1,1}  
{1,1,2}   {1,2,1}   {2,1,1}
{2,2}     {2,2}
{1,3}     {3,1}

{1}

{1,1}
{2}

{1,1,1}
{1,2}
{3}
"""

# BEST SOLUTION
def coinchange(n, coins):
    """Geeks for geeks space optimized"""
    dp = [0] * (n+1)
    dp[0] = 1
    # pick all coins one by one and update dp after the index greater
    # than or equal to the value of the picked coin
    for coin in coins:        
        for j in range(coin, n+1):
            dp[j] += dp[j-coin]
    return dp[-1]


def coinchangeTimeout(n, coins):
    dp = [set() for _ in range(n+1)]
    # dp = [0] * (n+1)
    m = len(coins)
    dp[0].add((0,) * m)
    for i in range(1, n+1):
        for j, c in enumerate(coins):
            if i >= c:
                for t in dp[i-c]:  # existing ways
                    newWay = list(t)
                    newWay[j] += 1
                    newWayTuple = tuple(newWay)
                    dp[i].add(newWayTuple)
    return len(dp[-1])

def coinchangeFail(n, coins):
    """seems to ignore repeated coins"""
    dp = [0] * (n + 1)
    for i in range(1, n+1):
        for c in coins:
            value = i
            while value >= c:
                existing = max(dp[i-c]+1, dp[i])
                # print(i, c, existing)
                dp[i] = existing
                value -= c
        print(dp)
    return dp[-1]

def coinchange2d(n, coins):
    """Geeks for geeks"""
    m = len(coins)
    dp = [[0 for _ in range(m)] for _ in range(n+1)]
    for i in range(m):
        dp[0][i] = 1

    for i in range(1, n+1):
        for j in range(m):
            x = dp[i - coins[j]][j] if i-coins[j] >= 0 else 0
            y = dp[i][j-1] if j >= 1 else 0
            dp[i][j] = x + y
    return dp[n][m-1]


def test():
    testeql(coinchange(4, [1,2,3]), 4)
    testeql(coinchange(10, [2,3,5,6]), 5)
    # testeql(coinchange(166, [5,37,8,39,33,17,22,32,13,7,10,35,40,2,43,49,46,19,41,1,12,11,28]), 96190959)
    testeql(coinchange(75, [25,10,11,29,49,31,33,39,12,36,40,22,21,16,37,8,18,4,27,17,26,32,6,38,2,30,34]), 16694)
    # testeql(coinchange(18, [49,9,40,17,46,24,42,26,43,41,35,1,47,28,20,38,2,44,32,22,18,45,25]), 18)

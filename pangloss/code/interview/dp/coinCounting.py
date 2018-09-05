def minCoins(coins, s):
    dp = [float('inf')] * (s+1)
    dp[0] = 0

    for i in range(s+1):
        for j in range(len(coins)):
            if coins[j] <= i and dp[i-coins[j]] + 1 < dp[i]:
                dp[i] = dp[i-coins[j]] + 1
    return dp[-1]

def test():
    testeql(minCoins([1,3,5], 5), 1)
    testeql(minCoins([1,3,5], 11), 3)

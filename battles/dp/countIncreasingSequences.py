def countIncreasingSequences(n, k):
    # Part of a tourney bugfix,
    # majority of the code was pre-written


    # Given integers n and k, find the number of strictly increasing sequences of length n consisting of positive integers not exceeding k

    # Example

    # For n = 2 and k = 3, the output should be
    # countIncreasingSequences(n, k) = 3.
    # They are: [1, 2], [1, 3] and [2, 3].
    
    ##
    #  list dp (short for dynamic programming)
    #  is used for storing the interim values.
    ##
    dp = []
    ans = 0

    for i in range(n + 1):
        line = []
        for j in range(k + 1):
            line.append(0)
        dp.append(line)
    dp[0][0] = 1

    for i in range(1, n + 1):
        for j in range(1, k + 1):
            for q in range(j):
                dp[i][j] += dp[i - 1][q]

    for j in range(1, k + 1):
        ans += dp[n][j]

    pr('dp')

    return ans


def test():
    testeql(countIncreasingSequences(2,3), 3)
    testeql(countIncreasingSequences(1,4), 4)
    testeql(countIncreasingSequences(3,7), 35)

description = """
Davis has s staircases in his house and he likes to climb each staircase 1, 2, or 3 steps at a time. Being a very precocious child, he wonders how many ways there are to reach the top of the staircase.

Given the respective heights for each of the  staircases in his house, find and print the number of ways he can climb each staircase on a new line.

Input Format

The first line contains a single integer, s, denoting the number of staircases in his house. 
Each line i of the  subsequent lines contains a single integer, n, denoting the height of staircase .
"""

def staircaseWays(n, memo):
    if n in memo:
        return memo[n]

    if n < 0:
        return 0
    if n == 0:
        return 1

    ways = staircaseWays(n - 1, memo) + staircaseWays(n - 2, memo) + staircaseWays(n - 3, memo)
    memo[n] = ways
    return ways

def test():
    memo = {}
    testeql(staircaseWays(1, memo), 1)
    testeql(staircaseWays(3, memo), 4)
    testeql(staircaseWays(7, memo), 44)

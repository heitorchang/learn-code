description = """
You are climbing a staircase that has n steps. You can take the steps either 1 or 2 at a time. Calculate how many distinct ways you can climb to the top of the staircase.

Example

    For n = 1, the output should be
    climbingStairs(n) = 1;

    For n = 2, the output should be
    climbingStairs(n) = 2.

    You can either climb 2 steps at once or climb 1 step two times.

Input/Output

    [time limit] 4000ms (py3)

    [input] integer n

    Guaranteed constraints:
    1 ≤ n ≤ 50.

    [output] integer

    It's guaranteed that the answer will fit in a 32-bit integer.

"""

def dp(n, memo):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n in memo:
        return memo[n]
    memo[n] = dp(n-1, memo) + dp(n-2, memo)
    return memo[n]

def climbingStairs(n):
    return dp(n, {})

def test():
    testeql(climbingStairs(1), 1)
    testeql(climbingStairs(2), 2)
    testeql(climbingStairs(26), 196418)
    # testeql(climbingStairs(50), 9901) # it's over 9000

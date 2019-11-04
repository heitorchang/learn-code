description = """
You and a friend are on your way to go hiking in the Gatineaus, and you've decided to stop in the Byward market for some breakfast. You order a large double-double, 2 beavertails, a small poutine, and a box of timbits.

You pay for the food and as you're waiting to receive your change, you start thinking about how many different combinations of coins could be used. In Canada, there are 5 types of coins:

A 5-cent coin called a "nickel"
A 10-cent coin called a "dime"
A 25-cent coin called a "quarter"
A 100-cent coin called a "loonie"
A 200-cent coin called a "toonie"
There also used to be a 1-cent coin known as the "penny", but it was removed from circulation in 2013. You're wondering how many more combinations would have been possible if we still had pennies.

Given an integer change, representing the amount of change you're owed (in cents), find how many combinations of coins could be used that would include at least 1 penny.

Since this could be a huge number, return the result mod 109 + 7.
"""
from functools import lru_cache

# stack overflow
import sys
sys.setrecursionlimit(5500000)

@lru_cache(maxsize=None)
def cc(amt, coins):
    # SICP Ex. 2.19
    if amt == 0:
        return 1
    elif amt < 0 or len(coins) == 0:
        return 0
    else:
        return cc(amt, coins[1:]) + cc(amt - coins[0], coins)
    
def makingCents(n):
    coins = (200, 100, 25, 10, 5, 1)
    return cc(n-1, coins) % (10**9 + 7)

test(makingCents(10), 2,
makingCents(11), 4)

desc = """
You're running a "Buy 2, Get 1 Free" promotion at your store. Your customers can group any 3 consecutive items in their shopping cart, and the cheapest item from every such group of 3 items will be free.

Given a list of prices, your task is to maximize the discount your customer can get.

Example

For prices = [10, 20, 17, 7, 16, 19, 16], the output should be
maxDiscount(prices) = 26.

The customer can group their items as follows: (10, 20, 17), 7, (16,19,16). Thus, they can get a $10 discount from the first group and a $16 discount from the second group, for a total discount of $26.

For prices = [1, 2, 7, 8, 10, 2], the output should be
maxDiscount(prices) = 7.

The customer can group their items as follows: 1, 2, (7, 8, 10), 2. Thus, they can get a $7 discount.

Input/Output

[time limit] 4000ms (py3)
[input] array.integer prices

An array of integers that represents the prices of each item in the customer's cart.

Guaranteed constraints:
3 ≤ prices.length ≤ 2000,
1 ≤ prices[i] ≤ 1000.

[output] integer

The maximum discount the customer can receive, given the rules above.
"""

def disc(a):
    return min(a)

def maxDiscount(prices):
    len_prices = len(prices)
    subproblem = [0 for _ in range(len_prices)]
    best = 0
    
    for i in range(2, len_prices):
        if i > 4:
            free_to_use = max(subproblem[:i-2])
        else:
            free_to_use = 0
        cur_disc = min(prices[i-2:i+1])
        best = max(best, cur_disc + free_to_use)
        subproblem[i] = best
    return best

def maxDiscountSubmitted(prices):
    len_prices = len(prices)
    optimal = [0 for _ in range(len_prices)]
    
    for i in range(2, len_prices):
        pr('i prices[i] optimal[:i-1] optimal')
        if i > 4:
            free = max(optimal[:i-2])
        else:
            free = 0
        cur_disc = min(prices[i-2:i+1])
        optimal[i] = max(max(optimal[:i]), cur_disc + free)
    return max(optimal)

def test():
    # testeql(maxDiscount([53, 91, 53, 46, 70, 50, 70, 63, 81, 48, 20, 95, 35, 80, 68, 21, 48, 40, 22, 93]), 240)
    testeql(maxDiscount([10, 20, 17, 7, 16, 19, 16]), 26)
    testeql(maxDiscount([10, 20, 9]), 9)

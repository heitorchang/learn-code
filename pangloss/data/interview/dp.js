data = data.concat([

//////////////////////////////////////////////////////////////////////
//
// DYNAMIC PROGRAMMING
//
//////////////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Dynamic Programming',
    title: 'Coin counting',
    reference: 'https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/',
    description: `Given a list of N coins valued (V1, V2, V3, ...) and a total sum S, find the minimum number of coins to total S (we can use as many coins of one type as we want), or report that it is not possible to get to sum S`,
    code: `
 def minCoins(coins, s):
    dp = [float('inf')] * (s+1)
    dp[0] = 0

    for i in range(s+1):
        for j in range(len(coins)):
            if coins[j] <= i and dp[i-coins[j]] + 1 < dp[i]:
                dp[i] = dp[i-coins[j]] + 1
    return dp[-1]   
    `
  },

  { // begin new topic
    topic: 'Dynamic Programming',
    title: 'Top-down vs. Bottom-up',
    reference: 'Intro to Algorithms, 365',
    description: `Using a top-down approach, the procedure is written recursively in a natural matter, but also uses memoization to save the result of each subproblem.<br><br>A bottom-up approach typically depends on some natural notion of the "size" of a subproblem, such that solving a subproblem depends only on solving "smaller" subproblems. Subproblems are sorted by size and solved in order, smallest first`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Dynamic Programming',
    title: 'Memoization',
    reference: 'Python Fluente, 240',
    description: `Memoization is the process of storing previously computed results in a quickly accessible place (a dictionary). The built-in <code>@functools.lru_cache</code> (Least Recently Used Cache) is an easy way to memoize a function.<br><br>
    The signature is: <code>@functools.lru_cache(maxsize=128, typed=False)</code><br><br>
    If maxsize is None, the cache can grow without bound. If typed is True, arguments of different types will be cached separately.
    `,
    code: `
import functools

@functools.lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    `
  },

  { // begin new topic
    topic: 'Dynamic Programming',
    title: 'Rod cutting',
    reference: 'Intro to Algorithms, 362',
    description: `A rod of length L is to be cut into several pieces, or left intact. Given an array of prices for pieces of increasing lengths, determine the most money that can be made from this rod.`,
    code: `
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
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },



  ]);

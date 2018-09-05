from math import log

description = """
You are playing a number guessing game with your friend. Your friend thought of some integer x from 1 to n. In order to guess the number, you can ask two types of questions:

"is x smaller or equal to a?" for some integer a;
"is x greater or equal to a?" for some integer a.
If the answer to your question is "yes", you should pay your friend $2, otherwise you should pay him $1.

How much will you have to pay to your friend, assuming that you apply the strategy that minimizes the amount of money you have to pay in order to guess the number in the worst case scenario?
"""

def numberGuessingNaive(n):
    # solution by sensytive
    p=[0]*(n+1)
    for i in range(2,n+1):
        p[i]=i 
        for m in range(1,i):
            pr('p[i] 1+p[m] 2+p[i-m]')
            p[i] = min(p[i], max(1+p[m], 2+p[i-m]))
        pr('p')
    return p[-1]

def factorialsProductTrailingZeros(l, r):
    result = 0
    last = 0
    for i in range(1, r + 1):
        number = i
        while number % 5 == 0:
            number /= 5
            result += 1
        if i >= l:
            pr('result last')
            result += last
    return result


def test():
    testeql(numberGuessingNaive(4),4)
    testeql(numberGuessingNaive(3),3)
    testeql(numberGuessingNaive(1),0)
    # testeql(numberGuessingNaive(534),14)
    testeql(factorialsProductTrailingZeros(4, 10), 7)
    testeql(numberGuessingNaive(15), 0)
    testeql(numberGuessingNaive(9), 0)

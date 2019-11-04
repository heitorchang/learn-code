from collections import defaultdict
def composeKPalindromes(s, k):
    histogram = defaultdict(int)
    for c in list(s):
        histogram[c] += 1
    print(histogram)
    for c in histogram:
        totalOptions = 0

def composeKPalindromesOtherSolution(s, k):
    L = list(set(list(s)))
    C = [s.count(l) for l in L]
    odds = sum(1 for c in C if c%2)
    pr('C')
    pr('s odds')
    if odds>k:
        return False
    if k>len(s):
        return False
    return True
        
def candles(candlesNumber, makeNew):
    burned = 0
    leftovers = 0
    while candlesNumber > 0:
        pr('candlesNumber burned leftovers')
        burned += candlesNumber
        leftovers += candlesNumber
        candlesNumber = leftovers // makeNew
        print(leftovers % makeNew)
        leftovers %= makeNew
    return burned


def test():
    testeql(composeKPalindromesOtherSolution("abacaba", 6), True)
    testeql(composeKPalindromesOtherSolution("abacaba", 5), True)

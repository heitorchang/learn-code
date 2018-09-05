
def arrayMaxConsecutiveSumTLE(inputArray, k):
    # time limit exceeded
    maxSum = float('-inf')
    for i in range(len(inputArray)-k+1):
        window = inputArray[i:i+k]
        s = sum(window)
        if s > maxSum:
            maxSum = s
    return maxSum

def arrayMaxConsecutiveSum(inputArray, k):
    s = sum(inputArray[:k])
    maxSum = s
    for i in range(k, len(inputArray)):
        s += inputArray[i]
        s -= inputArray[i-k]
        if s > maxSum:
            maxSum = s
    return maxSum

def eulersTotientFunction(n):
    divisor = 2
    result = n

    while divisor * divisor <= n:
        if n % divisor == 0:
            while n % divisor == 0:
                n /= divisor
            result -= result / divisor
        divisor += 1
    if n > 1:
        result -= result / n
    return result

def maxFraction(numerators, denominators):

    maxFractionIndex = 0
    for i in range(1, len(numerators)):
        if (numerators[i] * denominators[maxFractionIndex] >
                numerators[maxFractionIndex] * denominators[i]):
            maxFractionIndex = i
    return maxFractionIndex



def test():
    # testeql(arrayMaxConsecutiveSum([2,3,5,1,6], 2), 8)
    # testeql(arrayMaxConsecutiveSum([1,3,2,4], 3), 9)
    # testeql(eulersTotientFunction(5), 4)
    # testeql(eulersTotientFunction(49), 42)

    

def isUnusual(n):
    digits = list(map(int, str(n)))
    s = sum(digits)
    prod = 1
    for j in digits:
        prod *= j
    return s > prod
    
def smallestUnusualNumber(a):
    n = int(a)
    while True:
        if isUnusual(n):
            return n - int(a)
        n += 1

def fibonacciSimpleSum2(n):
    fib = [0, 1]
    cnt = 2

    while fib[cnt - 1] + fib[cnt - 2] < n:
        fib.append(fib[cnt - 1] + fib[cnt - 2])
        cnt += 1

    for i in range(cnt):
        if fib[i] + fib[cnt - 1] == n:
            return True

    return False
       
def binarySearch(inputArray, searchElement):

    minIndex = -1
    maxIndex = len(inputArray)

    while minIndex < maxIndex - 1:
        currentIndex = (minIndex + maxIndex) // 2
        currentElement = inputArray[currentIndex]

        if currentElement < searchElement:
            minIndex = currentIndex
        else:
            maxIndex = currentIndex

    if maxIndex == len(inputArray) or inputArray[maxIndex] != searchElement:
        return -1
    return maxIndex        
        
def test():
    testeql(isUnusual(21), True)
    testeql(isUnusual(22), False)
    testeql(fibonacciSimpleSum2(11), True)

def howManySundays(n, startDay):
    days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    i = days.index(startDay)
    x = i + n
    return x // 7


def arrayMaxConsecutiveSum(inputArray, k):

    result = 0
    currentSum = 0

    for i in range(k - 1):
        currentSum += inputArray[i]
    for i in range(k - 1, len(inputArray)):
        currentSum += inputArray[i]
        if currentSum > result:
            result = currentSum
        currentSum -= inputArray[i - k + 1]
    return result

    
def test():
    testeql(howManySundays(9, "Saturday"), 2)
    testeql(howManySundays(7, "Sunday"), 1)
    testeql(howManySundays(6, "Monday"), 1)
    testeql(howManySundays(3, "Monday"), 0)
    testeql(arrayMaxConsecutiveSum([2, 3, 5, 1, 6], 2), 8)

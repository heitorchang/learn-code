from itertools import combinations

# time : coins
# 20:33 : 298,626
# 21:15 : 300,588

def growingPlant(upSpeed, downSpeed, desiredHeight):

    currentHeight = 0
    dayIndex = 1

    while currentHeight + upSpeed < desiredHeight:
        currentHeight += upSpeed - downSpeed
        dayIndex += 1

    return dayIndex

def maxSumSegments(inputArray):
    result = []
    lenI = len(inputArray)
    for length in range(1, lenI + 1):
        maxSum = float('-inf')
        maxIndex = lenI
        for start in range(lenI - length, -1, -1):
            s = sum(inputArray[start:start+length])
            pr('s')
            if s >= maxSum:
                maxSum = s
                maxIndex = start
        result.append(maxIndex)
    return result
            

def test():
    testeql(growingPlant(100, 10, 910), 10)
    testeql(growingPlant(10, 9, 4), 1)
    # testeql(maxSumSegments([-1, 2, 1, 3, -2]), [3,2,1,0,0])

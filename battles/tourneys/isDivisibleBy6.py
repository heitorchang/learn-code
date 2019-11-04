def isDivisibleBy6(inputString):
    digitSum = 0
    leftBound = ord('0')
    rightBound = ord('9')
    answer = []
    mask = list(inputString)
    asteriskPos = -1

    for i in range(len(mask)):
        if (leftBound <= ord(mask[i]) and
          ord(mask[i]) <= rightBound):
            digitSum += ord(mask[i]) - leftBound
        else:
            asteriskPos = i

    for i in range(0, 10):
        if (digitSum + i) % 3 == 0:
            mask[asteriskPos] = chr(leftBound + i)
            if (ord(mask[len(mask) - 1]) - leftBound) % 2 == 0:
                answer.append(''.join(mask))

    return answer

def test():
    testequal(isDivisibleBy6("1*0"), ["120", 
                                      "150", 
                                      "180"])
    testequal(isDivisibleBy6("81234567890*"), ["812345678904"])

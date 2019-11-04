def test():
    testeql(isIPv4Address("172.16.254.1"), True)
    testeql(isIPv4Address("172.16.354.1"), False)


def isIPv4Address(inputString):

    currentNumber = 0
    emptyField = True
    countNumbers = 0

    inputString += '.'

    for i in range(len(inputString)):
        if inputString[i] == '.':
            if emptyField:
                return False
            countNumbers += 1
            currentNumber = 0
            emptyField = True
        else:
            digit = ord(inputString[i]) - ord('0')
            if digit < 0 or digit > 9:
                return False
            currentNumber = currentNumber * 10 + digit
            emptyField = False
            if currentNumber > 255:
                return False
        pr('countNumbers')
    return countNumbers == 4

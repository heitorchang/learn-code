def powersOfTwo(n):
    b = bin(n)[2:]
    b = b[::-1]
    lb = list(b)
    i = 0
    pws = []
    for c in lb:
        if c == '1':
            pws.append(2 ** int(i))
        i += 1
    return pws

def waterTubes(water, flowPerMinute):
    result = 0

    for i in range(len(water)):
        minutes = water[i] // flowPerMinute[i]
        if water[i] % flowPerMinute[i] != 0:
            minutes += 1

        if result >= minutes:
            result += minutes
    return result
    # does not pass

def isLucky(n):

    digits = []
    sum = 0

    while (n > 0):
        digits.append(n % 10)
        n = n // 10

    for i in range(len(digits)):
        if i < len(digits) // 2:
            sum += digits[i]
        else:
            sum -= digits[i]

    if sum != 0:
        return False
    return True

def test():
    # testeql(powersOfTwo(10), [2, 8])
    testeql(waterTubes([1,2,5], [1,1,2]), 3)

def addDigits(a, b, n):
    rem = a % b

    result = []
    result.append(str(a))

    for i in range(n):
        best = -1
        for digit in range(9, -1, -1):
            if (rem * 10 + digit) % b == 0:
                best = digit
                break
        if best == -1:
            break
        result.append(str(best))
        rem = (rem * 10 + best) % b

    return ''.join(result)

def videoPart(part, total):

    def getSeconds(time):
        h = int(time[0:2])
        m = int(time[3:5])
        s = int(time[6:8])
        return h * 60 * 60 + m * 60 + s

    def gcd(a, b):
        while a > 0:
            tmp = a
            a = b % a
            b = tmp
        return b

    partTime = getSeconds(part)
    totalTime = getSeconds(total)
    divisor = gcd(partTime, totalTime)
    return [partTime / divisor, totalTime / divisor]
 #pr('partTime totalTime')

def step(n):
    return sum(map(int, str(n)))

def iter(n, steps):
    if n < 10:
        return steps
    return iter(step(n), steps+1)

def digitDegree(n):
    return iter(n, 0)

def test():
    testeql(addDigits(5,13,10), "52000000000")
    testeql(videoPart("00:02:20", "00:10:00"), [7,30])
    testeql(step(91), 10)
    testeql(digitDegree(99), 2)

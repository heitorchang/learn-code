def reciprocal(n, d):
    if n == 1:
        return 0
    return findRecRepeat(n, d)

def findRecRepeat(n, digit):
    s = str(longDivision(1, n, 5000))
    # count leading zeros
    zeros = 0
    for i in range(len(s)):
        if s[i] != '0':
            zeros = i
            break
    if digit <= zeros:
        return 0
    pat = findRepeat(s[zeros:])
    if pat == "0":
        return 0
    digit -= zeros
    return int(pat[(digit % len(pat)) - 1])

def longDivision(num, denom, d):
    """Compute a fraction a / b, a < b up to d places"""
    result = ""
    rt = num
    for i in range(d):
        rt *= 10
        if rt >= denom:
            wholes = rt // denom
            rem = rt - denom * wholes
            result += str(wholes)
            rt -= denom * wholes
            # pr('result')
        else:
            result += "0"
    return result

def findRepeat(s):
    """Look for a repeating pattern"""
    for c in range(len(s)):
        print(s[c:])
        print(s[:-c])
        print()
        if s[c:] == s[:-c]:
            print("found match")
            return s[:c]
    return s

def test():
    # testeql(longDivision(2, 7, 5), 1)
    # testeql(reciprocal(4129, 129), 1)
    # testeql(reciprocal(7, 20), 1)
    # testeql(findRecRepeat(4129), 0)
    # testeql(reciprocal(2, 1), 5)
    findRepeat("142857142857142857142")

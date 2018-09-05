def improperFractionToMixed(a):
    num = a[0]
    den = a[1]

    w = num // den
    nn = num - w * den
    dd = den

    return [w, nn, dd]


def leapYear(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

def lookAndSaySequenceNextElement(element):
    digits = list(map(int, str(element)))
    i = 0
    result = ''
    while i < len(element):
        total = 1
        for j in digits[i+1:]:
            if j == digits[i]:
                total += 1
            else:
                break
        result += str(total) + str(digits[i])
        i += total
    return result
    # too late

    
def removeAdjacent(s):
    
    if s == '':
        return  ... 

    ans = []
    ans.append(s[0])
    for i in range(1, len(s)):
        if s[i] != s[i - 1]:
            ans.append(s[i])

    return ''.join(ans)

    
def test():
    testeql(lookAndSaySequenceNextElement('1211'), None)

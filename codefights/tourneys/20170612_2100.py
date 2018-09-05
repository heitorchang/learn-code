from collections import Counter

def checkEqualFrequency(inputArray):
    c = Counter(inputArray)
    v = c.values()
    return len(set(v)) == 1


def quadraticEquation(a, b, c):
    # does not pass all tests
    det = b * b - 4 * a * c
    if det < 0:
        return []
    elif det == 0:
        return [-b/(2*a)]
    else:
        return [(-b - det ** 0.5)/(2*a), (-b + det ** 0.5)/(2*a)]

def knapsackLight(value1, weight1, value2, weight2, maxW):
    w1 = weight1
    w2 = weight2
    v1 = value1
    v2 = value2
    
    if (w1 + w2) <= maxW:
        return v1 + v2
    elif w1 <= maxW and w2 <= maxW:
        return max(v1, v2)
    elif w1 > w2 and w1 <= maxW:
        return v1
    elif w2 > w1 and w2 <= maxW:
        return v2
    elif w1 > maxW and w2 <= maxW:
        return v2
    elif w2 > maxW and w1 <= maxW:
        return v1
    else:
        return 0


    

def test():
    testeql(checkEqualFrequency([1,2,2,1]), True)

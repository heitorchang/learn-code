def maxDivisor(left, right, divisor):
    for i in range(right, left-1, -1):
        if i % divisor == 0:
            return i

def knapsackLight(value1, weight1, value2, weight2, maxW):
    if weight1 + weight2 <= maxW:
        return value1 + value2
    if max(weight1, weight2) > maxW:
        return value1
    if weight1 <= maxW and (value1 >= value2 or weight2 > maxW):
        return value1
    return value2


def test():
    testeql(maxDivisor(1, 10, 3), 9)
    testeql(knapsackLight(15, 2, 20, 3, 2), 15)

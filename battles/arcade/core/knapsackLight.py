def knapsackLight(value1, weight1, value2, weight2, maxW):
    v1 = value1
    v2 = value2
    w1 = weight1
    w2 = weight2

    if w1 + w2 <= maxW:
        return v1 + v2
    if w1 <= maxW and w2 <= maxW:
        return max(v1, v2)
    if w1 > maxW and w2 > maxW:
        return 0
    if w1 > maxW:
        return v2
    if w2 > maxW:
        return v1

from itertools import combinations

def liquidMixing(densities):
    # Does not pass
    result = [densities[0]]
    for i in range(1, len(densities)):
        for j in range(i + 1):
            if densities[i] <= densities[j]:
                tmp = densities[i]
                for k in range(j + 1, i + 1):
                    densities[k] = densities[k - 1]
                densities[j] = tmp
                if i % 2 == 1:
                    result.append((densities[(i + 1) // 2] +
                                  densities[i // 2]) / 2)
                else:
                    result.append(densities[i // 2])
                break
    return result

def isMonotonousPhail(sequence):
    # partial pass
    if len(sequence) < 2:
        return True
    diff = sequence[1] - sequence[0]
    # pr('diff')
    if diff > 0:
        cur = sequence[1]
        for i in range(2, len(sequence)):
            if sequence[i] - cur <= 0:
                return False
            cur = sequence[i] - cur
            # pr('cur')
    else:
        cur = sequence[1]
        for i in range(2, len(sequence)):
            if sequence[i] - cur >= 0:
                return False
            cur = sequence[i] - cur
    return True

def isMonotonous(sequence):
    decr = True
    for i in range(len(sequence) - 1):
        if sequence[i] >= sequence[i+1]:
            decr = False
    incr = True
    for i in range(len(sequence) - 1):
        if sequence[i] <= sequence[i+1]:
            incr = False
    return decr or incr

def swap(str, a, b):
    lst = list(str)
    lst[a], lst[b] = lst[b], lst[a]
    return ''.join(lst)

def isOneSwapEnough(inputString):
    # does not pass, partial score
    pairs = combinations(range(len(inputString)), 2)
    for p in pairs:
        pr('p')
        swapped = swap(inputString, p[0], p[1])
        pr('swapped')
        if swapped == swapped[::-1]:
            return True
    return False

def test():
    # testeql(liquidMixing([10, 20, 8, 12, 6]), [10, 15, 10, 11, 10])
    # testeql(isMonotonous([1, 4, 5, 7, 9]), True)
    testeql(isOneSwapEnough('abab'), True)

def test():
    testeql(inversePermutation([1,3,4,2]), [1,4,2,3])
    testeql(sortByHeight([-1, 150, 190, 170, -1, -1, 160, 180]), [-1, 150, 160, 170, -1, -1, 180, 190])

def inversePermutation(permutation):
    len_p = len(permutation)
    ts = [(i, v) for (i, v) in zip(range(1, len_p+1), permutation)]
    result = [None for _ in range(len_p)]
    for t in ts:
        result[t[1]-1] = t[0]
    return result

def sortByHeight(a):
    for i in range(len(a)):
        minIndex = -1
        tmp = a[i]
        if a[i] == -1:
            continue
        for j in range(i, len(a)):
            if a[j] != -1:
                if minIndex == -1 or a[j] < a[minIndex]:
                    minIndex = j
        a[i] = a[minIndex]
        a[minIndex] = a[i]
    return a

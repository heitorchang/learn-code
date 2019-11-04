def deconstructSums(prefixSums):
    prefixSums = list(reversed(prefixSums))
    return list(reversed([a - b for (a, b) in zip(prefixSums, prefixSums[1:])] + [prefixSums[-1]]))

def prefixSumsToSuffixSums(prefixSums):
    prefixSums = deconstructSums(prefixSums)
    b = []
    for i in range(len(prefixSums)):
        b.append(sum(prefixSums[i:]))
    return b

def test():
    testeql(prefixSumsToSuffixSums([1, 3, 6, 10, 15]), [15, 14, 12, 9, 5])
    testeql(deconstructSums([1, 3, 6, 10, 15]), [1,2,3,4,5])

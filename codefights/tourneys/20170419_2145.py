from itertools import combinations

def divisorsPairs(sequence):
    s = sorted(sequence)
    total = 0
    for p in combinations(s, 2):
        if p[1] % p[0] == 0:
            total += 1
    return total


def mergeSort(sequence):

    def merge(sequence, left, middle, right):

        result = []

        i = left
        j = middle
        while i < middle and j < right:
            if sequence[i] < sequence[j]:
                result.append(sequence[i])
                i += 1
            else:
                result.append(sequence[j])
                j += 1

        while i < middle:
            result.append(sequence[i])
            i += 1

        while j < right:
            result.append(sequence[j])
            j += 1

        for i in range(left, right):
            sequence[i] = result[i - left]

    def split(sequence, left, right):
        middle = (left + right) // 2

        if left + 1 == right:
            return
        split(sequence, left, middle)
        split(sequence, middle, right)
        merge(sequence, left, middle, right)

    split(sequence, 0, len(sequence))

    return sequence

def test():
    testeql(divisorsPairs([2,4,8]), 3)
    testeql(mergeSort([3, 6, 1, 5, 3, 6]), [1, 3, 3, 5, 6, 6])

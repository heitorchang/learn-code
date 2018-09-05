def inversePermutation(permutation):
    s = list(enumerate(permutation))
    result = [None for _ in range(len(permutation))]
    print(s)
    for elem in s:
        result[elem[1]-1] = elem[0]+1
    return result


def sumOfCoprimes(m):

    ans = 0
    for p in range(2, m + 1):
        a = p
        b = m
        while a > 0:
            tmp = b % a
            b = a
            a = tmp

        if b == 1:
            ans += 1

    return ans

def test():
    testeql(inversePermutation([1,3,4,2]), [1,4,2,3])

    testeql(sumOfCoprimes(5), 9)

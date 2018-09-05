def inversePermutation(permutation):
    a = list(enumerate(permutation, 1))
    b = [0 for _ in range(len(permutation))]
    for elem in a:
        b[elem[1]-1] = elem[0]
    return b

def test():
    testeql(inversePermutation([1,3,4,2]), [1,4,2,3])

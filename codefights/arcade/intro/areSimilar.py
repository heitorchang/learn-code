def areSimilar(A, B):
    if A == B:
        return True
    len_a = len(A)
    equality = [False for _ in range(len_a)]
    for i in range(len_a):
        if A[i] == B[i]:
            equality[i] = True
    falses = equality.count(False)
    if falses != 2:
        return False
    a1_idx = equality.index(False)
    a1 = A[a1_idx]
    b1 = B[a1_idx]
    a2_idx = equality[a1_idx+1:].index(False) + a1_idx + 1
    a2 = A[a2_idx]
    b2 = B[a2_idx]

    return a1 == b2 and a2 == b1

def test():
    testeql(areSimilar([1,2,3],[1,3,2]), True)

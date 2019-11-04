def tripletSum(x, a):
    len_a = len(a)
    for i in range(len_a-2):
        for j in range(i+1, len_a-1):
            for k in range(j+1, len_a):
                pr('i j k')
                if a[i] + a[j] + a[k] == x:
                    return True
    return False

def test():
    testeql(tripletSum(5, [2,3,1]), False)

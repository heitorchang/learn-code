def isSumOfConsecutive2(n):
    total = 0
    for i in range(1, n):
        cur_sum = 0
        for j in range(i, n):
            cur_sum += j
            if cur_sum == n:
                total += 1
                break
            if cur_sum > n:
                break
    return total

def perfectArray(A):
    len_A = len(A)
    is_len = [elem == len_A for elem in A]
    return all(is_len)


def test():
    testeql(isSumOfConsecutive2(9), 2)

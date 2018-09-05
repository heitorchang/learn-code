def array_left_rotation(a, n, k):
    return a[k:] + a[:k]

def main():
    n, k = map(int, input().strip().split(' '))
    a = list(map(int, input().strip().split(' ')))
    answer = array_left_rotation(a, n, k);
    print(*answer, sep=' ')

def test():
    testeql(array_left_rotation([1,2,3,4,5], 5, 4), [5,1,2,3,4])

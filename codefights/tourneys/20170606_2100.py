
def countSumOfTwoRepresentations2(n, l, r):
    tot = 0
    for a in range(l, r+1):
        for b in range(a, r+1):
            if a + b == n:
                tot += 1
    return tot

def firstNotDivisible(divisors, start):
    answer = start
    while True:
        correct = True
        for i in range(0, len(divisors)):
            if answer % divisors[i] == 0:
                correct = False
                break
        if correct:
            return answer
        answer += 1


def test():
    testeql(firstNotDivisible([2,3,4], 14), 17)

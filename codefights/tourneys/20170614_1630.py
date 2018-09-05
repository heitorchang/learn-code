def reverseToSort(inputArray):
    for a in range(len(inputArray) - 1):
        for b in range(a+1, len(inputArray) + 1):
            window = inputArray[a:b]
            pr('window')
            if sorted(inputArray) == inputArray[:a] + window[::-1] + inputArray[b:]:
                return len(set(inputArray)) == len(inputArray)
    return False


def factor(n):
    totaldivs = 0
    for i in range(1, n+1):
        if n % i == 0:
            totaldivs += 1
    return totaldivs
    
def divNumber(k, l, r):
    tot = 0
    for i in range(l, r+1):
        t = factor(i)
        if t == k:
            tot += 1
    return tot

def test():
    # testeql(reverseToSort([19,32,23]), True)
    testeql(factor(25), 3)

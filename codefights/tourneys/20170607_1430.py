
def maxFraction(numerators, denominators):
    fl = []
    maxIndex = 0
    maxval = 0
    for i in range(len(numerators)):
        rat = numerators[i]/denominators[i]
        if maxval < rat:
            maxval = rat
            maxIndex = i
    return maxIndex

def alphabetSubsequence(s):
    o = ord(s[0])
    for c in s[1:]:
        pr('c ord(c)')
        if ord(c) <= o:
            return False
        o = ord(c)
    return True



def graphEdges(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    tot = 0

    # count all Trues
    return tot // 2

def sortByLength(inputArray):
    return sorted(inputArray, key=lambda w: len(w))


def firstMultiple(divisors, start):

    answer = start + 1
    while True:
        correct = True
        for i in range(len(divisors)):
            if answer % divisors[i] != 0:
                correct = False
                break
        if correct:
            return answer
        answer += 1


    

def test():
    testeql(alphabetSubsequence("effg"), False)
    testeql(firstMultiple([2,3,4], 13), 24)

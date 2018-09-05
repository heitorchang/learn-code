
def countWaysToChangeDigit(value):
    tot = 0
    while value > 0:
        tot += 9 - value % 10
        value //= 10
    return tot

def isMAC48Address(inputString):

    for i in range(len(inputString)):
        if i % 3 == 2:
            if inputString[i] != '-':
                return False
        else:
            sym = inputString[i]
            if not ('0' <= sym and sym <= '9' or 'A' <= sym and sym <= 'F'):
                return False

    return len(inputString) == 17


def arrayMode(sequence):
    count = []
    answer = 0

    for i in range(1000):
        count.append(0)
    for i in range(len(sequence)):
        count[sequence[i] - 1] += 1
        if count[sequence[i] - 1] > count[answer]:
            answer = sequence[i] - 1
    return answer + 1


def properOrImproper(a):
    pass

def combs(comb1, comb2):

    def getMask(comb):
        return int(chars.replace('*', '1').replace('.', '0'), 2)

    m1 = getMask(comb1)
    m2 = getMask(comb2)
    len1 = len(comb1)
    len2 = len(comb2)
    answer = len1 + len2
    for i in range(-len1, len2 + 1):
        if i < 0:
            tmp = m2 << (-i) & m1
            length = max(-i + len2, len1)
        else:
            tmp = m1 << i & m2
            length = max(i + len1, len2)
        if tmp == 0 and answer > length:
            answer = length

    return answer


def test():
    #testeql(countWaysToChangeDigit(10), 17)
    #testeql(isMAC48Address("00-1B-63-84-45-E6"), True)
    #testeql(arrayMode([1,3,3,3,1]), 3)

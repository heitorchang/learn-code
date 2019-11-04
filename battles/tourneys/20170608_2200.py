def splitByValue(k, elements):
    left = []
    right = []
    for c in elements:
        if c < k:
            left.append(c)
        else:
            right.append(c)
    return left + right


def sumUpDigits(inputString):

    answer = 0

    for i in range(len(inputString)):
        if '1' < inputString[i] and inputString[i] < '9':
            answer += ord(inputString[i]) - ord('0')

    return answer

def theJanitor(word):
    res = [0 for i in range(26)]
    for i in range(26):
        c = chr(97 + i)
        left = word.find(c)
        if left >= 0:
            right = word.rfind(c)
            res[i] = right - left + 1
            
    return res

def fib(n):
    a = [1, 1]
    whil

def fibonacciSum(n):


def test():
    # testeql(sumUpDigits("2 apples, 12 oranges"), 5)
    # testeql(theJanitor("abacaba"), [7,5,1,0,0])

from itertools import combinations

def binaryGenerator(s):
    n = int(s, 2)
    len_s = len(s)
    limit = 2 ** len(s)

    result = []
    for i in range(limit):
        if i & n == n:
            result.append(bin(i)[2:].zfill(len_s))
    return sorted(result)
    
    

def binaryGeneratorFail(s):
    lst = list(s)
    # get indices of zeros
    zeros = []
    result = []
    for i in range(len(lst)):
        if lst[i] == '0':
            zeros.append(i)
    pr('zeros')
    for i in range(1, len(zeros)+1):
        combos = list(combinations(zeros, i))
        toAdd = lst[:]
        pr('toAdd combos')
        for j in combos:
            pr('j')
            for idx in j:
                toAdd[idx] = "1"
            result.append("".join(toAdd))
    return sorted(result)

def test():
    testeql(binaryGenerator("01101"), ["01101", 
 "01111", 
 "11101", 
 "11111"])
    testeql(binaryGenerator("10010111"), ["10010111", 
 "10011111", 
 "10110111", 
 "10111111", 
 "11010111", 
 "11011111", 
 "11110111", 
 "11111111"])

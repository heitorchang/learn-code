import re

def fact(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def nCr(n, r):
    if n == r:
        return 1
    if n < r:
        raise ValueError("n less than r, something is not right.")
    return fact(n) / (fact(r) * (fact(n-r)))

def nextBin(s):
    """Advance a bit to the next largest number"""
    # print(s)
    len_s = len(s)
    idx = s.rfind('01')
    if s[-1] == '0':
        # push all remaining bits right
        ones_to_push = s[idx+2:].count('1')
        # print('push', ones_to_push)
        
        return s[:idx] + '10' + '0' * (len_s - idx - 2 - ones_to_push) + '1' * ones_to_push
    else:
        return s[:idx] + '10' + s[idx+2:]

def wrapper():
    count = 0
    
        
def detectBlock(s):
    print(s)
    ones = s.count('1')
    p_first = re.compile("^1+0*$")
    if p_first.match(s):
        return nCr(len(s), ones)
    
    p = re.compile("^10+(1+)$")
    m = p.match(s)
    
    if m:
        print('match p', m)
        return 1
        
    else:
        p2 = re.compile("^1+0+(1[01]*)")
        m2 = p2.match(s)
        if m2:
            print('match p2', m2.groups()[0])
            return 1+ detectBlock(m2.groups()[0])

d="""
100011
100101
100110
101001
101010
101100
110001
110010
110100
"""

def testsub():
    testeql(detectBlock("10110100"), 19)
    testeql(detectBlock("10101110"), 6)
    testeql(detectBlock("110100"), 9)
    
def recurseBlock(s):
    pass

def totalSameOnes(k):
    # exceeds time limit
    
    s = bin(k)[2:]
    ones = s.count('1')
    if ones == 1:
        return len(s)
    if ones == len(s):
        return 1

    n = detectBlock(s)
    print('n', n)
    
    #subs_min = '1' + '0' * (len(s)-ones) + '1' * (ones-1)
    #subs_min_n = int(subs_min, 2)

    #possibleSubs = 0
    #while int(subs_min, 2) <= k:
    #    possibleSubs += 1
    #    subs_min = nextBin(subs_min)
    
    allSmaller = 0
    for i in range(ones, len(s)):
        possible = nCr(i-1, ones-1)
        allSmaller += possible

    return n + allSmaller
    # return possibleSubs + allSmaller
    
def test():
    # testeql(totalSameOnes(23), 2)
    # testeql(totalSameOnes(184), totalSameOnesX(184))
    testeql(totalSameOnes(27), 3)
    # testeql(detectBlock("10110100"), 19)
    
    # testeql(totalSameOnes(7), 1)
    # testeql(totalSameOnes(1), 1)
    # testeql(totalSameOnes(8), 4)
    # testeql(totalSameOnes(9999), 1548)

def alex(k):
    s = bin(k)[2:]
    print(s)
    nearest_s = '1' + '0' * (len(s)-1)
    nearest = int(nearest_s, 2)
    print(nearest)
    diff = k - nearest
    diff_s = bin(diff)[2:]
    print(diff_s)
    
    c = """
1000 0111 135 1
1000 1011 139 2 
1000 1101 141 3
1000 1110 142 4 

1001 0011 147 5
1001 0101 149 6
1001 0110 150 7 
1001 1001 153 8
1001 1010 154 9
1001 1100 156 10

10100011 163
10100101 165

pattern: 

10000111 135 192

10001011 139
10001101 141
10001110 142

10010011 147
10010101 149
10010110 150
10011001 153
10011010 154
10011100 156

10100011 163
10100101 165
10100110 166
10101001 169
10101010 170
10101100 172
10110001 177
10110010 178
10110100 180
10111000 184 211

    
    110001
    110010
    110100
"""
def binloop(a, stop):
    ia = int(a, 2)
    istop = int(stop, 2)
    
    while ia <= istop:
        print(a, ia)
        a = nextBin(a)
        ia = int(a, 2)
    

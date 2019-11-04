import re

def fact(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

def ncr(n, r):
    if n == r:
        return 1
    if n < r:
        raise ValueError("n less than r, something is not right.")
    return fact(n) / (fact(r) * (fact(n-r)))

def countLowerThan(s):
    # s = bin(k)[2:]
    len_s = len(s)
    ones = s.count('1')
    print()
    print(s, int(s, 2), 's')

    p_nothing_to_do = re.compile(r'^10+1+$')
    if p_nothing_to_do.search(s):
        return 1
    
    lower = '1' + '0' * (len(s)-ones) + '1' * (ones-1)
    print('  ', lower, 'low')
    # print()
    # ct = binloop(lower, s)
    # print("BINLOOP CT", ct)  # 792

    p_shortcut = re.compile(r'^10+(1+0+)$')
    m_shortcut = p_shortcut.search(s)
    if m_shortcut:
        print("SHORTCUT")
        shortcut_s = m_shortcut.groups()[0]
        print(shortcut_s, "Shortcut s")
        shortcut_ones = shortcut_s.count('1')
        print(len(shortcut_s))
        return ncr(len(shortcut_s), shortcut_ones)

    # p_end = re.compile(r'1+0+$')
    # p_end = re.compile(r'^.*?101+0+$')
    p_end = re.compile(r'10+1+0+$')
    m = p_end.search(s)
    if m:
        ms = m.group()
        len_ms = len(ms)
        left = s[:m.span()[0]]
        left_ones = left.count('1')
        print('P_END left', left)
        print('P_END ms', ms)
        m_ones = ms.count('1')
        p_shuf = re.compile(r'1+0+$')
        m_shuf = p_shuf.search(ms)
        shuf = m_shuf.group()
        shuf_ones = shuf.count('1')
        # ct = ncr(len_ms, m_ones)
        ct = ncr(len(shuf), shuf_ones)
        print('ct', ct)
        # 10011011111000 9976
        # 10010111111000 9720
        t99999 = """
        11000010111111100 99836 *
        11000011000111111 99903 7
        11000011001011111 99935 6 
        11000011001101111 99951 5 
        11000011001110111 99959 4
        11000011001111011 99963 3
        11000011001111101 99965 2
        11000011001111110 99966 1
        """

        t_random = """
        ... (4)
        1100111001110 6606
        1100110111100 6588  next
        110011
        
        """
        # next = '1' * (left_ones - 1) + '0' + '1' * (ones-left_ones+1) + '0' * (len_s - ones - 1)

        next = left + '0' + '1' * (ones - left_ones)
        len_next = len(next)
        next += '0' * (len_s - len_next)
        print(next, 'next')
        return ct + countLowerThan(next)
        # return 0
    
    p_ends_in_one = re.compile(r'10+1+$')
    m_ends_in_one = p_ends_in_one.search(s)
    if m_ends_in_one:
        new_right = prevBin(m_ends_in_one.group())
        next = s[:m_ends_in_one.span()[0]] + new_right
        print(next, int(next, 2), 'NEXT ENDS IN ONE')
        return 1 + countLowerThan(next)
        # return 0
    
    print("GOT HERE, ERROR")
    print(s)

def testCount():
    k = int('111010', 2)
    k = int('111001', 2)
    #k = int('110110', 2)
    k = int('100101110', 2)
    # testeql(countLowerThan(bin(k)[2:]), 8)
    k = int('1100111001110', 2)
    testeql(countLowerThan(bin(k)[2:]), 0)
    
def totalSameOnes(k):
    s = bin(k)[2:]
    ones = s.count('1')
    if ones == 1:
        return len(s)
    if ones == len(s):
        return 1

    n = countLowerThan(s)
    print('n', n)
    
    allSmaller = 0
    for i in range(ones, len(s)):
        possible = ncr(i-1, ones-1)
        allSmaller += possible

    print('allSmaller', allSmaller)
    return n + allSmaller
    
def test():
    # testeql(totalSameOnes(23), 2)
    # k = int('111010', 2)
    # testeql(totalSameOnes(k), totalSameOnesX(k))
    # testeql(totalSameOnes(27), 3)
    testeql(totalSameOnes(99999), totalSameOnesX(99999))
    testeql(totalSameOnes(9999), totalSameOnesX(9999))
    #k = int('11000110', 2)
    #testeql(totalSameOnes(k), totalSameOnesX(k))

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

def prevBin(s):
    len_s = len(s)
    idx = s.find('10')
    ones = s.count('1')
    result = '01' + '1' * (ones - 1) + '0' * (len_s - ones - 1)
    return result

def binloop(a, stop):
    ct = 0
    ia = int(a, 2)
    istop = int(stop, 2)
    
    while ia <= istop:
        print(a, ia, ct)
        a = nextBin(a)
        ia = int(a, 2)
        ct += 1
    return ct
    

def detectBlock(s):
    print(s)
    ones = s.count('1')
    p_first = re.compile("^1+0*$")
    if p_first.match(s):
        return ncr(len(s), ones)
    
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

def totalSameOnesX(k):
    s = bin(k)[2:]
    ones = s.count('1')
    if ones == 1:
        return len(s)
    if ones == len(s):
        return 1

    subs_min = '1' + '0' * (len(s)-ones) + '1' * (ones-1)
    subs_min_n = int(subs_min, 2)

    possibleSubs = 0
    while int(subs_min, 2) <= k:
        possibleSubs += 1
        subs_min = nextBin(subs_min)
    
    allSmaller = 0
    for i in range(ones, len(s)):
        possible = ncr(i-1, ones-1)
        allSmaller += possible

    return possibleSubs + allSmaller

t = """
10011011011100 9948
10011011100011 9955
10011011100101 9957
10011011100110 9958
10011011101001 9961
10011011101010 9962
10011011101100 9964
10011011110001 9969
10011011110010 9970
10011011110100 9972
10011011111000 9976
10011100001111 9999
"""

t99999 = """
11000010111111100 99836 *
11000011000111111 99903 7
11000011001011111 99935 6 
11000011001101111 99951 5 
11000011001110111 99959 4
11000011001111011 99963 3
11000011001111101 99965 2
11000011001111110 99966 1
"""

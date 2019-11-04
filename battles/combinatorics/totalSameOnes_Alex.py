import math

def nCr(n,r):

    f = math.factorial
    return f(n) / f(r) / f(n-r)

def totalSameOnes(n):
    # count bits in n
    c = bin(n).count('1')
    
    # get largest power of 2 not greater than n
    k = 0
    while 2**k<= n:
        k += 1
    k = k-1
    
    #if n is a power of 2, return that power plus 1
    if 2**(k) ==n:
        return k+1
    
    # if number of 1s is equal to the closest power +1, this means all of the numbers are 1s and the answer is 1
    if k+1 == c:
        return 1
    
    # start real calculations here...
    # add n choose k to the 
    #
    print('k', k)
    total = 0
    ntok = n
    toadd = 0
    i = 1
    while ntok >=c:

        if c ==0:
            total +=1
            break
      
        
        
        k =0
        while 2**k< ntok:
            k += 1
            
        k = k-1
        
        if k ==0:
            total +=1
            break
        if k <c:
            
            break
       
        total+=nCr(k,c)
       
        
        toadd += 2**k
        ntok = n - toadd

        if ntok < 0:
            
            break
        c = c-1
        i += 1
    
            
    return total +1
    
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

def test():
    testeql(totalSameOnes(23), 2)
    # testeql(totalSameOnes(99999), totalSameOnesX(99999))
    # testeql(totalSameOnes(9999), totalSameOnesX(9999))

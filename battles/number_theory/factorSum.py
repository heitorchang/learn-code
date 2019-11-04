# somehow my solution fails

# good solution

def factorSumGood(n):
    n1=n
    while True:
        s=0
        k=2
        while n>1:
            while n%k==0:
                n//=k
                s+=k
            k+=1
        # print(s)
        if s==n1:
            return s
        if isp(s):
            return s 
        else:
            n=s

def isp(n):
    k=2
    while k<n:
        if n%k==0:
            return False
        k+=1
    return True


# my solution

def factorize(n):
    ans = []
    while n > 1:
        for trial in range(2, n+1):
            if n % trial == 0:
                ans.append(trial)
                n //= trial
                break
    return ans

def factorSumBad(n):
    if n <= 3:
        return n
    factsum = 0
    while True:
        
        factsum = sum(factorize(n))
        if n == factsum:
            return n
        n = factsum
        # print(n)

def tester():
    for n in range(1, 1000):
        good = factorSumGood(n)
        bad = factorSumBad(n)
        if good != bad:
            print(n)

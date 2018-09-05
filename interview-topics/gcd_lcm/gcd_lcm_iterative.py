def gcd_iter(a, b):
    limit = min(a, b)
    for n in range(limit, 0, -1):
        if a % n == 0 and b % n == 0:
            return n
    return 1

def lcm_iter(a, b):
    begin = min(a, b)
    for n in range(begin, a * b + 1):
        if n % a == 0 and n % b == 0:
            return n
    return 0


# a bit more intelligent

def lcm_step(a, b):
    left, right = a, b
    while left != right:
        if left < right:
            left += a
        else:
            right += b
    return left

def gcd_mod(a, b):
    # let a > b
    if a < b:
        a, b = b, a
    if b == 0:
        return a
    return gcd_mod(b, a % b)
        

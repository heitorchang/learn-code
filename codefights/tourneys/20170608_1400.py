
def isLucky(n):
    digits = list(map(int, str(n)))
    length = len(digits)
    left = digits[:length//2]
    right = digits[length//2:]
    return sum(left) == sum(right)
    

def test():
    testeql(isLucky(1230), True)
        

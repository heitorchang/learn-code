import re

def test():
    testeql(increaseNumberRoundness(902200100), True)
    testeql(increaseNumberRoundness(11000), False)

def increaseNumberRoundness(n):
    p = re.compile(r'0[1-9]+0*$')
    m = p.search(str(n))
    if m:
        return True
    return False
    

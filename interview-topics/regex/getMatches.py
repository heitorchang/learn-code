import re

# remember to use raw strings: r"[0-9]+"

def getBeginningDigits(s):
    """Given s, find longest substring of digits, starting from the left"""
    p = re.compile(r"^\d+")  # same as ^[0-9]+
    it = p.finditer(s)
    try:
        return next(it).group()
    except StopIteration:
        return ""

def getAllMatches(s):
    """Find all (longest) sequences of digits in s"""
    p = re.compile(r"\d+")
    return p.findall(s)
    
def test():
    testequal(getBeginningDigits("12345ace"), "12345")
    testequal(getBeginningDigits("Ab12"), "")
    testequal(getAllMatches("a12zz399p87"), ['12', '399', '87'])
    testequal(getAllMatches("no digits"), [])

import re

def test():
    testeql(lastDigitRegExp('var_1_i'), "1")
    testeql(lastDigitRegExp('1'), "1")

def lastDigitRegExpRE(inputString):
    p_end = re.compile('[0-9]$')
    m_end = p_end.search(inputString)
    if m_end:
        return inputString[-1]
    p = re.compile('([0-9]).+$')
    m = p.search(inputString)
    return m.groups()[0]

def lastDigitRegExp(inputString):
    rev = inputString[::-1]
    for i in range(len(rev)):
        c = rev[i]
        if c in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
            return c

import re

def replaceCharsWithSpace(s, patToRemove):
    return re.sub(patToRemove, ' ', s)

def test():
    testeql(replaceCharsWithSpace("a@#b", r'[^A-Za-z0-9]'), "a  b")

import re

def longestWord(text):
    # remove non alpha
    p = re.compile('[^\w\s]')
    s = p.sub(' ', text)
    words = s.split()
    return sorted(words, key=len)[-1]

def test():
    testeql(longestWord("ready, steady, go!"), "steady")

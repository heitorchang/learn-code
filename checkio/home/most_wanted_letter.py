from collections import Counter

def checkio(text):
    ctr = Counter(''.join([c for c in text.lower() if c.isalpha()]))
    maxCount = max(ctr.values())
    mostCommonLetters = [e for e, count in ctr.items() if count == maxCount]
    return list(sorted(mostCommonLetters))[0]

def test():
    testeql(checkio("One"), "e")

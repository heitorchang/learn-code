def unusualLexOrder(words):
    reg = [w[::-1] for w in words]
    s = sorted(reg)
    return [w[::-1] for w in s]



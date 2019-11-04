def baseConversion(n, x):
    return hex(int(n, x))[2:]

def test():
    testeql(baseConversion("1302", 5), "ca")

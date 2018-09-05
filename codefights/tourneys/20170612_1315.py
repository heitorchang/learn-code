def arrayPacking(a):
    bitstr = ""
    for n in a:
        bb = bin(n)[2:]
        bitstr = bb.zfill(8) + bitstr
    return int(bitstr, 2)


def test():
    testeql(arrayPacking([24,85,0]), 21784)

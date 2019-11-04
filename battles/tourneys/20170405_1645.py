def test():
    testeql(pointInLine([10, 7], [1, 0, -10]), False)

def pointInLine(point, line):
    ptx = point[0]
    pty = point[1]

    x = line[0]
    y = line[1]
    eq = line[2]

    return (ptx * x + pty * y) == -eq

# 12345
#  9-5 = 4
# + 9-4
def countWaysToChangeDigit(value):
    total = 0
    digits = list(str(value))
    pr('digits')
    for d in digits:
        dd = int(d)
        total += 9 - dd
    return total

def areaPos(xa, ya, xb, yb, xc, yc):
    return (0.5 * abs(xa*yb + xb*yc + xc*ya - xa*yc - xc*yb - xb*ya)) > 1e-5

def countTriangles(x, y):
    pts = range(len(x))
    verts = combinations(pts, 3)
    total = 0
    for v in verts:
        if areaPos(x[v[0]], y[v[0]], x[v[1]], y[v[1]], x[v[2]], y[v[2]]):
            total += 1
    return total

def test():
    testeql(countTriangles([0, -1, -2], [0, -2, -4]), 0)

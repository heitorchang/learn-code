from itertools import product

m = int(1e9+7)
def trySubst(s):
    try:
        left, right = s.split("=")
        base, expt = map(int, left.split("^"))
        p = pow(base, expt, m)
        # print(p)
        return p == int(right)
    except ValueError:
        return False

def TTYPaperTape3(t):
    numsp = t.count("_")

    digs = [""] + list(map(str, range(10)))

    t = t.replace("_", "{}")
    
    for vals in product(digs, repeat=numsp):
        if ''.join(vals) != '' and int(''.join(vals)) > 0:
            if trySubst(t.format(*vals)):
                return int(''.join(vals))

    

test(
    TTYPaperTape3(" _^ _ = 9"), 32,
    TTYPaperTape3("_ ^ _ _ = 25"), 52,
    TTYPaperTape3("_0 ^ 2 = _00"), 11,
)

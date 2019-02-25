from itertools import product

m = int(1e9+7)
digs = [' '] + list(map(str, range(10)))

def repl(eq, vals):
    return eq.format(*vals)

def substInto(eq, vals):
    ff = eq.replace("_", "{}")
    return ff.format(*map(str, vals))

    
def pick(real, missing):
    ct = missing.count("{}")

    # __1_
    # _1_02
    # 2102
    # 1202

    for p in product(digs, repeat=ct):
        try:
            if int(missing.format(*p)) == real:
                return ''.join(p).strip()
        except:
            pass
    

def TTYPaperTape3(t):
    t = t.replace("_", "{}")

    # split base, expt and rt (right)

    left, right = t.split("=")
    base, expt = left.split("^")

    basesp = base.count("{}")
    exptsp = expt.count("{}")
    rightsp = right.count("{}")

    valright = set()
    
    for r in product(digs, repeat=rightsp):
        curr = repl(right, r)
        try:
            currint = int(''.join(curr))
        except:
            continue
        valright.add(currint)

    valright.discard(0)

    valbase = []
    for b in product(digs, repeat=basesp):
        curb = repl(base, b)
        try:
            curbint = int(''.join(curb))
        except:
            continue
        valbase.append(curbint)

    valexpt = []
    for e in product(digs, repeat=exptsp):
        cure = repl(expt, e)
        try:
            cureint = int(''.join(cure))
        except:
            continue
        valexpt.append(cureint)

    valbase = [b for b in valbase if b > 0]
    valexpt = [b for b in valexpt if b > 0]

    works = set()
    

    for b in valbase:
        found = False
        for e in valexpt:
            pp = pow(b, e, m)
            if pp in valright:
                bans = b
                eans = e
                rans = pp
                found = True
                break
        if found:
            if basesp:
                bi = pick(bans, base)
            else:
                bi = ""

            if exptsp:
                ei = pick(eans, expt)
            else:
                ei = ""

            if rightsp:
                ri = pick(rans, right)
            else:
                ri = ""
            works.add(int(bi + ei + ri))
            found = False
    return min(works)

    """
test(
    TTYPaperTape3(" _^ _ = 9"), 32,
    TTYPaperTape3("_ ^ _ _ = 25"), 52,
    TTYPaperTape3("_0 ^ 2 = _00"), 11,
    TTYPaperTape3(" 3_^2=1_2_"), 204,

    
)
"""

test(
    TTYPaperTape3("_1 ^ __ = 1_1"), 122,
    TTYPaperTape3("_ ^_ _ = 25"), 52,
    )

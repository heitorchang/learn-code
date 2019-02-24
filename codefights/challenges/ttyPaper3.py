def eqdig(r, m):
    return ''.join([d for d, e in zip(str(r), m) if d != e])




from itertools import product

m = int(1e9+7)
digs = [''] + list(map(str, range(10)))
       

def repl(eq, vals):
    return eq.format(*vals)

def substInto(eq, vals):
    ff = eq.replace("_", "{}")
    # print(ff.format(*map(str, vals)))
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
                return ''.join(p)
        except:
            pass
    

def TTYPaperTape3(t):
    print(t)
    t = t.replace(" ", "")
    
    numsp = t.count("_")

    digs = [""] + list(map(str, range(10)))

    t = t.replace("_", "{}")

    # split base, expt and rt (right)

    left, right = t.split("=")
    base, expt = left.split("^")

    basesp = base.count("{}")
    exptsp = expt.count("{}")
    rightsp = right.count("{}")

    maxbase = int(repl(base, ['9'] * basesp))

    maxexpt = int(repl(expt, ['9'] * exptsp))


    minright = int(repl(right, ['0'] * rightsp))
    maxright = int(repl(right, ['9'] * rightsp))

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


    for b in valbase:
        found = False
        for e in valexpt:
            pp = pow(b, e, m)
            if pp in valright and b + e > 0:
                bans = b
                eans = e
                rans = pp
                found = True
                break
        if found:
            break

    # print(str(bans) + "^" + str(eans) + "=" + str(rans))
    # print("Base,expt,r", base, expt, right)

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

    return int(bi + ei + ri)
    

test(
    TTYPaperTape3(" _^ _ = 9"), 32,
    TTYPaperTape3("_ ^ _ _ = 25"), 52,
    TTYPaperTape3("_0 ^ 2 = _00"), 11,
    TTYPaperTape3(" 3_^2=1_2_"), 204,

    
)


test(

    pick(2102, "{}1{}02"), '2',
    pick(1202, "{}1{}02"), '2',

    )

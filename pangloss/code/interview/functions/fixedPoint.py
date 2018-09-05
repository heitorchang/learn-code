def fixedPoint(f, x):
    prev = x
    trial = f(x)
    while abs(trial - prev) > 0.0001:
        prev = trial
        trial = f(trial)
    return trial

def fixedSqrt(x):
    return fixedPoint(lambda y: 0.5 * (x/y + y), x)

def test():
    testeql(round(fixedSqrt(2), 3), 1.414)

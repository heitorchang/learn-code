def wr(ms, msForW, unit, addUnit):
    # Compute whole and remainder
    wUnits = ms // msForW
    rem = ms - wUnits * msForW
    if addUnit:
        wStr = str(wUnits) + unit
    else:
        wStr = str(wUnits)
    return (wStr, rem)

def fit(fmt, ms):
    if fmt[0] == '%':
        addUnit = True
        fmt = fmt[1:]
    else:
        addUnit = False
        
    if fmt == "y":
        return wr(ms, 1000 * 60 * 60 * 24 * 365, "y", addUnit)
    elif fmt == "d":
        return wr(ms, 1000 * 60 * 60 * 24, "d", addUnit)
    elif fmt == "h":
        return wr(ms, 1000 * 60 * 60, "h", addUnit)
    elif fmt == "m":
        return wr(ms, 1000 * 60, "m", addUnit)
    elif fmt == "s":
        return wr(ms, 1000, "s", addUnit)
    elif fmt == "ms":
        return wr(ms, 1, "ms", addUnit)
    else:
        return "ERR"

def timeFormat(value, f):
    if f == "":
        f = "%y %d %h %m %s %ms"
    result = ""
    elems = f.split()
    rem = value
    for elem in elems:
        curStr, rem = fit(elem, rem)
        result += curStr + " "
    return result.strip()
    
def test():
    testeql(fit("%y", 1000), ('0y', 1000))
    testeql(timeFormat(31626061001, ""), "1y 1d 1h 1m 1s 1ms")

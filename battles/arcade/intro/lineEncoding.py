def encode(char, ct):
    if ct > 1:
        return str(ct) + char
    else:
        return char

def lineEncoding(s):
    curChar = s[0]
    curCt = 1
    out = ""
    for i in range(1, len(s)):
        if s[i] == curChar:
            curCt += 1
        else:
            out += encode(curChar, curCt)
            curChar = s[i]
            curCt = 1
    out += encode(curChar, curCt)
    return out

def altW(w):
    r = ""
    m = []
    for c in w:
        if c.isupper():
            m.append(1)
        else:
            m.append(0)
    w = w[::-1]
    for i in range(len(m)):
        if m[i] == 1:
            r += w[i].lower()
        else:
            r += w[i].upper()
    return r

def reverseInverse(s):
    r = ""
    ws = we = None
    for i in range(len(s)):
        c = s[i]
        if c.isalnum():
            if ws is None:
                ws = i
                we = i+1
            else:
                we += 1
        else:
            if ws is not None:
                r += altW(s[ws:we])
                ws = we = None
            r += c
    return r

def test():
    testeql(reverseInverse("First question: How do CodeBots work?"), "tSRIF NOITSEUQ: wOH OD sTOBeDOC KROW?")
    testeql(reverseInverse("Hey, What's Up!"), "yEH, tAHW'S pU!")

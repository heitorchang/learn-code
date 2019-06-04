from textwrap import wrap

def codesignalify(s):
    c = cvt(s)
    print("{}".format(c).replace("'", '"'))

def cvt(s):
    ans = ""
    s = s.lower()
    for c in s:
        if c.isalpha() or c.isspace():
           ans += c
    return wrap(ans)

"""
all human beings are born free and equal in dignity and rights they
are endowed with reason and conscience and should act towards one
another in a spirit of brotherhood
"""

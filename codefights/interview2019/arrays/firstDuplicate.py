def firstDuplicate(a):
    s = set()
    for e in a:
        if e in s:
            return e
        s.add(e)
    return -1

def caucusRace(v):
    SUM = sum(v)
    i = len(v)-1
    s = 0
    while i >= 0:
        v[i] += s
        s = 0 if v[i] > 0 else v[i]
        i -= 1
        
    result = []
    i = 0 
    while SUM > 0:
        if v[i] > 0:
            result += [i]
            SUM -= v[i]
        i += 1
        
    return result

def test():
    testeql(caucusRace([-1, 4, -1, 3, -2, 2, 2, -3, 1, 3, -2]), [1,3,5,8])

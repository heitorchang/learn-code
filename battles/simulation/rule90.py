# Cellular automata rule 90 (sierpinski triangle)

def n(c):
    # next cell, given cells c
    z = ["000", "101", "010", "111"]  # give zero
    if c in z:
        return '0'
    else:
        return '1'

def rule90(s, t):  # seed, iterations
    a = [s]  # answer
    for i in range(t):
        r = ""  # row
        for j in range(len(s)):
            if j == 0:
                c = s[-1] + s[:2]  # cells
            elif j == len(s) - 1:
                c = s[-2:] + s[0]
            else:
                c = s[j-1:j+2]
            r += n(c)
        a += [r]
        s = r
    return a
            

test(rule90("000010000", 5), ["000010000", 
 "000101000", 
 "001000100", 
 "010101010", 
 "100000001", 
 "110000011"])

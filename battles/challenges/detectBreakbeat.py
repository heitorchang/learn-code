def q2(w):
    z = w // 4
    return z

def q4(w):
    z = w // 4
    return 3 * z

def e4(w):
    z = w // 8
    return 3 * z

def e6(w):
    z = w // 8
    return 5 * z

# [][][][][][]0][][][][][][][][][]
# 0       4       8       12

# [0 ][  ][  ][1 ][  ][1 ][  ][  ]

def detectBreakbeat(p):
    N = p.split()
    if len(N) < 8:
        return False
    
    i1 = N[0]
    x = len(N)

    Q2 = q2(x)
    Q4 = q4(x)

    E4 = e4(x)
    E6 = e6(x)

    i2 = N[Q2]

    if i1 == i2:
        return False
        
    if i1 == "~" or i2 == "~":
        return False

    if N[Q2] != N[Q4]:
        return False

    if N[E4] == i1 or N[E6] == i1:
        return True

    return False

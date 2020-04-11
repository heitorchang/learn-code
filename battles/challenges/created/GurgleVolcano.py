import numpy as np
from scipy import sparse
from itertools import chain
from scipy.sparse.csgraph import dijkstra

def GurgleVolcano(floor, hp):
    rows = len(floor)
    cols = len(floor[0])

    floorstr = "".join(chain(*floor))

    lenfl = len(floorstr)

    # sanity
    assert rows * cols == lenfl
    assert floorstr.count("S") == 1
    assert floorstr.count("F") == 1
    
    row_ind = []
    col_ind = []
    data = []

    def isLava(i):
        if floorstr[i] == "L":
            return 1
        return 0

    def below(i):
        return i + cols

    def above(i):
        return i - cols

    def left(i):
        return i - 1

    def right(i):
        return i + 1
    
    def addData(r, c):
        row_ind.append(r)
        col_ind.append(c)
        data.append(isLava(c))

    for i in range(lenfl):
        if i == 0:  # top left
            addData(0, right(i))
            addData(0, below(i))
        elif i == cols - 1: # top right
            addData(i, left(i))
            addData(i, below(i))
        elif i == lenfl - cols:  # bottom left
            addData(i, above(i))
            addData(i, right(i))
        elif i == lenfl - 1:  # bottom right:
            addData(i, left(i))
            addData(i, above(i))
        elif 1 <= i <= cols - 2:  # top
            addData(i, left(i))
            addData(i, right(i))
            addData(i, below(i))
        elif i % cols == 0:  # left
            addData(i, above(i))
            addData(i, right(i))
            addData(i, below(i))
        elif i % cols == cols - 1:  # right
            addData(i, above(i))
            addData(i, left(i))
            addData(i, below(i))
        elif lenfl - cols + 1 <= i <= lenfl - 2:  # bottom
            addData(i, above(i))
            addData(i, left(i))
            addData(i, right(i))
        else:  # center
            addData(i, above(i))
            addData(i, left(i))
            addData(i, right(i))
            addData(i, below(i))

    rp = np.array(row_ind)
    cp = np.array(col_ind)
    dp = np.array(data)

    print()
    print(len(rp), len(cp), len(dp))

    mat_coo = sparse.coo_matrix((dp, (rp, cp)))
    
    d = dijkstra(mat_coo)
    print(d)
    # find S and F

    sloc = floorstr.index('S')
    floc = floorstr.index('F')
    
    dmg = int(d[sloc][floc])
        
    return max(1, hp - dmg)

    
case1 = ["SLL",
         "LGF"]


case2 = ["LLLLLLL",
         "LLLLLLF",
         "SLGLLLL",
         "LLGGGGG"]

case3 = ["LLLLLLLLLLL",
         "SLLLLLLLLLL",
         "LLLLLLLLLLF"]

# snake G
case4 = ["LSLLLLLL",
         "LGLGGGLL",
         "LGLGLGLL",
         "LGLGLGLL",
         "LGGGLGLL",
         "LLLLLLFL"];

case5 = ["LLLLLL",
         "LSGFLL",
         "LLLLLL"]

case6 = ["LLLLLLLLLLLLLLLLLLLLLL",
         "LLLLFLLLLLGGGGLLLGGLLL",
         "LLLLLLLLLLLLLLLLLGGLLL",
         "LLLLLLGGLLLLLLLLLLLLLL",
         "LLLLLLGGLLLGGLLLLLLLLL",
         "LLLLLLLLLLLGGLLLLLLLLL",
         "LLLLLLLLLLLLLLLLLLSLLL",
         "LLLLLLLLLLLLLLLLLLLLLL",
         "LLLLLLLLLLLLLLLLLLLLLL"]


case7 = ["LLLLLLLLLLLLLLLLLLLLL",
         "FLLLLLLLLLLLLLLLLLLLL",
         "LGLLLLLLLLLLLLLLLSLGG",
         "LGGGGGLLLLLGGGGLLLLLG",
         "LLLLLLGLLGGGGGGGGLLLG",
         "LLLLLLGLLLLLLLLLLLLLG",
         "LLLLLLGGGGGGGGGGGGGGG"]

def signalify(testc):
    print("{}".format(testc).replace("'", '"'))


from random import randint

def randomize(r, c):
    sz = r * c

    s = ""
    while len(s) < sz:
        typ = randint(0, 3)
        if typ == 0:
            ch = "G"
        else:
            ch = "L"
        s += ch * randint(1, 4)

    s = s[:sz]
    
    # put S and F
    sa = list(s)
    spos = randint(1, c - 1)
    sa[spos] = "S"

    fpos = randint(sz - c + 1, sz - 2)
    sa[fpos] = "F"

    s = ''.join(sa)
    
    arr = []
    for i in range(r):
        arr.append(s[:c])
        s = s[c:]

    return arr


    
a = ["SLLLLLL",
     "LLLLLLL",
     "LLLLLLL",
     "LLLLLLL",
     "LLLLLLF"]

b = ["LLLLLLL",
     "LLLLLLL",
     "LLLLLLL",
     "LLLLLLL",
     "SGGGGGF"]

c = ["SGGGGGF",
     "LLLLLLL",
     "LLLLLLL",
     "LLLLLLL",
     "LLLLLLL"]

d = ["SLLLLLL",
     "GLLLLLL",
     "GLLLLLL",
     "GLLLLLL",
     "FLLLLLL"]

e = ["SLGLGLG",
     "LGLGLGL",
     "GLGLGLG",
     "LGLGLGL",
     "GLGLGLF"]
    


# 012
# SLL
# LGF
# 345

# [[n,1,n,1,n,n],
#  [0,n,1,n,0,n],
#  [n,1,n,n,n,0],
#  [0,n,n,n,0,n],
#  [n,1,n,1,n,0],
#  [n,n,1,n,0,n]]

"""
row_ind = np.array([0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5]) # from
col_ind = np.array([1, 3, 0, 2, 4, 1, 5, 0, 4, 1, 3, 5, 2, 4]) # to
data =    np.array([1, 1, 0, 1, 0, 1, 0, 0, 0, 1, 1, 0, 1, 0]) # lava?

mat_coo = sparse.coo_matrix((data, (row_ind, col_ind)))
"""

#  0 1 2 3 4
#  5 6 7 8 9
# 1011121314
# 1516171819

pairtest(
    GurgleVolcano(case3, 100), 90,
    )

"""
    GurgleVolcano(b, 100), 100,
    GurgleVolcano(c, 100), 100,
    GurgleVolcano(d, 100), 100,
    GurgleVolcano(e, 100), 95,
"""

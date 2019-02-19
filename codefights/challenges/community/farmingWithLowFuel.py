from itertools import permutations

def count(m, rows, cols):
    ROWS = len(m)
    COLS = len(m[0])
    tot = 0
    for i, r in enumerate(rows):
        if r:
            for col in range(COLS):
                tot += m[i][col]

    for i, c in enumerate(cols):
        if c:
            for row in range(ROWS):
                tot += m[row][i]
                if rows[row]:
                    tot -= m[row][i]
                        

    return tot

    
def splt(lst, rows):
    return (lst[:rows], lst[rows:])
    
    
def FarmingWithLowFuel(farmMap, fuel):
    # brute force
    mx = 0
    rs = len(farmMap)
    cs = len(farmMap[0])
    
    fst = [1] * fuel + ((rs + cs) - fuel) * [0]

    p = list(permutations(fst))
    ps = set(p)
    
    for q in ps:
        mx = max(mx, count(farmMap, *splt(q, rs)))

    return mx

    """
test(FarmingWithLowFuel([[0,1,0,1], 
                         [1,0,1,1], 
                         [0,0,1,0]], 1), 3,

    """

test(
     FarmingWithLowFuel([[5,1,10], 
                         [3,3,0], 
                         [1,5,0]], 2), 24,

    )

"""

test(
     FarmingWithLowFuel([[1,1,1], 
                         [2,2,2], 
                         [3,3,3]], 2), 15,

)
"""

description = """
You are given a **Function Tower** that is made of **Function Bricks** as an array of strings. Each string is a level in the tower. Values flow downward starting from the first string, the topmost level.

A brick is the substring `[ f ]` (including its endpoint brackets, `[ ]`), where `f` is either a constant (a positive integer) or a function of one parameter (`x`). 

Functions are labeled as `x + n` or `x * n`, where `n` is a positive integer.

The output of a brick flows to all bricks directly below it. A constant brick ignores input, and always outputs the number it holds. 

The value of `x` fed to a function brick is the **sum of the outputs of all bricks directly above it**. A function brick will output the result of the arithmetic function called with this value of `x`.

Your task is to return the sum of all outputs of the bottommost level.

It is guaranteed that a function brick has at least one brick above it to serve as input. You do not need to check for errors.

__Example__


"""

test1 = [
"[       3        ]", 
"   [ x + 1 ][ 9  ]", 
"   [x + 14][x * 3]"]


import re

def functionTower(bars):
    cols = len(bars[0])
    brickpat = r'(\[.*?\])'

    # check columns
    for i in range(len(bars)):
        if len(bars[i]) != cols:
            raise ValueError("columns not uniform")
    
    ids = []
    vals = []
    brickid = 1
    brickcontents = [0]
    
    for row, line in enumerate(bars):
        bricks = re.finditer(brickpat, line)
        idrow = [0] * cols
        for b in bricks:
            for i in range(b.start(), b.end()):
                idrow[i] = brickid

            try:
                brickcontents.append(int(b.group(0)[1:-1]))
            except ValueError:
                aboveset = set()
                for i in range(b.start(), b.end()):
                    aboveset.add(ids[row-1][i])
                x = sum(brickcontents[k] for k in aboveset)
                formula = b.group(0)[1:-1].strip().replace('x', str(x))
                brickcontents.append(eval(formula))
            brickid += 1
        ids.append(idrow)

    for r in ids:
        print(r)
    print(brickcontents)
    return sum(brickcontents[k] for k in set(ids[-1]))
    

test2 = [
"[        1        ]   ",
"  [x * 2][3][x + 9]   ",
" [ x + 5  ][ x * 10  ]",
"   [x + 1]     [x + 1]",
"[      x * 2      ]   "]


"""
1
2 3 10
10  130
11  131

284
"""

test3 = [
"[         7          ]",
" [ x + 3]   [ x * 3 ] ",
" [ x + 1]   [ x * 2 ] ",
"      [ x + 5 ]       ",
"  [x + 10] [  9  ]    "]

"""
7
10 21
11 42
58
68 9

77
"""

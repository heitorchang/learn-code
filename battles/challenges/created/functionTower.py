draft2 = """
You are given a **Function Tower** of multiple levels as an array of strings. The Tower is made of **Bricks** of variable horizontal size and one character tall.

Integer values flow from top to bottom, starting from the topmost level (the first string of the `tower` array).

A brick `[ ... ]` (including its endpoint brackets, `[ ]`) is either a constant-number brick (a positive integer) or an arithmetic function.

Function bricks are labeled as `x + n` or `x * n`, where `n` is a positive integer. There are only addition and multiplication bricks.

The value of `x` fed to a function brick is the **sum of the outputs of all bricks it touches above**. It will then output the result of its computation.

The output of a brick flows to all bricks that it touches below. However, a constant-number brick ignores all input. It always outputs the single integer it holds. 

Your task is to return the sum of all outputs of the bottommost level.

It is guaranteed that every arithmetic brick has a value-producing brick above it (when computation is done top-to-bottom).

__Example__

For
```
tower: ["[       3        ]", 
 "   [ x + 1 ][ 9  ]", 
 "   [x + 14][x * 3]"]
```

In the middle level, the brick `x + 1` equals `4` and the constant-number `9` remains unchanged.

In the bottommost level, the `x + 14` brick receives the `x + 1` above as input, which we computed as `4`. So this brick has a value of `18`.

The final brick, `[x * 3]`, receives both `4` and `9` as inputs, because these are directly above it. Note that in the middle level, the bracket `]` is part of the `x + 1` brick.

So `x = 13` (the sum of `4` and `9`). We multiply it by `3` to get `39`.

Finally, the desired output is the sum of the bricks on the bottommost row, which is `18 + 39 = 57`. So we should return `57`.

For 
```
tower: ["[             5             ]", 
 "   [x * 2]   [x + 3]         ", 
 "   [ 0   ]   [ 0   ]  [ 9  ] ", 
 " [          x + 1          ] "]
```

we have values
```
[    5       ]
[10] [8]
[0]  [0]  [9]
[     10     ] 
```
The `[0]` bricks ignore the outputs above them, effectively discarding the intermediate results, and output `0` to the bottommost brick. Since there is also a `9` touching the bottommost brick, we return `9 + 1 = 10`.



The ASCII representation of the multiple levels of the function tower. The array is guaranteed to form a rectangle without missing characters at the end of each line.

*Guaranteed constraints*
The tower has at most `8` levels.
Each level is at most `40` characters long.


The sum of all the outputs of the bottommost level of the tower (the last string).

The expected total is at most `10,000`.

"""

finaldraft = """

You are given a **Function Tower** of multiple levels as an array of strings. The Tower is made of **Bricks** of variable length but they are only one character tall. 

A brick `[ ... ]` (including its endpoint brackets, `[ ]`) is either a constant-number (a positive integer) or a function of one parameter (`x`). 

Functions are labeled as `x + n` or `x * n`, where `n` is a positive integer. There are only addition and multiplication operations.

Integer values flow downward, starting from the first string, the topmost level.

The output of a brick flows to all bricks it touches below it. A constant-number brick ignores input, and always outputs the single integer it holds. 

The value of `x` fed to a function brick is the **sum of the outputs of all bricks it touches above it**. A function brick will output the result of its arithmetic function called with this value of `x`.

Your task is to return the sum of all outputs of the bottommost level.

It is guaranteed that every function brick has a value-producing brick above it.

__Example__

For
```
tower: ["[       3        ]", 
 "   [ x + 1 ][ 9  ]", 
 "   [x + 14][x * 3]"]
```

In the middle level, the brick `x + 1` equals `4` and the constant-number `9` remains unchanged.

In the bottommost level, the `x + 14` brick receives the `x + 1` above as input, which we computed as `4`. So this brick has a value of `18`.

The final brick, `[x * 3]`, receives both `4` and `9` as inputs, because these are directly above it. Note that in the middle level, the bracket `]` is part of the `x + 1` brick.

So `x = 13` (the sum of `4` and `9`). We multiply it by `3` to get `39`.

Finally, the desired output is the sum of the bricks on the bottommost row, which is `18 + 39 = 57`. So we should return `57`.

For 
```
tower: ["[             5             ]", 
 "   [x * 2]   [x + 3]         ", 
 "   [ 0   ]   [ 0   ]  [ 9  ] ", 
 " [          x + 1          ] "]
```

we have values
```
[    5       ]
[10] [8]
[0]  [0]  [9]
[     10     ] 
```
The `[0]` bricks ignore the outputs above them, effectively discarding the intermediate results, and hand over `0` to the bottommost brick. Since there is also a `9` touching the bottommost brick, we return `9 + 1 = 10`.

"""


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
"[             5             ]",
"   [x * 2]   [x + 3]         ",
"   [ 0   ]   [ 0   ]  [ 9  ] ",
" [          x + 1          ] "]

"""
10
"""
    
    

test3 = [
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

test4 = [
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

bogus = [
    "[ 3 ]      ",
    "[x+1] [x+2]",
    "[x + 3    ]"]


test5 = [
"[              2               ]",
"  [ x + 10 ]  [x * 3]  [x + 4]  ",
"      [      x * 2       ]      ",
"    [ x + 1 ]   [x * 5]  [ 5 ]  ",
"  [        x * 10            ]  ",
" [ x + 3 ]                      ",
"      [ x + 4 ]      [ 10 ]     ",
"   [ x + 10 ]     [ x + 5 ]     "]

"""
2
12 6 6
48
49 240 5
2940
2943
2947 10
2957 15

2972
"""

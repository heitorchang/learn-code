desc = """
You have escaped Dr. Leopardan's **Flamethrower Room**, but your path is blocked by the **Poison Gas Room**.

Like the previous trap, this is a tiled, 8-by-8 room. On the ceiling, multiple *poison vents* are mounted. They will release poisonous gas in a diamond shape. The numbers represent the concetration of poison gas in ppm (parts per million).

Vent coordinates are given as `[r, c]`, `r` being shown as **rows** and `c` being the **column** in the diagram.

```
For vents: [[4, 4]]

The room will be:
 C01234567
R+--------
0|00000000
1|00000000
2|00001000
3|00012100
4|00123210
5|00012100
6|00001000
7|00000000
```

As shown, the maximum concentration is 3 ppm directly below the vent, and spreads to 2 and 1 ppm. Gas is cumulative--if two vents are close to each other, the total concentration on each tile adds up:

```
For vents: [[4, 4], [4, 3]],

The room will be:
 C01234567
R+--------
0|00000000
1|00000000
2|00011000
3|00133100
4|01355310
5|00133100
6|00011000
7|00000000
```

There may be only one vent above any tile.

Finally, gas neutralizes when it touches any of the porous walls. So

```
For vents: [[2, 2]]

The room will be:
 C01234567
R+--------
0|21000000
1|32100000
2|21000000
3|10000000
4|00000000
5|00000000
6|00000000
7|00000000


Once more, your fellow spy Belinda Bitwiddle hacked into the lab's system and obtained the coordinates of the vents to save your life.

A tile is considered safe if its poison concentration is `1` or `0`.

Help her identify the total number of tiles that are safe to stand on until the poison dissipates completely.

__Examples__

Using the example diagrams above, you should return `59`, `56`, and `60` respectively.
"""

def inbounds(x, y):
    """Check if (x, y) is inside the 8-by-8 grid"""
    return 0 <= x <= 7 and 0 <= y <= 7


def inctile(grid, x, y, n):
    """Increases the concentration of gas at tile (x, y) by n units"""
    if inbounds(x, y):
        grid[x][y] += n


def addvent(grid, x, y):
    """Emit gas from (x, y)"""

    # Center
    inctile(grid, x, y, 3)

    # 2 ppm
    inctile(grid, x+1, y, 2)
    inctile(grid, x-1, y, 2)
    inctile(grid, x, y+1, 2)
    inctile(grid, x, y-1, 2)

    # 1 ppm
    # middle row
    inctile(grid, x+2, y, 1)
    inctile(grid, x-2, y, 1)

    # middle column
    inctile(grid, x, y+2, 1)
    inctile(grid, x, y-2, 1)

    # mid-top row
    inctile(grid, x+1, y+1, 1)
    inctile(grid, x-1, y+1, 1)
    
    # mid-bottom row
    inctile(grid, x+1, y-1, 1)
    inctile(grid, x-1, y-1, 1)


def poisonGasRoom(vents):
    if len(vents) != len(set((a, b) for a, b in vents)):
        print(vents, 'duplicates')
    grid = [[0 for _ in range(8)] for _ in range(8)]

    for vent in vents:
        addvent(grid, vent[0], vent[1])

    safe = 0

    for r in range(8):
        for c in range(8):
            if grid[r][c] <= 1:
                safe += 1

    return safe

pairtest(poisonGasRoom([[4, 4], [4, 3], [4, 5]]), 53,
         poisonGasRoom([[4, 4]]), 59,
         poisonGasRoom([[1, 0]]), 60,
         poisonGasRoom([]), 64,
         poisonGasRoom([[1,1],[1,2],[1,3],[0,0],[0,4]]), 47,
         poisonGasRoom([[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [1, 0], [1, 1], [1, 2], [1, 3], [1, 4], [1, 5], [1, 6], [1, 7], [2, 0], [2, 1], [2, 2], [2, 3], [2, 4], [2, 5], [2, 6], [2, 7], [3, 0], [3, 1], [3, 2], [3, 3], [3, 4], [3, 5], [3, 6], [3, 7], [4, 0], [4, 1], [4, 2], [4, 3], [4, 4], [4, 5], [4, 6], [4, 7], [5, 0], [5, 1], [5, 2], [5, 3], [5, 4], [5, 5], [5, 6], [5, 7], [6, 0], [6, 1], [6, 2], [6, 3], [6, 4], [6, 5], [6, 6], [6, 7], [7, 0], [7, 1], [7, 2], [7, 3], [7, 4], [7, 5], [7, 6], [7, 7]]), 0,
         poisonGasRoom([[3,4], [6,2],[1,3],[1,5],[2,6],[3,7]]), 36,

         poisonGasRoom([[0,0], [7,7]]), 58,
         poisonGasRoom([[0,1],[0,3],[0,5],[0,7],[2,2],[2,4],[2,6],[3,5],[3,7]]), 32,
         poisonGasRoom([[1,1],[3,3],[5,5],[7,7]]), 37,
         poisonGasRoom([[2,3],[2,4],[2,5],[2,6]]), 50,
         poisonGasRoom([[0,0],[7,0],[0,7],[7,7]]), 52,

)

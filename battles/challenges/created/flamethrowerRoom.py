desc = """

__Story__

You and your partner Belinda Bitwiddle are infiltrating evil Dr. Leopardan's secret lab but you have fallen in one of his trap rooms, the **Flamethrower Room**.

It's a 8-by-8 tiled square room with 8 powerful flamethrowers mounted on both the northern and western walls. After a brief flash, they will fire, burning everything in a straight line ahead of it.

Belinda has hacked Dr. Leopardan's systems and collected two integers from 0 to 255 inclusive that represent the state of the flamethrowers. When converted to an 8-bit number (left-padded with zeros so there are eight digits in total), a `0` represents an inactive flamethrower, and a `1` represents a live flamethrower.

The eight binary digits corresponding to `northWall` go from left to right in the diagram below, and the ones for `westWall` go from top to bottom.

__Your Task__

Belinda's information will save your from a crispy death, but she wants statistics. She wants to know how many tiles are safe to step on. Return this total number of safe tiles.

__Example__

For `northWall: 30, westWall: 180`, the room will look like this (`o` are safe tiles and `x` are burned tiles)

```
      
  + 00011110
W   --------
E 1|xxxxxxxx
S 0|oooxxxxo
T 1|xxxxxxxx
  1|xxxxxxxx
W 0|oooxxxxo
A 1|xxxxxxxx
L 0|oooxxxxo
L 0|oooxxxxo
```

You should return `16`, the number of `o`s shown above.

"""
from copy import deepcopy

def flamethrowerRoom(northWall, westWall):
    grid = [[0 for _ in range(8)] for _ in range(8)]

    northFl = map(int, bin(northWall)[2:].zfill(8))
    westFl = map(int, bin(westWall)[2:].zfill(8))

    nn = list(deepcopy(northFl))
    ww = list(deepcopy(westFl))
    print("  ", end="")
    print(list(nn))
    
    for i, r in enumerate(westFl):
        if r == 1:
            grid[i] = [1] * 8

    for i, c in enumerate(northFl):
        if c == 1:
            for r in range(8):
                grid[r][i] = 1
                
    for i, r in enumerate(grid):
        print(str(ww[i]), end=" ")
        print(r)

    tot = 0
    for r in range(8):
        for c in range(8):
            tot += grid[r][c]

    return 64 - tot

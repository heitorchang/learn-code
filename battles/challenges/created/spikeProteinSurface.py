desc = """
Your efforts in aiding the government's fight against the coronavirus crisis has now drawn the attention of a biotech startup.

They wish to synthesize a chemical compound that will attach to the viruses' spike proteins and hopefully prevent the viruses from entering human cells.

They have provided you with scanning electron microscope images of several coronavirus spike points.

These images are reproduced here as arrays of strings. You may consider the rows and columns to represent squares in a 2-D grid.

An empty space is represented by a dot (`.`) while a part of the virus spike point is represented by the lowercase letter `o`. Note that only the point is given to you; the rod has been cut out.

Your task is to estimate the exposed surface area of the spike point, measured as individual squares of the 2-D grid that are adjacent to a part of the virus (to the top, bottom, left or right).

Do not count the single spot on the bottommost row, because that is where the spike point is attached to the rod.

Note: All images are padded with at least two spaces on the top, left and right, and the bottommost row only has one `o`.

__Example__

For

```
spike:
["...................",
"...................",
"......o............",
"...o..o..o.........",
"....o.o.o..........",
".....ooo...........",
"......o............"]
```

we may mark adjacent spots that contribute to surface area with `x`s. They are:

```
spike:
["...................",
"......x............",
"...x.xox.x.........",
"..xoxxoxxox........",
"...xoxoxox.........",
"....xooox..........",
".....xox..........."]
```

There are `19` `x`s, so return `19`. Remember that the bottommost spot attaches to the rod and should not be counted.
"""

def spikeProteinSurface(image):
    grid = [list(row) for row in image]

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == '.':
                # top
                if r > 0:
                    if grid[r-1][c] == 'o':
                        grid[r][c] = 'x'

                # left
                if c > 0:
                    if grid[r][c-1] == 'o':
                        grid[r][c] = 'x'

                # right
                if c < len(grid[0]) - 1:
                    if grid[r][c+1] == 'o':
                        grid[r][c] = 'x'

                # bottom
                if r < len(grid) - 1:
                    if grid[r+1][c] == 'o':
                        grid[r][c] = 'x'


    # count xs
    xs = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'x':
                xs += 1

    return xs

print(spikeProteinSurface(
    ["...................",
     "...................",
     "......o............",
     "...o..o..o.........",
     "....o.o.o..........",
     ".....ooo...........",
     "......o............"]
))

print(spikeProteinSurface(
    ["..............",
     "..............",
     "...o.....o....",
     "....o...o.....",
     ".....o.o......",
     "......o......."]
))


print(spikeProteinSurface(
    ["....................",
     "....................",
     "...o.o..o..o..o.....",
     "...oooo.o..o..o.....",
     "......o.o..oooo.....",
     "......ooo..o........",
     "........o..o........",
     "........oooo........",
     ".........o.........."]
))


print(spikeProteinSurface(
    ["....................",
     "....................",
     "......o.......o.....",
     "......o..o....o.....",
     "......o..o...o......",
     "......o..o..o.......",
     ".......o.o.o........",
     "........ooo.........",
     "........o..........."]
))
print(spikeProteinSurface(
    [".............................",
     ".............................",
     "........o.....o..............",
     "........o.....o.o..o.o.......",
     "......o..o....o.o..ooo.......",
     ".......o..o...o..o.o.........",
     "........ooo...o..o.o.........",
     "..........oo..ooo..o.........",
     "...........o..o....o.........",
     "...........o..o.ooo..........",
     "...........ooooo.............",
     ".............o..............."]
))


print(spikeProteinSurface(
    ["....................",
     "....................",
     "........ooo.........",
     ".........o..........",
     ".........o..........",
     ".........o..........",
     ".........o..........",
     ".........o..........",
     ".........o.........."]
))

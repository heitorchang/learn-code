description = """
[Turtle graphics in Python is a popular way for introducing programming to kids.](https://docs.python.org/3.7/library/turtle.html)

Your granddaughter wants to show you how cool her latest drawing is, and to drive the point home of how powerful programs can be, you will tell her how many sides her polygon has, *without even looking at her screen*.

Of course, this will have to be done with a program that interprets the given Python Turtle script.

Assume that the following import is done at startup prior to running your granddaughter's script:

```
from turtle import fd, lt, rt
```

The turtle starts at the center of the graphics window, pointing to the right. 
`fd` is `forward`, moving the given number of pixels in its current direction. `lt` turns the turtle left (counterclockwise) the given number of degrees, and `rt` turns it to the right (clockwise).
"""

import sys
from turtle import fd, lt, rt

if __name__ == "__main__":
    filename = sys.argv[1]
    print("[", end="")

    cmds = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            eval(line)
            cmds.append('"' + line + '"')

    print(",".join(cmds), end="")
    print("]")
    dummy = input("Press Enter to quit.")

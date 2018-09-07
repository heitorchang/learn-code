description = """
You've built a powerful pool-shooting robot and want to try it out on custom-built tables. Because you don't want to waste materials, you will first simulate where the ball should end up going.

The tables and the ball will be really smooth, so once the ball rolls, it won't stop until it falls into a pocket. The ball will also bounce perfectly elastically at the edges, losing no speed whatsoever.

Your robot will be set up to strike the red ball placed right outside the lower-left pocket, angled at exactly 45 degrees from either edge. The ball will roll towards the top and to the right, bouncing happily until it falls into a pocket.

The pockets are numbered from 0 to 5, counting clockwise from the initial (bottom left) pocket. Given integers width and height representing the dimensions of the table, your task is to find which pocket the ball will eventually end up in.

The width is guaranteed to be an even number of units and the side pockets are always at the midpoint of the width. The height is never greater than the width.

Example

For width = 8, and height = 3, the output should be poolTableBounce(width, height) = 5.

In the diagram below, the red line indicates the path, showing that the ball falls into pocket number 5.

8 by 3 table

Input / Output

[execution time limit] 4 seconds (py3)

[input] integer width

An even integer representing the width of the custom pool table.

Guaranteed constraints:
2 ≤ width ≤ 106

[input] integer height

The height of the custom pool table.

Guaranteed constraints:
1 ≤ height ≤ width

[output] integer

The pocket number (0 to 5) that the ball ends up in.

"""

comments = """
oleg_l: This is pure math. Let the ball to go by the initial direction and reflect the table instead. Try to see the pattern.


"""

def poolTableBounce(width, height):
    midpt = width // 2
    
    def checkPocket(x, y):
        if x == 0 and y == height:
            return 1
        elif x == midpt and y == height:
            return 2
        elif x == width and y == height:
            return 3
        elif x == width and y == 0:
            return 4
        elif x == midpt and y == 0:
            return 5
        else:
            return 0


    def move(x, y, d):
        # d is direction: 0 = NE, 1 = SE, 2 = SW, 3 = NW

        def isEdge(px, py):
            return px == 0 or px == width or py == 0 or py == height

        if d == 0: # NE
            while True:
                x += 1
                y += 1
                if isEdge(x, y):
                    if x < width:
                        d = 1
                    else:
                        d = 3
                    return (x, y, d)

        elif d == 1: # SE
            while True:
                x += 1
                y -= 1
                if isEdge(x, y):
                    if x < width:
                        d = 0
                    else:
                        d = 2
                    return (x, y, d)

        elif d == 2: # SW
            while True:
                x -= 1
                y -= 1
                if isEdge(x, y):
                    if x > 0:
                        d = 3
                    else:
                        d = 1
                    return (x, y, d)

        elif d == 3: # NW
            while True:
                x -= 1
                y += 1
                if isEdge(x, y):
                    if x > 0:
                        d = 2
                    else:
                        d = 0
                    return (x, y, d)

    x = 0
    y = 0
    direction = 0
    
    while True:
        x, y, direction = move(x, y, direction)
        p = checkPocket(x, y)
        if p != 0:
            return p
    return -1

description = """
Below we will define an n-interesting polygon. Your task is to find the area of a polygon for a given n.

A 1-interesting polygon is just a square with a side of length 1. An n-interesting polygon is obtained by taking the n - 1-interesting polygon and appending 1-interesting polygons to its rim, side by side. You can see the 1-, 2-, 3- and 4-interesting polygons in the picture below.

                       x  
             x        xxx 
      x     xxx      xxxxx
 x   xxx   xxxxx    xxxxxxx
      x     xxx      xxxxx
             x        xxx
                       x
"""

def shapeAreaRec(n):
    """recursive solution, but blows up on hidden test"""
    if n == 1:
        return 1
    return 4 * (n-1) + shapeAreaRec(n-1)

def shapeArea(n):
    area = 1
    while n > 1:
        area += 4 * (n-1)
        n -= 1
    return area


def test():
    testeql(shapeArea(2), 5)
    testeql(shapeArea(3), 13)

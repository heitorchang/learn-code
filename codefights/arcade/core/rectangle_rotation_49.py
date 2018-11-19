from math import sqrt

def isunder(x, y, slope, yint):
    """is point (x, y) under the line y = slope * x + yint?"""
    line_ypt = x * slope + yint
    return y < line_ypt

def rectangleRotation(a, b):
    """
      1
    +----+
  4 |    | 2
    +----+
      3

    to
    
    1/\2
    /  \
    \  /
    4\/3

    where each line is (slope, yint)
    """

    line2 = (-1, sqrt(a**2 / 2))
    line4 = (-1, -sqrt(a**2 / 2))

    line1 = (1, sqrt(b**2 / 2))
    line3 = (1, -sqrt(b**2 / 2))

    tot = 0

    print(line2, line1)
    print(line3, line4)

    for xpts in range(-b * a, b * a):
        for ypts in range(-a * b, a * b):
            if (isunder(xpts, ypts, line1[0], line1[1]) and
                isunder(xpts, ypts, line2[0], line2[1]) and
                not isunder(xpts, ypts, line3[0], line3[1]) and
                not isunder(xpts, ypts, line4[0], line4[1])):
                tot += 1
    return tot

test(rectangleRotation(6, 4), 23,
     rectangleRotation(30, 2), 65,
     rectangleRotation(50, 4), 177)

def test():
    testequal(findSquareSide([-3, -3, 2, 2], [-3, -3, 2, 2]), 25)

def findSquareSide(x, y):
    min_x, max_x = min(x), max(x)
    min_y, max_y = min(y), max(y)
    print(min_x, max_x)
    return (max_x - min_x) * (max_y - min_y)

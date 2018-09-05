from itertools import combinations

def pair_to_line(a, b):
    """Convert a pair of coordinates to line (y = mx + b)"""
    if a[0] == b[0]:  # vertical line, b = x-intercept
        return (float('inf'), a[0])
    else:
        slope = (b[1] - a[1]) / (b[0] - a[0])
        y_int = b[1] - slope * b[0]
        return (slope, y_int)

def is_collinear(a, b, c):
    line_ab = pair_to_line(a, b)
    line_bc = pair_to_line(b, c)
    return line_ab == line_bc

def checkio(cakes):
    """Keep track of valid rows (lines) as vertical or sloped lines.
    (y = mx + b. if m is infinity, b is x-intercept.)
    Use a set to prevent storing duplicate rows.
    Use itertools.combinations to gather list of all possible
    cake triples. If they are collinear, add to set of rows.
    Return len(set_of_lines)
    """
    lines = set()
    triples = combinations(cakes, 3)
    for t in triples:
        if is_collinear(*t):
            lines.add(pair_to_line(t[0], t[1]))
    return len(lines)
    
def test():
    assert checkio([[3, 3], [5, 5], [8, 8], [2, 8], [8, 2]]) == 2
    assert checkio(
        [[2, 2], [2, 5], [2, 8], [5, 2], [7, 2], [8, 2],
         [9, 2], [4, 5], [4, 8], [7, 5], [5, 8], [9, 8]]) == 6

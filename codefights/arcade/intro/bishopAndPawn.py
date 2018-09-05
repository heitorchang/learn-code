description = """
Given the positions of a white bishop and a black pawn on the standard chess board, determine whether the bishop can capture the pawn in one move.

The bishop has no restrictions in distance for each move, but is limited to diagonal movement. Check out the example below to see how it can move:
"""

def cellToCoords(cell):
    return [1+ord(cell[0]) - ord('a'), int(cell[1])]

def bishopAndPawn(b, p):
    bc = cellToCoords(b)
    pc = cellToCoords(p)
    return abs(bc[0]-pc[0]) == abs(bc[1]-pc[1])

def coordToGrid(coord):
    col = ord(coord[0]) - ord('a')
    row = int(coord[1]) - 1
    return (col, row)

def inBounds(coord):
    return 0 <= coord[0] <= 7 and 0 <= coord[1] <= 7 

def safe_pawns(pawns):
    board = [[0 for _ in range(8)] for _ in range(8)]

    # place pawns
    for pawn in pawns:
        gridCoord = coordToGrid(pawn)
        board[gridCoord[0]][gridCoord[1]] = 1

    totalSafe = 0
    # check each pawn and guard
    for pawn in pawns:
        gridCoord = coordToGrid(pawn)
        # if in first row, it is unsafe
        if gridCoord[1] > 0:
            bottomLeft = (gridCoord[0] - 1, gridCoord[1] - 1)
            bottomRight = (gridCoord[0] + 1, gridCoord[1] - 1)
            protectedByLeft = inBounds(bottomLeft) and board[bottomLeft[0]][bottomLeft[1]] == 1
            protectedByRight = inBounds(bottomRight) and board[bottomRight[0]][bottomRight[1]] == 1
            if protectedByLeft or protectedByRight:
                totalSafe += 1
    return totalSafe

def test():
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
    testeql(safe_pawns(["a1","b2","c3","d4","e5","f6","g7","h8"]), 7)

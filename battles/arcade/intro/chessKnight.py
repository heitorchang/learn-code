def parseCell(cell):
    col = 1 + ord(cell[0]) - ord('a')
    row = int(cell[1])
    return (row, col)

def inBounds(coords):
    return 1 <= coords[0] <= 8 and 1 <= coords[1] <= 8

def chessKnight(cell):
    knightCoords = parseCell(cell)
    moves = [(-2, 1), (-1, 2), (1, 2), (2, 1),
             (-2, -1), (-1, -2), (1, -2), (2, -1)]
    validMoves = 0
    for m in moves:
        if inBounds((knightCoords[0] + m[0],
                     knightCoords[1] + m[1])):
            validMoves += 1
    return validMoves

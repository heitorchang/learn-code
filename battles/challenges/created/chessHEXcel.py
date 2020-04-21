desc = """
To spice up the workday of accountants worldwide, you are developing a new type of spreadsheet app that combines features of Chess into standard spreadsheet software.

Instead of using cell references and ranges such as `A2:B5`, a cell may be named as a Chess piece. For now, you will use Queens (`Q`), Kings (`K`), Rooks (`R`) and Bishops (`B`).

In this challenge, we will use a 8 x 8 board. Cells without a chess piece will have a fixed integer value from 0 to 14, corresponding to the sum of the indices of its row and column position.

```
0  1  2  3  4  5  6  7
1  2  3  4  5  6  7  8
2  3  4  5  6  7  8  9
3  4  5  6  7  8  9 10
4  5  6  7  8  9 10 11
5  6  7  8  9 10 11 12
6  7  8  9 10 11 12 13
7  8  9 10 11 12 13 14
```

Chess pieces all belong to one color and may be placed anywhere. Also, there may be repeats of the same piece.

The value of its cell will be the sum of all the other cells that may be captured by the piece (in all 8 directions until the edge of the board for Queens, one space in all 8 directions for Kings, horizontally and vertically for Rooks, and diagonally for Bishops).

If a chess piece can capture another chess piece, the entire sum of the captured piece is added to the cell doing the capturing.

Since an empty cell may have many pieces capturing it, its entire value is repeatedly given to all pieces capturing that cell.

In this challenge, there will be no scenarios where two pieces capture each other (leading to circular references).

You will be given an array of strings representing locations of chess pieces in the format `"PRC"` where `P` is the type of chess piece (Q, K, R, B), `R` is the row index (from top to bottom in the diagram above) and `C` is the column index.

Your task is to return the sum of all the cells containing chess pieces.

__Example__

For:

```
pieces: ["Q42", "K15"]
```

The board will look like this:

```
0  1  2  3  4  5  6  7
1  2  3  4  5  K  7  8
2  3  4  5  6  7  8  9
3  4  5  6  7  8  9 10
4  5  Q  7  8  9 10 11
5  6  7  8  9 10 11 12
6  7  8  9 10 11 12 13
7  8  9 10 11 12 13 14
```

It is easier to compute the pieces' values by first computing the King's value and then let its value be captured by the Queen. The King's eight neighbors are: `4 + 5 + 6 + 5 + 7 + 6 + 7 + 8`, equaling `48`. The Queen can capture a much larger number of cells:

Top: `2 + 3 + 4 + 5 = 14`
Top-right: `6 + 6 + King (48) + 6 = 66`
Right: `7 + 8 + 9 + 10 + 11 = 45`
Bottom-right: `8 + 10 + 12 = 30`
Bottom: `7 + 8 + 9 = 24`
Bottom-left: `6 + 6 = 12`
Left: `4 + 5 = 9`
Top-left: `2 + 4 = 6`

Total = `14 + 66 + 45 + 30 + 24 + 12 + 9 + 6` equals `206`

Finally, we add the two pieces together, `48 + 206` to return `254`.
"""

def inbounds(r, c):
    return 0 <= r <= 7 and 0 <= c <= 7


def intval(r, c):
    return r + c


def q(r, c):
    """Get cell coordinates capturable by a queen"""
    cells = set()
    for a in range(8):
        for b in range(8):
            if a == r or b == c or a + b == r + c:
                cells.add((a, b))
    # last diagonal
    for a in range(8):
        cdiff = c - r
        if inbounds(a, a + cdiff):
            cells.add((a, a + cdiff))
    
    # remove self
    cells.remove((r, c))
    return cells


def k(r, c):
    """Get cell coordinates capturable by a king"""
    cells = set()
    for a in range(r-1, r+2):
        for b in range(c-1, c+2):
            if not (a == r and b == c):
                if inbounds(a, b):
                    cells.add((a, b))
    return cells


def rook(r, c):
    """rook"""
    cells = set()
    for a in range(8):
        for b in range(8):
            if a == r or b == c:
                cells.add((a, b))
    # remove self
    cells.remove((r, c))
    return cells


def bish(r, c):
    """bishop"""
    cells = set()
    for a in range(8):
        for b in range(8):
            if a + b == r + c:
                cells.add((a, b))
    # other diagonal
    for a in range(8):
        cdiff = c - r
        if inbounds(a, a + cdiff):
            cells.add((a, a + cdiff))

    # remove self
    cells.remove((r, c))
    return cells


def ev(board, coord):
    r, c = coord
    if isinstance(board[r][c], int):
        return board[r][c]

    p = board[r][c]

    fns = {'Q': q,
           'K': k,
           'R': rook,
           'B': bish}
    
    cells = fns[p](r, c)
    
    return sum(ev(board, cell) for cell in cells)


def chessXcel(pieces):
    board = [[r + c for c in range(8)] for r in range(8)]
    prefs = set()
    
    for p in pieces:
        t, r, c = p[0], int(p[1]), int(p[2])
        board[r][c] = t
        prefs.add((r, c))

    ans = 0
    for p in prefs:
        ans += ev(board, p)

    return ans


"""

pairtest(k(1, 5), set([(0, 4), (0, 5), (0, 6),
                       (1, 4), (1, 6),
                       (2, 4), (2, 5), (2, 6)]),
         k(0, 0), set([(0, 1), (1, 1), (1, 0)]),
         k(6, 7), set([(5, 6), (5, 7), (6, 6), (7, 6), (7, 7)]),
         k(7, 7), set([(6, 6), (6, 7), (7, 6)]))




pairtest(q(3, 3), set([(0, 3), (1, 3), (2, 3),
                      (2, 4), (1, 5), (0, 6),
                      (3, 4), (3, 5), (3, 6), (3, 7),
                      (4, 4), (5, 5), (6, 6), (7, 7),
                      (4, 3), (5, 3), (6, 3), (7, 3),
                      (4, 2), (5, 1), (6, 0),
                      (3, 2), (3, 1), (3, 0),
                      (2, 2), (1, 1), (0, 0)]),

         q(2, 5), set([(0, 5), (1, 5),
                      (1, 6), (0, 7),
                      (2, 6), (2, 7),
                      (3, 6), (4, 7),
                      (3, 5), (4, 5), (5, 5), (6, 5), (7, 5),
                      (3, 4), (4, 3), (5, 2), (6, 1), (7, 0),
                      (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
                      (1, 4), (0, 3),
                      (1, 5), (0, 5),]))


pairtest(r(5, 6), set([(0, 6), (1, 6), (2, 6), (3, 6), (4, 6), (6, 6), (7, 6),
                       (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 7)])


         )


pairtest(b(4, 2), set([(6, 0), (5, 1), (3, 3), (2, 4), (1, 5), (0, 6),
                       (2, 0), (3, 1), (5, 3), (6, 4), (7, 5)]))

pairtest(chessXcel(["B00"]), 56,
         chessXcel(["R00"]), 56)

"""

pairtest(chessXcel(["Q42", "K15"]), 254,
         chessXcel(["R37"]), 116,
         chessXcel(["K01", "R06", "B42", "R45"]), 541,
         chessXcel(["K11", "K13"]), 48,
         chessXcel(["K00", "B07", "R70", "Q31"]), 384,
         chessXcel(["K14", "R74", "B52"]), 420,
         chessXcel(["Q00", "K07", "K77"]), 209,
         chessXcel(["K14", "R74", "Q41"]), 519)



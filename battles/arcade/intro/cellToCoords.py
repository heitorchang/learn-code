description = """
Given two cells on the standard chess board, determine whether they have the same color or not.

Example

For cell1 = "A1" and cell2 = "C3", the output should be
chessBoardCellColor(cell1, cell2) = true."""


def cellToCoords(cell):
    return [1+ord(cell[0])-ord('A'), int(cell[1])]

def chessBoardCellColor(cell1, cell2):
    cell1Parity = sum(cellToCoords(cell1)) % 2
    cell2Parity = sum(cellToCoords(cell2)) % 2
    return cell1Parity == cell2Parity

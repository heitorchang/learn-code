"""does not pass two hidden tests"""

def neighbors(width, height, coords):
    row, col = coords
    answer = []
    
    for i in range(row-1, row+2):
        for j in range(col-1, col+2):
            if 0 <= i < width and 0 <= j < height:
                answer.append((i, j))
    return answer
    

def findWordRecur(board, word, coords, buildUp, visited):
    rows = len(board)
    cols = len(board[0])
    
    if buildUp == word:
        return word

    newLetter = word[len(buildUp)]
    
    for newCoords in neighbors(rows, cols, coords):
        newRow, newCol = newCoords
        if board[newRow][newCol] == newLetter and newCoords not in visited:
            return findWordRecur(board, word, newCoords,
                                 buildUp+newLetter, visited+[newCoords])
    

def findWord(board, word):
    rows = len(board)
    cols = len(board[0])
    
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0]:
                firstLetterCoords = (r, c)
                w = findWordRecur(board, word, firstLetterCoords,
                                  word[0], [firstLetterCoords])
                if w:
                    return w

def wordBoggle(board, words):
    if not words:
        return []

    ans = set()
    for w in words:
        if findWord(board, w):
            ans.add(w)
    return sorted(list(ans))


    

test(wordBoggle([["R","L","D"], 
                 ["U","O","E"], 
                 ["C","S","O"]], ["OOR", "ROLU", "SED", "RUC"]), ["OOR", "ROLU", "RUC", "SED"],
     wordBoggle([["A", "B"],
                 ["C", "D"],
                 ["E", "F"]], ["ADBC", "ADBCFE"]), ["ADBC", "ADBCFE"])


"""



test(wordBoggle([["R","L","D"], 
                 ["U","O","E"], 
                 ["C","S","O"]],["CODE",
                                 "COC",
                                 "SOLD", 
                                 "RULES", 
                                 "COOL"]), ["CODE", "RULES", "SOLD"])

"""

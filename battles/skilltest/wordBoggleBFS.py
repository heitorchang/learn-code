from collections import deque

def neighbors(w, h, r, c):
    ans = []
    for m in range(r-1, r+2):
        for n in range(c-1, c+2):
            if 0 <= m < w and 0 <= n < h:
                ans.append((m, n))
    return ans

def findword(board, word):
    print('findword')
    rows = len(board)
    cols = len(board[0])
    
    q = deque()
    # find first letter
    found = False
    for r in range(rows):
        for c in range(cols):
            if board[r][c] == word[0]:
                firstrow, firstcol = r, c
                found = True
    if not found:
        return None
    
    wptr = 0
    visited = [[False for _ in range(cols)] for _ in range(rows)]
    visited[firstrow][firstcol] = True
    curr = firstrow
    curc = firstcol
    
    q.append([curr, curc, word[wptr], [(curr, curc)]])
    
    while q:
    # for i in range(30):
        curlet = q.popleft()
        print(curlet)
        if word == curlet[2]:
            return word
        if len(curlet[2]) > len(word):
            return None
            
        for coords in neighbors(rows, cols, curlet[0], curlet[1]):
            if (coords[0], coords[1]) not in curlet[3]:
                q.append([coords[0], coords[1], curlet[2]+board[coords[0]][coords[1]], curlet[3] + [(coords[0], coords[1])]])
                # print(q)
    return None

def wordBoggle(board, words):
    if not words:
        return []

    ans = set()
    for w in words:
        if findword(board, w):
            ans.add(w)
    return sorted(list(ans))

"""
test(wordBoggle([["R","L","D"], 
                 ["U","O","E"], 
                 ["C","S","O"]], "CODE"))
"""


test(wordBoggle([["R","L","D"], 
                 ["U","O","E"], 
                 ["C","S","O"]],["CODE", 
                                 "SOLO", 
                                 "RULES", 
                                 "COOL"]), ["CODE", "RULES"])

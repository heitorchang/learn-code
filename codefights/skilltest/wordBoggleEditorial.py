# translation of JS walkthrough solution

def wordBoggle(board, words):

    def seek(x, y, node, visited=None):
        if visited is None:
            visited = set()
        hash = 5 * x + y

        visited.add(hash)

        if "$" in node:
            wordsFound.add(node['$'])

        for dx in range(-1, 2):
            for dy in range(-1, 2):
                if not(dx == 0 and dy == 0) and 0 <= x + dx < len(board) and 0 <= y + dy < len(board[0]):
                    nextHash = 5 * (x+dx) + (y+dy)
                    letter = board[x+dx][y+dy]

                    if letter in node and nextHash not in visited:
                        seek(x + dx, y + dy, node[letter], visited)

        visited.remove(hash)


    trie = {}

    for word in words:
        node = trie

        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]

        node["$"] = word

    wordsFound = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            letter = board[i][j]
            if letter in trie:
                seek(i, j, trie[letter])

    
    return sorted(list(wordsFound))

    
test(wordBoggle([["R","L","D"], 
                 ["U","O","E"], 
                 ["C","S","O"]],["CODE",
                                 "COC",
                                 "SOLD", 
                                 "RULES", 
                                 "COOL"]), ["CODE", "RULES", "SOLD"])


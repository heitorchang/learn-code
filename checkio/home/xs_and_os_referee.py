from collections import Counter

def checkio(game_result):
    counters = []

    # rows
    for r in range(0, 3):
        counters.append(Counter(game_result[r]))

    # columns
    for c in range(0, 3):
        counters.append(Counter(game_result[0][c] + game_result[1][c] + game_result[2][c]))

    # diagonals
    counters.append(Counter(game_result[0][0] + game_result[1][1] + game_result[2][2]))
    counters.append(Counter(game_result[0][2] + game_result[1][1] + game_result[2][0]))

    # check counters
    for ctr in counters:
        if max(ctr.values()) == 3:
            char = ctr.most_common()[0][0]
            if char != ".":
                return char
        
    return "D"

def test():
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio([
        "X.O",
        "XX.",
        "XOO"]) == "X", "Xs wins"
    assert checkio([
        "OO.",
        "XOX",
        "XOX"]) == "O", "Os wins"
    assert checkio([
        "OOX",
        "XXO",
        "OXX"]) == "D", "Draw"
    assert checkio([
        "O.X",
        "XX.",
        "XOO"]) == "X", "Xs wins again"


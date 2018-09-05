def sumSq(s):
    tot = 0
    for elem in s:
        tot += elem ** 2
    return tot
    
def selection(cards, choice):
    bitStr = list(bin(choice)[2:].zfill(len(cards)))
    # pr('bitStr')
    nums = set()
    for i, b in enumerate(bitStr):
        # pr('cards[i][0]')
        if b == '0':  # visible
            nums.update(cards[i][0])
        else:
            nums.update(cards[i][1])
    return nums

def buildCard(cardStr, maxWritten):
    parts = list(map(int, cardStr.split()))
    card = ([], [])
    allNums = set(range(1, maxWritten + 1))
    visible = set(parts[1:])
    notVisible = allNums - visible
    return (sorted(visible), sorted(notVisible))

def query(cards, L, R):
    # convert to 0-based
    L -= 1
    R -= 1
    cardSubset = cards[L:R+1]

    # pr('cardSubset')
    
    # prepare choices (to be converted to bit strings)
    maxChoice = 2 ** len(cardSubset)
    maxTot = 0
    for c in range(maxChoice):
        s = selection(cardSubset, c)
        selSumSq = sumSq(s)
        if selSumSq > maxTot:
            maxTot = selSumSq
        # pr('c s')
    return maxTot
    
def main():
    numCards, maxWritten, queries = [2, 3, 2]
    cards = []
    cards.append(buildCard("2 2 1", maxWritten))
    cards.append(buildCard("2 2 3", maxWritten))

    # queries loop
    L, R = 1, 1
    print(query(cards, L, R))  # expect: 9

    L, R = 1, 2
    print(query(cards, L, R))  # expect: 14
    

def test():
    testeql(selection([([1,2],[3]),([2], [1,3]),([3], [1,2])], 3), set([1,2,3]))
    testeql(buildCard("2 2 1", 3), ([1,2], [3]))
    testeql(main(), None)

from itertools import zip_longest

def find_in_grid(grid, word):
    word = word.lower()
    for i, line in enumerate(grid):
        line = line.lower()
        find_result = line.find(word)
        if find_result > -1:
            return [i+1, find_result+1, i+1, find_result+len(word)]
    return None   

def checkio(text, word):
    rhyme = [line.replace(' ', '') for line in text.split('\n')]
    # check lines
    in_line = find_in_grid(rhyme, word)
    if in_line:
        return in_line        

    # check columns
    rhyme_transposed = [''.join(col) for col in zip_longest(*rhyme, fillvalue=' ')]
    in_column = find_in_grid(rhyme_transposed, word)
    if in_column:
        return [in_column[1], in_column[0], in_column[3], in_column[2]]
    return None

def test():
    assert checkio("""DREAMING of apples on a wall,
And dreaming often, dear,
I dreamed that, if I counted all,
-How many would appear?""", "ten") == [2, 14, 2, 16]
    assert checkio("""He took his vorpal sword in hand:
Long time the manxome foe he sought--
So rested he by the Tumtum tree,
And stood awhile in thought.
And as in uffish thought he stood,
The Jabberwock, with eyes of flame,
Came whiffling through the tulgey wood,
And burbled as it came!""", "noir") == [4, 16, 7, 16]

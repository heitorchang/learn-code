from collections import Counter

def firstNotRepeatingCharacter(s):
    ctr = Counter(s)
    singles = set()
    for letter in ctr:
        if ctr[letter] == 1:
            singles.add(letter)

    # now iterate through string
    for c in s:
        if c in singles:
            return c
    return '_'

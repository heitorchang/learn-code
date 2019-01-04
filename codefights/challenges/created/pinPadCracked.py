description = """

Given a sequence of the five 0 or 2, 1 or 8, etc. "buttons"

and the order each was pressed (0-based indices are given), determine if the correct 4-digit PIN can be deduced.
"""

from random import shuffle, seed

def generateButtons(aSeed=None):
    seed(aSeed)
    
    digits = list(map(str, range(10)))

    shuffle(digits)

    pairs = [''.join(sorted(digits[i:i+2])) for i in range(0, 10, 2)]

    pairs.sort()
    
    out = ' '.join(pairs)
    
    if not testButtons(out):
        raise ValueError

    return out


def testButtons(buttonStr):
    s = set(buttonStr.replace(" ", ""))
    return len(s) == 10
    

def pinPadCracked(logins):
    return True


print(generateButtons())

test(generateButtons(0), '02 15 34 69 78')


test(testButtons("01 23 45 67 89"), True,
     testButtons("11 22 33 44 55"), False,
     testButtons("09 18 27 36 45"), True)
    
test(pinPadCracked(["02 19 25 37 46 0032",
                    "08 12 39 64 37 1234"]), True)

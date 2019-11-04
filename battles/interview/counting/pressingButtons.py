description = """
Given a string of digits, return all of the possible non-empty letter combinations that the number could represent. The mapping of digits to letters is the same as you would find on a telephone's buttons, as in the example below:

The resulting array should be sorted lexicographically.

Example

For buttons = "42", the output should be
pressingButtons(buttons) = ["ga", "gb", "gc", "ha", "hb", "hc", "ia", "ib", "ic"].

Input/Output

    [time limit] 4000ms (py3)

    [input] string buttons

    A string composed of digits ranging from '2' to '9'.

    Guaranteed constraints:

    0 ≤ buttons.length ≤ 7.

    [output] array.string

"""

def pressingButtonsIterate(buttons):
    letters = { "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz",
    }

    if buttons == "":
        return []

    curLevel = ['']

    for button in buttons:
        newLevel = []
        for substr in curLevel:
            for letter in letters[button]:
                newLevel.append(substr + letter)
        curLevel = newLevel
    return curLevel


def pressingButtons(buttons):
    """Recursive"""
    # Wrapper for dealing with "" input
    letters = { "2": "abc",
                "3": "def",
                "4": "ghi",
                "5": "jkl",
                "6": "mno",
                "7": "pqrs",
                "8": "tuv",
                "9": "wxyz",
    }
    def pressingButtonsRecurse(buttons):
        if len(buttons) == 0:
            return ['']
        else:
            prev = pressingButtonsRecurse(buttons[:-1])
            return [p + ltr for p in prev for ltr in letters[buttons[-1]]]

    if buttons == "":
        return []
    return pressingButtonsRecurse(buttons)
        
def test():
    testeql(pressingButtons(""), [])
    testeql(pressingButtons("2"), ["a", "b", "c"])
    testeql(pressingButtons("42"), ["ga", 
                                    "gb", 
                                    "gc", 
                                    "ha", 
                                    "hb", 
                                    "hc", 
                                    "ia", 
                                    "ib", 
                                    "ic"])
    testeql(pressingButtons("234"), ["adg", 
 "adh", 
 "adi", 
 "aeg", 
 "aeh", 
 "aei", 
 "afg", 
 "afh", 
 "afi", 
 "bdg", 
 "bdh", 
 "bdi", 
 "beg", 
 "beh", 
 "bei", 
 "bfg", 
 "bfh", 
 "bfi", 
 "cdg", 
 "cdh", 
 "cdi", 
 "ceg", 
 "ceh", 
 "cei", 
 "cfg", 
 "cfh", 
 "cfi"])

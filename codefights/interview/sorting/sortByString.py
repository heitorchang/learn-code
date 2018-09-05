description = """
Sort the letters in the string s by the order they occur in the string t.

Example

    For s = "weather" and t = "therapyw", the output should be
    sortByString(s, t) = "theeraw";

    For s = "good" and t = "odg", the output should be
    sortByString(s, t) = "oodg".

Input/Output

    [time limit] 4000ms (py3)

    [input] string s

    A string consisting only of lowercase English letters.

    Guaranteed constraints:
    0 ≤ s.length ≤ 104.

    [input] string t

    A string consisting only of unique lowercase English letters. It is guaranteed that t contains all of the letters that occur in s.

    Guaranteed constraints:
    0 ≤ t.length ≤ 26.

    [output] string

"""

def test():
    # testeql(sortByString("good", "odg"), "oodg")
    # testeql(sortByString("wcptedsgaisegdxpestczpxat", "svldchawotingexpufzrk"), "sssddccaawtttiggeeexxpppz")
    testeql(sortByStringDict("good", "odg"), "oodg")
    testeql(sortByStringDict("wcptedsgaisegdxpestczpxat", "svldchawotingexpufzrk"), "sssddccaawtttiggeeexxpppz")

from collections import Counter
    
def sortByString(s, t):
    # method 1: Counter
    ctr = Counter(s)
    out = ""
    
    for c in t:
        out += c * ctr[c]

    return out
    
def sortByStringDict(s, t):
    # method 2: assign each letter a number
    letterToDigit = {}
    for i, c in enumerate(t):
        letterToDigit[c] = i
    sInts = []
    for c in s:
        sInts.append(letterToDigit[c])
    # pr('sInts')
    sInts.sort()
    # pr('sInts')
    intToLetter = {v: k for k, v in letterToDigit.items()}
    out = ""
    for n in sInts:
        out += intToLetter[n]
    return out

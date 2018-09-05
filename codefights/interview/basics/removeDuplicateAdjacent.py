description = """
Given a string s, recursively remove any adjacent duplicate characters that it contains.

Example

    For s = "cooodefightssforrrcodee", the output should be
    removeDuplicateAdjacent(s) = "cdefightfocod";
    For s = "acaaabbbacdddd", the output should be
    removeDuplicateAdjacent(s) = "acac".

Input/Output

    [time limit] 4000ms (py3)

    [input] string s

    A string composed of lowercase English letters.

    Guaranteed constraints:

    1 ≤ s.length ≤ 50.

    [output] string

    A string obtained by removing all adjacent duplicates from the input string.

"""

def test():
    testeql(removeDuplicateAdjacent("eee"), "")
    testeql(removeDuplicateAdjacent("abc"), "abc")
    testeql(removeDuplicateAdjacent("cooodefightssforrrcodee"), "cdefightfocod")
    testeql(removeDuplicateAdjacent("mississipie"), "mpie") 




    


def removeDuplicateAdjacentRecurse(s):
    # first attempt, does not pass all tests

    # cooodee
    #  cooodee
    if len(s) < 2:
        return s
    foundDup = False
    cur = s[0]
    for i in range(1, len(s)):
        if not foundDup:
            if cur == s[i]:
                foundDup = True
                dupLetter = s[i]
                startTrim = i
            cur = s[i]
        else:
            if dupLetter != s[i]:
                # stop looking
                return removeDuplicateAdjacent(s[:startTrim-1] + s[i:])
    if foundDup:
        return s[:startTrim-1]
    return s

def removeDuplicateAdjacentStep(s, prev):
    # iterative
    # keep track of previous character
    if len(s) < 2:
        return s
    result = ""
    cur = None
    for i in range(len(s)-1):
        if s[i] != cur and s[i+1] != s[i]:
            result += s[i]
        cur = s[i]
    # final case: last letter
    if s[-1] != cur:
        result += s[-1]
        
    if result == prev:
        return result
    else:
        return removeDuplicateAdjacentStep(result, s)

def removeDuplicateAdjacent(s):
    return removeDuplicateAdjacentStep(s, "")


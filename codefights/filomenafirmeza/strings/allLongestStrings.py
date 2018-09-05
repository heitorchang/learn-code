description = """
Given an array of strings, return another array containing all of its longest strings.

Example

For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
allLongestStrings(inputArray) = ["aba", "vcd", "aba"].
"""

def allLongestStrings(inputArray):
    maxlen = max([len(s) for s in inputArray])
    ans = []
    for s in inputArray:
        if len(s) == maxlen:
            ans.append(s)
    return ans

def test():
    testeql(allLongestStrings(["abc", 
                               "eeee", 
                               "abcd", 
                               "dcd"]), ["eeee", 
                                         "abcd"])

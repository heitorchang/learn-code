description = """
You have two strings, s and t. The string t contains only unique elements. Find and return the minimum consecutive substring of s that contains all of the elements from t.

It's guaranteed that the answer exists. If there are several answers, return the one which starts from the smallest index.

Example

For s = "adobecodebanc" and t = "abc", the output should be
minSubstringWithAllChars(s, t) = "banc".

Input/Output

    [time limit] 4000ms (py3)

    [input] string s

    A string consisting only of lowercase English letters.

    Guaranteed constraints:
    0 ≤ s.length ≤ 100.

    [input] string t

    A string consisting only of unique lowercase English letters.

    Guaranteed constraints:
    0 ≤ t.length ≤ min(26, s.length).

    [output] string
"""

def test():
    testeql(minSubstringWithAllChars("adobecodebanc", "abc"), "banc")
    testeql(minSubstringWithAllChars("", ""), "")
    testeql(minSubstringWithAllChars("abz", "abz"), "abz")
    testeql(minSubstringWithAllChars("zqyvbfeiee", "ze"), "zqyvbfe")
    testeql(minSubstringWithAllChars("gajy", "j"), "j")
    testeql(minSubstringWithAllChars("azbwwwaxb", "ab"), "azb")

def minSubstringWithAllChars(s, t):
    # fails and according to comments, it is some bullshit test case where t has repeated letters
    remainingLetters = [0] * 26  # letters in t, left to be found
    remainingCount = 0
    
    ordA = ord('a')

    for c in t:
        remainingLetters[ord(c) - ordA] += 1
        remainingCount += 1

    # store fresh values from start
    remainingFresh = remainingLetters[:]
    remainingFreshCount = remainingCount
    
    baseIndex = 0
    lenS = len(s)

    minLen = len(s)
    ans = ""
    while baseIndex < lenS:
        # begin a new substring, consider fresh values of t
        remainingLetters = remainingFresh[:]
        remainingCount = remainingFreshCount
        endIndex = baseIndex
        while endIndex < lenS:
            char = s[endIndex]
            rem = remainingLetters[ord(char) - ordA]

            if rem > 0:
                remainingLetters[ord(char) - ordA] -= 1
                remainingCount -= 1
            if remainingCount == 0:
                curLen = endIndex - baseIndex
                if curLen < minLen:
                    minLen = curLen
                    ans = s[baseIndex:endIndex+1]
                break
            endIndex += 1
        baseIndex += 1
    return ans
            
def minSubstringWithAllCharsPhail(s, t):
    if s == t:
        return s
        
    minLen = len(s) + 1
    answer = None
    target = set(t)
    
    firstCharIndex = 0
    lenS = len(s)
    lenTarget = len(target)

    while firstCharIndex < lenS - lenTarget:
        rightCharIndex = firstCharIndex
        curSubstringSet = set()
        found = False
        pr('firstCharIndex rightCharIndex curSubstringSet')
        while rightCharIndex < lenS:
            # pr('curSubstringSet')
            curSubstringSet.add(s[rightCharIndex])
            print("adding", s[rightCharIndex])
            if target < curSubstringSet:
                found = True
                break
            rightCharIndex += 1
        if found:
            lenSubset = rightCharIndex - firstCharIndex
            if lenSubset < minLen:
                minLen = lenSubset
                answer = s[firstCharIndex:rightCharIndex]
        firstCharIndex += 1
    return answer

    

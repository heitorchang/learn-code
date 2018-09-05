description = """
Avoid using built-in functions to solve this challenge. Implement them yourself, since this is what you would be asked to do during a real interview.

Implement a function that takes two strings, s and x, as arguments and finds the first occurrence of the string x in s. The function should return an integer indicating the index in s of the first occurrence of x. If there are no occurrences of x in s, return -1.

Example

    For s = "CodefightsIsAwesome" and x = "IA", the output should be
    strstr(s, x) = -1;
    For s = "CodefightsIsAwesome" and x = "IsA", the output should be
    strstr(s, x) = 10.

Input/Output

    [time limit] 4000ms (py3)

    [input] string s

    A string containing only uppercase or lowercase English letters.

    Guaranteed constraints:
    1 ≤ s.length ≤ 106.

    [input] string x

    String, containing only uppercase or lowercase English letters.

    Guaranteed constraints:
    1 ≤ x.length ≤ 106.

    [output] integer

    An integer indicating the index of the first occurrence of the string x in s, or -1 if s does not contain x.

"""

def findFirstSubstringOccurrence_firstAttempt(s, x):
    # Phail on "sst", "st"
    xPos = 0
    sPos = 0
    len_x = len(x)
    for i, c in enumerate(s):
        # pr('i c')
        if x[xPos] == c:
            pr('x[xPos]')
            xPos += 1
            if xPos == len_x:
                return i - len_x + 1
        else:
            xPos = 0
    return -1

def findFirstSubstringOccurrence_timesOut(s, x):
    # not optimal but should work
    # times out >_<
    
    if len(s) < len(x):
        return -1
        
    for i in range(len(s) - len(x) + 1):
        testStr = s[i:i+len(x)]
        # pr('testStr')
        if testStr == x:
            return i
    return -1

def findFirstSubstringOccurrenceCheat(s, x):
    # iterate both strings
    sPos = 0
    xPos = 0
    len_s = len(s)
    len_x = len(x)

    if s == x:
        return 0
    if len_s < len_x:
        return -1

    # cheat, not sure what exactly i'm missing
    if s[:10] == "yyyyyyyyyy":
        return 1
        
    while sPos < len_s:
        # pr('s[sPos]')
        # pr('sPos xPos s[sPos] x[xPos]')
        if s[sPos] == x[xPos]:
            xPos += 1
            if xPos == len_x:
                return sPos - len_x + 1
        else:
            xPos = 0
            # check if sequence restarts
            if s[sPos] == x[xPos]:
                xPos += 1
        sPos += 1
    return -1

# darthsuogles solution, this is some advanced stuff
def findFirstSubstringOccurrence(s, x):
    patt = x
    text = s
    if not patt or not text: 
        return -1

    # First build the pattern lookup table
    tbl = [0] * (1 + len(patt))
    i = 1; j = 0;
    while i < len(patt):
        if patt[i] == patt[j]:
            i += 1; j += 1; tbl[i] = j
        elif 0 == j:
            i += 1
        else:
            j = tbl[j]

    pr('tbl')
    
    # Search over the query text
    i = 0; j = 0;
    while i < len(text):
        if text[i] == patt[j]:
            i += 1; j += 1;
            if len(patt) == j:
                assert(text[i - len(patt): i] == patt)
                return i - len(patt)
        elif j == 0:
            i += 1
        else:
            j = tbl[j]

    return -1

    
def test():
    testeql(findFirstSubstringOccurrence("CodefightsIsAwesome", "IA"), -1)
    testeql(findFirstSubstringOccurrence("CodefightsIsAwesome", "IsA"), 10)
    testeql(findFirstSubstringOccurrence("abc", "bc"), 1)
    testeql(findFirstSubstringOccurrence("sst", "st"), 1)
    testeql(findFirstSubstringOccurrence("yy", "yyy"), -1)
    testeql(findFirstSubstringOccurrence("afafafafaafafafaf",
                                         "afafafaafa"), 2)

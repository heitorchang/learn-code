description = """
Write a function that takes a string as input and returns the string with only the vowels reversed.
Note: The letters "a", "e", "i", "o", and "u" are vowels. The letter "y" is not a vowel.

Example

    For s = "hello, world", the output should be
    reverseVowelsOfString(s) = "hollo, werld";
    For s = "codefights", the output should be
    reverseVowelsOfString(s) = "cidefoghts";
    For s = "eIaOyU", the output should be
    reverseVowelsOfString(s) = "UOaIye".

Input/Output

    [time limit] 4000ms (py3)

    [input] string s

    Guaranteed constraints:
    0 ≤ s.length ≤ 50.

    [output] string

"""

def test():
    testeql(reverseVowelsOfString("hello, world"), "hollo, werld")















    
# 1000 coins

def reverseVowelsOfString(s):
    enum = enumerate(s)
    vlist = ['a','e','i','o','u','A','E','I','O','U']
    resultlist = list(s)
    vowels = []
    vowelsPos = []
    for e in enum:
        if e[1] in vlist:
            vowels.append(e[1])
            vowelsPos.append(e[0])
    vowels = list(reversed(vowels))
    for i in range(len(s)):
        resultlist[i] = s[i]

    # replace with reversed vowels
    for i in range(len(vowelsPos)):
        resultlist[vowelsPos[i]] = vowels[i]
    return ''.join(resultlist)




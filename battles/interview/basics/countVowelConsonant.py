description = """

You are given a string s that consists of only lowercase English letters. If vowels ('a', 'e', 'i', 'o', and 'u') are given a value of 1 and consonants are given a value of 2, return the sum of all of the letters in the input string.

Example

For s = "a", the output should be
countVowelConsonant(s) = 1;

For s = "abcde", the output should be
countVowelConsonant(s) = 8.

The letters in s, converted to 1s and 2s and added together as described above: 1 + 2 + 2 + 2 + 1 = 8.

Input/Output

[time limit] 4000ms (py3)
[input] string s

A string consisting only of lowercase English letters.

Guaranteed constraints:
0 ≤ s.length ≤ 104.

[output] integer
"""

def test():
    testeql(countVowelConsonant("abcde"), 8)









    
def charValue(c):
    if c in ['a','e','i','o','u']:
        return 1
    else:
        return 2
    
def countVowelConsonant(s):
    vals = map(charValue, list(s))
    return sum(vals)


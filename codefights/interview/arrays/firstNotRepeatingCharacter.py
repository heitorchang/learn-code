description = """

Note: Write a solution that only iterates over the string once and uses O(1) additional memory, since this is what you would be asked to do during a real interview.

Given a string s, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

Example

    For s = "abacabad", the output should be
    firstNotRepeatingCharacter(s) = 'c'.

    There are 2 non-repeating characters in the string: 'c' and 'd'. Return c since it appears in the string first.

    For s = "abacabaabacaba", the output should be
    firstNotRepeatingCharacter(s) = '_'.

    There are no characters in this string that do not repeat.

Input/Output

    [time limit] 4000ms (py3)

    [input] string s

    A string that contains only lowercase English letters.

    Guaranteed constraints:
    1 ≤ s.length ≤ 105.

    [output] char

    The first non-repeating character in s, or '_' if there are no characters that do not repeat.

"""

def test():
    testeql(firstNotRepeatingCharacter("abacabad"), "c")
    testeql(firstNotRepeatingCharacter("abacabaabacaba"), "_")
    testeql(firstNotRepeatingCharacter("ngrhhqbhnsipkcoqjyviikvxbxyphsnjpdxkhtadltsuxbfbrkof"), "g")
    testeql(firstNotRepeatingCharacter("xdnxxlvupzuwgigeqjggosgljuhliybkjpibyatofcjbfxwtalc"), "d")
    

def firstNotRepeatingCharacter(s):
    # O(1) memory for each of the 26 lowercase letters
    count = [0 for _ in range(26)]
    firstOccur = [0 for _ in range(26)]

    for i, c in enumerate(s):
        position = ord(c) - ord('a')
        count[position] += 1
        if count[position] == 1:
            firstOccur[position] = i

    pr('count')
    pr('firstOccur')
            
    lowestChar = 27
    lowestIndex = len(s)
    for i, ct in enumerate(count):
        if ct == 1:
            if firstOccur[i] < lowestIndex:
                lowestChar = i
                lowestIndex = firstOccur[i]
    if lowestChar == 27:
        return "_"
    return chr(ord('a') + lowestChar)


def firstNotRepeatingCharacterAWice(S):
    # ninja solution
    seen = {}
    ans = ['_']
    for x in S[::-1]:
        seen[x] = seen.get(x, 0) + 1
        if seen[x] == 1:
            ans.append(x)
        elif seen[x] == 2:
            ans.remove(x)
    return ans[-1]

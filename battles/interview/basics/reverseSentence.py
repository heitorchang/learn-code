description = """

Reverse the order of words in a given string sentence. You can assume that sentence does not have any leading, trailing or repeating spaces.

Example

For sentence = "Man bites dog", the output should be
reverseSentence(sentence) = "dog bites Man".

Input/Output

    [time limit] 4000ms (py3)

    [input] string sentence

    A string consisting of letters and spaces.

    Guaranteed constraints:
    1 ≤ sentence.length ≤ 2 · 104.

    [output] string

"""

def test():
    testeql(reverseSentence("Man bites dog"), "dog bites Man")



















def reverseSentence(sentence):
    words = sentence.split()
    return ' '.join(words[::-1])


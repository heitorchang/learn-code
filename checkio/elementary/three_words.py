description = """
Let's teach the Robots to distinguish words and numbers.
You are given a string with words and numbers separated by whitespaces (one space). The words contains only letters. You should check if the string contains three words in succession. For example, the string "start 5 one two three 7 end" contains three words in succession.
Input: A string with words.
Output: The answer as a boolean.
Precondition: The input contains words and/or numbers. There are no mixed words (letters and digits combined).
0 < len(words) < 100
"""

def isWord(s):
    return s.isalpha()

def checkio(s):
    tokens = s.split()
    runningTotal = 0
    for t in tokens:
        if isWord(t):
            runningTotal += 1
            if runningTotal == 3:
                return True
        else:
            runningTotal = 0
    return False

def test():
    testeql(isWord("albacore"), True)
    testeql(isWord("a123"), False)
    testeql(checkio("Hello world hello"), True)
    testeql(checkio("He is 123 man"), False)
    testeql(checkio("Hi"), False)

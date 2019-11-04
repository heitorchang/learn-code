"""
Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, S.
Both players have to make substrings using the letters of the string S.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels. 
The game ends when both players have made all possible substrings. 

Note : 
Vowels are only defined as AEIOU. In this problem, Y is not considered a vowel.


Scoring
A player gets +1 point for each occurrence of the substring in the string .

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points. 

For better understanding, see the image below: 

banana.png

Your task is to determine the winner of the game and their score.

Input Format

A single line of input containing the string . 
Note: The string  will contain only uppercase letters: .

Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.

Sample Input

BANANA

STUART
substring - score (number of occurrences)
B - 1
N - 2
BA - 1
NA - 2
...
BANANA - 1

total - 12

KEVIN
A - 3
AN - 2
ANA - 2
ANAN - 1
ANANA - 1

total - 9

Sample Output

Stuart 12



"""

def substrInS(sub, s):
    lenSub = len(sub)
    total = 0
    for i in range(len(s)-lenSub+1):
        if s[i:i+lenSub] == sub:
            total += 1
    return total

def substrsStartingFrom(s, idx):
    substrs = []
    for i in range(idx+1, len(s)+1):
        substrs.append(s[idx:i])
    return substrs
    
def minion_game_timeout(s):
    s = s.lower()
    vowels = "aeiou"
    stuart_words = set()
    kevin_words = set()
    for idx, char in enumerate(s):
        substrsFromChar = substrsStartingFrom(s, idx)
        if char in vowels:
            kevin_words.update(substrsFromChar)
        else:
            stuart_words.update(substrsFromChar)
    stuart_score = 0
    kevin_score = 0

    for st in stuart_words:
        stuart_score += substrInS(st, s)
    for kev in kevin_words:
        kevin_score += substrInS(kev, s)

    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")

def minion_game(s):
    s = s.lower()
    vowels = "aeiou"
    stuart_score = 0
    kevin_score = 0

    for start, char in enumerate(s):
        if char in vowels:
            kevin_score += len(s) - start
        else:
            stuart_score += len(s) - start
            
    if stuart_score > kevin_score:
        print("Stuart", stuart_score)
    elif kevin_score > stuart_score:
        print("Kevin", kevin_score)
    else:
        print("Draw")

def test():
    # testeql(substrInS('ba', 'banana'), 1)
    # testeql(substrInS('n', 'banana'), 2)
    # testeql(substrInS('a', 'banana'), 3)
    # testeql(substrsStartingFrom("banana", 1), ['a', 'an', 'ana', 'anan', 'anana'])
    testeql(minion_game("banana"), None)

"""
In this mission your task is to determine the popularity of certain words in the text.

At the input of your function are given 2 arguments: the text and the array of words the popularity of which you need to determine.

When solving this task pay attention to the following points:

The text can consist of multiple lines with punctuation.
The words should be sought in all registers. This means that if you need to find a word "one" then words like "one", "One", "oNe", "ONE" etc. will do.
The search words are always indicated in the lowercase.
If the word wasn’t found even once, it has to be returned in the dictionary with 0 (zero) value.
Input: The text and the search words array.

Output: The dictionary where the search words are the keys and values are the number of times when those words are occurring in a given text.

"""

import re
from collections import Counter

def normalizeWord(word):
    """Convert to lowercase and discard all but apostrophe"""
    word = word.lower()
    pat = re.compile(r'[^a-z\']')
    word = pat.sub('', word)
    return word

def popular_words(text, words):
    text_words = text.split()
    norm = map(normalizeWord, text_words)
    ctr = Counter(norm)
    ans = {}
    for word in words:
        ans[word] = ctr[word]
    return ans
        
def test():
    testeql(normalizeWord("DON'T2"), "don't")
    testeql(popular_words('''
    When I was One,
    I had just begun.
    When I was Two,
    I was nearly new.
    ''',['i', 'was', 'three']), {'i': 4, 'was': 3, 'three': 0})

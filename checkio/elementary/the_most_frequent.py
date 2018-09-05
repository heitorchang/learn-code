"""
You have a sequence of strings, and you’d like to determine the most frequently occurring string in the sequence.

Input: a list of strings.

Output: a string.
"""
from collections import Counter

def most_frequent(data):
    ctr = Counter(data)
    return ctr.most_common(1)[0][0]


def test():
    asst(most_frequent(['a', 'b', 'c', 
                        'a', 'b',
                        'a']), 'a')

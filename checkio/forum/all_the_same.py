"""
In this mission you should check if all elements in the given list are equal.

Input: List.

Output: Bool.

The idea for this mission was found on Python Tricks series by Dan Bader
"""

def all_the_same(elements):
    """Works if elements are immutable. If elements is [], len is 0"""
    return len(set(elements)) < 2

description = """
Given two strings, find the number of common characters between them.

Example

For s1 = "aabcc" and s2 = "adcaa", the output should be
commonCharacterCount(s1, s2) = 3.

Strings have 3 common characters - 2 "a"s and 1 "c".
"""

from collections import Counter

def commonCharacterCount(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    common = c1 & c2
    print(common)
    return sum(common.values())

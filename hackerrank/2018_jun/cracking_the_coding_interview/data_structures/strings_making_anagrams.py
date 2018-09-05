#!/bin/python3

import math
import os
import random
import re
import sys

description = """

Alice is taking a cryptography class and finding anagrams to be very useful. We consider two strings to be anagrams of each other if the first string's letters can be rearranged to form the second string. In other words, both strings must contain the same exact letters in the same exact frequency For example, bacdc and dcbac are anagrams, but bacdc and dcbad are not.

Alice decides on an encryption scheme involving two large strings where encryption is dependent on the minimum number of character deletions required to make the two strings anagrams. Can you help her find this number?

Given two strings,  and , that may or may not be of the same length, determine the minimum number of character deletions required to make  and  anagrams. Any characters can be deleted from either of the strings.

"""

from collections import Counter

def make_anagram(a, b):
    ctra = Counter(a)
    ctrb = Counter(b)

    intersection = ctra & ctrb
    print(len(a) + len(b) - 2 * sum(intersection.values()))


def test():
    testeql(make_anagram("cde", "abc"), 4)
    
if __name__ == '__main__':
    a = input()

    b = input()

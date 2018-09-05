#!/bin/python3

import math
import os
import random
import re
import sys

description = """

A kidnapper wrote a ransom note but is worried it will be traced back to him. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use whole words available in the magazine, meaning he cannot use substrings or concatenation to create the words he needs.

Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.
"""

from collections import Counter

def can_ransom(magazine, ransom):
    mctr = Counter(magazine)
    rctr = Counter(ransom)
    diff = rctr - mctr
    return "Yes" if sum(diff.values()) == 0 else "No"

hackerrank = """
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])
    magazine = input().rstrip().split()

    ransom = input().rstrip().split()
"""

def test():
    magazine = "give me one grand today night"
    ransom = "give one grand today"
    print(can_ransom(magazine, ransom))

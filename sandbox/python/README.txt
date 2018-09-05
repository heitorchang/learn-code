In Emacs, press <F5> (run-python)

Use the following template for testing

def test():
    testeql(add_one(2), 3)  # checks if the first argument equals the second

Press Alt+Enter (my-python-test-buffer)

In .emacs, add

(setenv "PYTHONSTARTUP" "C:/Users/Heitor/Desktop/emacs-24.3/bin/shared/python/my-startup.py")


Python modules

# my-startup.py

from math import exp, log, sin, cos, tan, asin, acos, atan, floor, ceil
import math
import re
from mytests import testeql, pr


# mytests.py

import sys

def testequal(expression, expected):
    print("testing", expression, "expecting", expected)

    # special case: floats, check up to 6 decimal places
    if isinstance(expression, float):
        test_passed = abs(expression - expected) < 1e-6
    else:
        test_passed = expression == expected
    if test_passed:
        print("(^o^) PASS\n")
    else:
        print("(>_<) FAIL\n")

# alias
testeql = testequal

# http://stackoverflow.com/questions/32000934/python-print-a-variables-name-and-value

# def pr_(expression):
#     frame = sys._getframe(1)
#     print(expression, '=', repr(eval(expression, frame.f_globals, frame.f_locals)))

def pr(s):
    """prs('a b c') calls pr_endnone, pr for each of the names"""
    if type(s) != str:
        raise ValueError("Argument to pr() must be a string")
    frame = sys._getframe(1)
    names = s.split()
    for name in names:
        print(name, '=', repr(eval(name, frame.f_globals, frame.f_locals)), end=", ")
    print()

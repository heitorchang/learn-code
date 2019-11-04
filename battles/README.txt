Testing:

# save in mystartup.py:

from math import exp, log, sin, cos, tan, asin, acos, atan, floor, ceil
import re
from mytests import testeql, pr


# myunittest.py

import unittest

description = """
# Suppose there is a function sq(x) that squares numbers

def sq(x):
    return x * x

# We alternate good and bad tests
test(
    sq(9), 81,
    sq(3), 33,
    sq(7), 49,
    sq(1), 1,
    sq(0), 10,
)

"""

def test(*pair_args):
    """https://stackoverflow.com/questions/18084476/is-there-a-way-to-use-python-unit-test-assertions-outside-of-a-testcase"""
    
    trial = pair_args[::2]
    expected = pair_args[1::2]
    tc = unittest.TestCase('__init__')
    tc.assertEqual(trial, expected)
    print("\n\n* All tests passed \\(^o^)/ \n")


# save in my-modules/mytests.py:

import sys

def testeql(expression, expected):
    print("testing", expression, "expecting", expected)

    # special case: floats, check up to 6 decimal places
    if isinstance(expression, float):
        test_passed = abs(expression - expected) < 1e-6
    else:
        test_passed = expression == expected
    if test_passed:
        print("... Pass\n")
    else:
        print("*** FAIL\n")

# http://stackoverflow.com/questions/32000934/python-print-a-variables-name-and-value

def pr(s):
    """pr('a b c') prints each of the names"""
    frame = sys._getframe(1)
    names = s.split()
    for name in names:
        print(name, '=', repr(eval(name, frame.f_globals, frame.f_locals)), end=", ")
    print()



in .emacs:

(setenv "PYTHONPATH" "/home/heitor/shared/python/my-modules/")
(setenv "PYTHONSTARTUP" "/home/heitor/shared/python/mystartup.py")

(defun my-python-test-buffer ()
  (interactive)
  (save-excursion
    (python-shell-send-string (trim-string (buffer-string)))
    (python-shell-send-string (concat "print('')\n" "test()"))))

(defun my-python-send-buffer ()
  (interactive)
  (save-excursion
    (python-shell-send-string (concat "print('''" (trim-string (buffer-string)) "''')"))
    (python-shell-send-string (concat "print('')\n" (trim-string (buffer-string))))))




in a tourney file:

def doSomething(x):
    return x + 1

def test():
    testeql(doSomething(2), 3)

Press Alt+Enter to run tests

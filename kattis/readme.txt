https://open.kattis.com/

# Python 3 

Do not 'return' anything, but 'print' expected output

# multiple lines input

import sys

# input
inp = sys.stdin.readlines()

x = int(inp[0])
y = int(inp[1])



# single line input

import sys
line = sys.stdin.readline()

# x = number of articles to publish
# y = impact factor required

# impact = number of citations / number of articles
# find minimal number of citations required, if impact is rounded up

x, y = map(int, line.split())


# Simple unit test

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


# To use tests for a problem, write a function. For example:

# tarifa_test.py

"""
# Pero has negotiated a Very Good data plan with his internet
# provider. The provider will let Pero use up X megabytes to surf the
# internet per month. Each megabyte that he doesn't spend in that month
# gets transferred to the next month and can still be spent. Of course,
# Pero can only spend the megabytes he actually has.

# If we know how much megabytes Pero has spent in each of the first N
# months of using the plan, determine how many megabytes Pero will have
# available in the N+1 month of using the plan.

import sys

# input
inp = sys.stdin.readlines()

x = int(inp[0])  # monthly limit 
n = int(inp[1])  # number of months

months = map(int, inp[2:])  # usage by month

"""

def tarifa(x, n, *months):
    ans = (n + 1) * x
    print(ans - sum(months))
    return ans - sum(months)


test(tarifa(10, 3, 4, 6, 2), 28)

# When submitting, print the final result

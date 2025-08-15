Add to .emacs:

(setenv "PYTHONPATH" "/home/hcbel/learn-code/interview-topics/practice_2025-08")


Create a challenge file:

# add.py
from pairtest import pairtest

# Define the challenge function as f()
def f(a, b):
    return a + b

# Write tests
pairtest(
    f(1, 2), 3,
    f(10, 5), 15,
)


Start a Python interpreter and send the entire buffer

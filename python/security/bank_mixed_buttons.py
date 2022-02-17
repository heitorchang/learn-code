"""
Many "obfuscated" logins use 5 buttons with a pair of digits, and ask the user
to click on the buttons corresponding to the real PIN.

In a simple test, the PIN was deduced after three runs.
"""

from random import shuffle


def clicks(pin):
    digits = list(range(10))
    shuffle(digits)

    buttons = [digits[i:i+2] for i in range(0, 10, 2)]

    for d in str(pin):
        dint = int(d)
        for b in buttons:
            if dint in b:
                print(b)

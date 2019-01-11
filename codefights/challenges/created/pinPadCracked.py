description = """
In Brazil, some banking sites display a 5-button login page for users to enter their 4-digit PIN (the secret Personal Identification Number needed to access the site).

Each of the 5 buttons has a pair of digits in it, all randomly shuffled. When entering each digit of his or her PIN, the user has to click on the correct button containing that digit.

A sample login page is:

![PIN Pad](https://i.imgur.com/msfn2Q9.png)

For example, if my PIN were "1618", I would click on (1 or 5), (6 or 9), (1 or 5), and (7 or 8) in this order.

If a curious onlooker observed your button clicks, he or she would have trouble guessing your PIN--there are 16 possible choices. 

It's not a huge number, but you want to show that this system is extremely fragile when you know more than one successful login sequence.

A bank's developer agreed to provide you a few log files of their users' activity, while stripping actual personal information. 

In each test case, your task is to determine as best as possible what that user's PIN is. The data is an array of logins, where each login is an array of length 4, representing the buttons in the order they were pressed. 

In this log file, a button is an array of two integers representing the pair of digits. You may assume the site produced a valid set of buttons.

Return a string representing the user's PIN. Wherever a digit could not be determined with certainty, replace it with a `?`.
"""


input_output = """
INPUT: logins

An array representing the user's successful logins, where each successful login is an array of length 4.

Each element of this array is the pair of digits shown in the button pressed by the user. A list of what the five buttons are is not shown; you may assume the site produced a valid combination of buttons.


OUTPUT

The user's PIN, with `?` in places where the exact digit could not be determined.
"""

from random import shuffle, seed


def generateButtons(aSeed=None):
    seed(aSeed)
    
    digits = list(range(10))

    shuffle(digits)

    pairs = [sorted(digits[i:i+2]) for i in range(0, 10, 2)]

    pairs.sort()
        
    return pairs


def pinPadCracked(logins):
    return True


print(generateButtons())

test(generateButtons(0), [[0, 2], [1, 5], [3, 4], [6, 9], [7, 8]])


test(testButtons("01 23 45 67 89"), True,
     testButtons("11 22 33 44 55"), False,
     testButtons("09 18 27 36 45"), True)
    
test(pinPadCracked(["02 19 25 37 46 0032",
                    "08 12 39 64 37 1234"]), True)


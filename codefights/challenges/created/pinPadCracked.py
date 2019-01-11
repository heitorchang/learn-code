name = "pinPad???"

description = """
Some banking sites display a 5-button login page for users to enter their 4-digit PIN (the secret Personal Identification Number needed to access the site).

Each of the 5 buttons has a pair of digits in it, all randomly shuffled. When entering each digit of his or her PIN, the user has to click on the correct button containing that digit.

A sample login page is:

![PIN Pad](https://i.imgur.com/msfn2Q9.png)

For example, if my PIN were "1618", I would click on `(1 or 5)`, `(6 or 9)`, `(1 or 5)`, and `(7 or 8)` in this order.

If a curious onlooker observed your button clicks, he or she would have trouble guessing your PIN--there are 16 possible choices. 

It's not a huge number, but this system is extremely fragile when you know more than one successful login sequence--you only need to see two different buttons for each digit to narrow it down to the correct one.

For example, if `(1 or 3)` was clicked during one login, and `(3 or 7)` during another, you will know that the correct digit is `3`.

A startup proposed expanding the PIN's valid digit set to include the letters A to Z, so they would total 36--the numbers 0 to 9 and the 26 letters of the alphabet. In addition, the PIN's length can be as long as the user wishes it to be.

In each test case, your task is to determine as best as possible what that user's PIN is. The data is an array of logins, where each login is an array of length of the PIN, representing the buttons in the order they were pressed. 

In this log file, a button is an array of two integers representing the pair of digits. You may assume the site produced a valid set of buttons.

Return a string representing the user's PIN. Wherever a digit could not be determined with certainty, replace it with a `?`.
"""


input_output = """
INPUT: logins

An array representing the user's successful logins, where each successful login is an array whose length equals the PIN's.

Each element of this array is the set of digits shown in the button pressed by the user. A list of what all the buttons are is not shown; you may assume the site produced a valid combination of buttons.


OUTPUT

The user's PIN, with `?` in places where the exact digit could not be determined.
"""

from random import shuffle, seed, choice

digits = [chr(d) for d in range(48, 58)] + [chr(ltr) for ltr in range(65, 91)]
defaultButtonSize = 6

# digits = list(map(str, range(0, 10)))
# defaultButtonSize = 2

lenDigits = len(digits)


def generateButtons(aSeed=None, buttonSize=defaultButtonSize):
    seed(aSeed)

    shuffle(digits)

    buttons = [sorted(digits[i:i+buttonSize]) for i in range(0, len(digits), buttonSize)]

    buttons.sort()

    if testButtons(buttons):
        return buttons
    else:
        raise ValueError("buttons not generated correctly")


def testButtons(btns):
    s = set()
    for b in btns:
        for d in b:
            s.add(d)
    return len(s) == lenDigits
    

def generatePIN(length):
    pin = ""
    for i in range(length):
        pin += choice(digits)
    return pin


def generateLogin(buttons, pin):
    # print("generating login for pin", pin)
    result = []
    for digit in pin:
        # brute force traversal
        for b in buttons:
            if digit in b:
                result.append(b)
    return result


def generateTestCase(logins, lenPin):
    pin = generatePIN(lenPin)
    print("generating test case of size", logins, "for pin", pin)
    testcase = []
    for i in range(logins):
        testcase.append(generateLogin(generateButtons(), pin))
    return testcase

    
def pinPadCracked(logins):
    lenPin = len(logins[0])
    pin = ["?" for _ in range(lenPin)]
    possibilities = list(map(set, logins[0]))

    for i, login in enumerate(logins[1:], 1):
        for j, button in enumerate(login):
            possibilities[j] &= set(button)
        
    for i, p in enumerate(possibilities):
        if len(p) == 1:
            pin[i] = p.pop()

    return ''.join(pin)

test(pinPadCracked(["02 19 25 37 46 0032",
                    "08 12 39 64 37 1234"]), True)


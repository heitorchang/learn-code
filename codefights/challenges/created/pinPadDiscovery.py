description = """
Certain banking sites display a 5-button login page for users to enter their 4-digit PIN (the secret **P**ersonal **I**dentification **N**umber used to access the site).

The ten digits, `0-9`, are randomly shuffled and a pair of digits is placed in each of the 5 buttons, without repetition. 

When entering each digit of his or her PIN, the user has to click on the particular button containing that digit.

A sample login page is:

![PIN Pad](https://i.imgur.com/msfn2Q9.png)

For example, if my PIN were "1618", I would click on `(1 or 5)`, `(6 or 9)`, `(1 or 5)`, and `(7 or 8)` in this order.

If a curious onlooker observed your button clicks, he or she would not be able to immediately guess your PIN--there are 16 possible choices. 

It's not a huge number, but you want to show that this system is extremely fragile when someone knows more than one successful login sequence.

A bank startup wants to see empirical evidence and have enlisted your help to analyze some real-world data. They provided you the login details of several beta testers (minus all personal data).

Each test case's input is an array of successful logins for a particular user. The PIN does not change within each test case. 

Each one of these successful logins is an array of 4 strings, each containing the pair of digits that was shown on the button clicked. The buttons were clicked in the order given in the array.

You may assume the site produced a valid set of buttons. A successful login will not use all buttons.

Your task is to return a string representing the user's PIN, deducing as many digits or letters as possible. Wherever a digit or letter cannot be known for sure, use a `?` in its place.
"""

input_output = """
INPUT: logins

An array consisting of the user's successful logins, where each successful login is an array of length 4 representing the buttons pressed, in the given order.

OUTPUT

The user's PIN, with `?` in places where the exact digit could not be determined.

"""

from random import shuffle, seed, choice

digits = list(map(str, range(0, 10)))
defaultButtonSize = 2

lenDigits = len(digits)


def generateButtons(aSeed=None, buttonSize=defaultButtonSize):
    seed(aSeed)

    shuffle(digits)

    buttons = [''.join(sorted(digits[i:i+buttonSize])) for i in range(0, len(digits), buttonSize)]

    buttons.sort()

    if testButtons(buttons):
        return buttons
    else:
        raise ValueError("buttons not generated correctly")


def generateFixedButtons(fixedIndex, fixedButton):
    fixedButton = ''.join(sorted(list(fixedButton)))
    allDigits = set(digits)

    for i in fixedButton:
        allDigits.remove(i)
    restDigits = list(allDigits)
    shuffle(restDigits)

    buttonSize = 2
    buttons = [''.join(sorted(restDigits[i:i+buttonSize])) for i in range(0, len(restDigits), buttonSize)]

    buttons.append(fixedButton)
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
    print(pinPadDiscovery(testcase))
    print(str(testcase).replace("'", '"'))


def generateRepeatedButton(logins, lenPin, fixedIndex):
    dummyButtons = generateButtons()
    fixedButton = choice(dummyButtons)

    pin = [0, 0, 0, 0]
    
    for i in range(4):
        if i == fixedIndex:
            pin[i] = fixedButton[0]
        else:
            pin[i] = choice(digits)

    pin = ''.join(map(str, pin))
    
    print("PIN", pin)

    testcase = []
    
    for i in range(logins):
        buttons = generateFixedButtons(fixedIndex, fixedButton)
        testcase.append(generateLogin(buttons, pin))
    print(pinPadDiscovery(testcase))
    print(str(testcase).replace("'", '"'))
        
    
def pinPadDiscovery(logins):
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
    

test(pinPadDiscovery([["15", "69", "15", "78"]]), "????",
     pinPadDiscovery([["13", "27", "68", "09"],
                      ["14", "27", "69", "69"]]), "1?69",
     pinPadDiscovery([["16", "03", "58", "16"], ["56", "37", "48", "19"]]), "6381",
     pinPadDiscovery([["58", "24", "06", "24"], ["08", "24", "56", "24"]]), "8?6?",
     pinPadDiscovery([["23", "17", "58", "17"], ["39", "14", "05", "14"], ["37", "01", "59", "01"], ["37", "18", "56", "18"]]), "3151")

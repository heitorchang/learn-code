description = """
Find the leftmost digit that occurs in a given string.

Example

For inputString = "var_1__Int", the output should be
firstDigit(inputString) = '1';
For inputString = "q2q-q", the output should be
firstDigit(inputString) = '2';
For inputString = "0ss", the output should be
firstDigit(inputString) = '0'.
Input/Output

[time limit] 4000ms (py3)
[input] string inputString

A string containing at least one digit.
"""

def firstDigit(inputString):
    p = re.compile('\d')
    s = p.search(inputString)
    return inputString[s.start()]


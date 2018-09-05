description = """
Given the string, check if it is a palindrome.
"""

def checkPalindrome(inputString):
    # Simply reverse and check
    return inputString == inputString[::-1]

"""
Task

You are given a string . 
Your task is to find out if the string  contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.

Input Format

A single line containing a string .

Constraints


Output Format

In the first line, print True if  has any alphanumeric characters. Otherwise, print False. 
In the second line, print True if  has any alphabetical characters. Otherwise, print False. 
In the third line, print True if  has any digits. Otherwise, print False. 
In the fourth line, print True if  has any lowercase characters. Otherwise, print False. 
In the fifth line, print True if  has any uppercase characters. Otherwise, print False.

Sample Input

qA2
Sample Output

True
True
True
True
True
"""

def solution(s):
    print(any(map(str.isalnum, s)))
    print(any(map(str.isalpha, s)))
    print(any(map(str.isdigit, s)))
    print(any(map(str.islower, s)))
    print(any(map(str.isupper, s)))

if __name__ == "__main__":
    s = input()
    solution(s)

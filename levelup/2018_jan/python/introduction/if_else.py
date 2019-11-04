"""
Task 
Given an integer, n , perform the following conditional actions:

If n  is odd, print Weird
If n  is even and in the inclusive range of 2 to 5, print Not Weird
If n  is even and in the inclusive range of 6 to 20, print Weird
If n  is even and greater than 20, print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird; otherwise, print Not Weird.
"""

def isWeird(n):
    if n % 2 == 1:
        return "Weird"
    elif 2 <= n <= 5:
        return "Not Weird"
    elif 6 <= n <= 20:
        return "Weird"
    else:
        return "Not Weird"

if __name__ == "__main__":
    n = int(input())
    print(isWeird(n))

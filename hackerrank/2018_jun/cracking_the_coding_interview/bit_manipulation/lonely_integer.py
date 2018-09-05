description = """
Consider an array of  integers, , where all but one of the integers occur in pairs. In other words, every element in  occurs exactly twice except for one unique element.

Given the array A, find and print the unique element.
"""

idea = """The trick is to use ^, the XOR operator, which works like an on/off switch. Every element of the pairs will cancel each other out."""

if __name__ == '__main__':
    n = int(input())
    bits = 0
    a = list(map(int, input().rstrip().split()))
    for i in a:
        bits ^= i
    print(bits)

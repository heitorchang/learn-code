description = """
Determine if the given number is a power of some non-negative integer.

Example

    For n = 125, the output should be
    isPower(n) = true;
    For n = 72, the output should be
    isPower(n) = false.

Input/Output

    [time limit] 4000ms (py3)

    [input] integer n

    A positive integer.

    Guaranteed constraints:
    1 ≤ n ≤ 400.

    [output] boolean

    true if n can be represented in the form ab (a to the power of b) where a and b are some non-negative integers and b ≥ 2, false otherwise.

"""

# solution by John

def isPower(n):
    for i in range(1,50):
        for j in range(2,4):
            if i**j==n:
                return True
    return False

# solution by compmonk

def isPower(n):
    for i in range(2, n):
        x = 0
        while i ** x <= n:
            x += 1
        if i ** (x - 1) == n:
            return True
    return n == 1
    
    


description = """
Find the smallest integer not less than the given limit which is divisible by all integers from the given array.

Example

For divisors = [2, 3, 4] and start = 13, the output should be
firstMultiple(divisors, start) = 24.
"""

def firstMultiple(divisors, start):
    while True:
        for d in divisors:
            if start % d != 0:
                start += 1
                break  # get out of for loop
                
        else:  # if all divisors divide evenly
            break  # get out of while loop

    return start

def test():
    testeql(firstMultiple([2, 3, 4], 13), 24)
    testeql(firstMultiple([5, 6], 62), 90)

description = """

Given integers a and b, determine whether the following pseudocode results in an infinite loop

while a is not equal to b do
  increase a by 1
  decrease b by 1

Assume that the program is executed on a virtual machine which can store arbitrary long numbers and execute forever.

Example

    For a = 2 and b = 6, the output should be
    isInfiniteProcess(a, b) = false;
    For a = 2 and b = 3, the output should be
    isInfiniteProcess(a, b) = true.

a   b  b-a
2   6  4
3   5  2
4   4  0

a   b 
2   3  1
3   2  -1
4   1

a   b
2   2  0

2   5
3   4
4   3


Input/Output

    [time limit] 4000ms (py3)

    [input] integer a

    Guaranteed constraints:
    0 ≤ a ≤ 20.

    [input] integer b

    Guaranteed constraints:
    0 ≤ b ≤ 20.

    [output] boolean

    true if the pseudocode will never stop, false otherwise.


"""

def test():
    testeql(isInfiniteProcess(2, 6), False)
    testeql(isInfiniteProcess(2, 3), True)


def isInfiniteProcess(a, b):
    if b == a:
        return False
        
    if b < a:
        return True

    if (b - a) % 2 == 1:
        return True
    return False

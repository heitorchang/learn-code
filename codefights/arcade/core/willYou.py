description = """
Once Mary heard a famous song, and a line from it stuck in her head. That line was "Will you still love me when I'm no longer young and beautiful?". Mary believes that a person is loved if and only if he/she is both young and beautiful, but this is quite a depressing thought, so she wants to put her belief to the test.

Knowing whether a person is young, beautiful and loved, find out if they contradict Mary's belief.

A person contradicts Mary's belief if one of the following statements is true:

    they are young and beautiful but not loved;
    they are loved but not young or not beautiful.

Example

    For young = true, beautiful = true and loved = true, the output should be
    willYou(young, beautiful, loved) = false.

    Young and beautiful people are loved according to Mary's belief.

    For young = true, beautiful = false and loved = true, the output should be
    willYou(young, beautiful, loved) = true.

    Mary doesn't believe that not beautiful people can be loved.

Input/Output

    [time limit] 4000ms (py3)

    [input] boolean young

    [input] boolean beautiful

    [input] boolean loved

    [output] boolean

    true if the person contradicts Mary's belief, false otherwise.
"""

def test():
    testeql(YBL(True, False, True), "101")


def YBL(y, b, l):
    return bin((y << 2) + (b << 1) + l)[2:].zfill(3)

def willYou(young, beautiful, loved):
    # brute force truth table
    bitStr = YBL(young, beautiful, loved)

    # return whether a person contradicts the belief
    if bitStr == "000":
        return False # test 3
    elif bitStr == "001":
        return True # test 4
    elif bitStr == "010":
        return False
    elif bitStr == "011":
        return True
    elif bitStr == "100":
        return False
    elif bitStr == "101":
        return True # test 2
    elif bitStr == "110":
        return True
    elif bitStr == "111":
        return False # test 1
        


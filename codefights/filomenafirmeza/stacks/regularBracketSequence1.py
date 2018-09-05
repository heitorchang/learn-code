description = """
For a string consisting of only '('s and ')'s, determine if it is a regular bracket sequence or not.

A bracket sequence is called regular if it is possible to insert some numbers and signs into the sequence in such a way that the new sequence will represent a correct arithmetic expression.

Example

For sequence = "()()", the output should be
regularBracketSequence1(sequence) = true.

We could insert (1 + 2) * (2 + 4) which is a valid arithmetic expression, so the answer is true.
"""

def regularBracketSequence1(sequence):
    stack = []
    for c in sequence:
        if c == "(":
            stack.append("(")
        elif c == ")":
            if not stack or stack.pop() != "(":
                return False
    if stack:
        return False
    return True


def test():
    testeql(regularBracketSequence1("()()"), True)
    testeql(regularBracketSequence1("((())"), False)
    testeql(regularBracketSequence1("(())()()()"), True)
    testeql(regularBracketSequence1("(()()(())((("), False)

    

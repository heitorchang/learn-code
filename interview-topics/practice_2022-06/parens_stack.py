def is_bal(s):
    """check if s has balanced parens"""
    stack = []
    for c in s:
        if c == '(':
            stack.append('(')
        elif c == ')':
            try:
                top = stack.pop()
                if top != '(':
                    return False
            except IndexError:
                return False
    return len(stack) == 0

def is_matched(expression):
    stack = []
    for c in expression:
        try:
            if c == ")":
                if stack.pop() != "(":
                    return False
            elif c == "}":
                if stack.pop() != "{":
                    return False
            elif c == "]":
                if stack.pop() != "[":
                    return False
            else:
                stack.append(c)
        except IndexError:
            return False
    if len(stack) > 0:
        return False
    return True


def test():
    testeql(is_matched("{[()]}"), True)
    testeql(is_matched("{[(])}"), False)
    testeql(is_matched("{{[[(())]]}}"), True)


def main():
    t = int(input().strip())
    for a0 in range(t):
        expression = input().strip()
        if is_matched(expression) == True:
            print("YES")
        else:
            print("NO")

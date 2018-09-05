def swapParens(s):
    s = s.replace("(", "<")
    s = s.replace(")", "(")
    s = s.replace("<", ")")
    return s

def onePass(s):
    count = 0
    start = 0
    end = 0
    for i in range(len(s)):
        if s[i] == '(':
            if count == 0:
                start = i
            count += 1
        elif s[i] == ')':
            count -= 1
            if count == 0:
                end = i
                return swapParens(s[0:start] + s[end-1:start:-1]) + s[end+1:]
        else:
            pass
    
    
def reverseParentheses(s):
    try:
        _ = s.index("(")
        return reverseParentheses(onePass(s))
    except ValueError:
        return s

def test():
    testeql(reverseParentheses("Code(Cha(lle)nge)"), "CodeegnlleahC")
    testeql(reverseParentheses("abc(cba)ab(bac)c"), "abcabcabcabc")

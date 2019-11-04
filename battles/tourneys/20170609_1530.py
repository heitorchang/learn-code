

def truncateString(s):
    if len(s) == 0:
        return ""
    left = int(s[0])
    right = int(s[-1])
    if (left+right) % 3 == 0:
        return truncateString(s[1:-1])
    elif left % 3 == 0:
        return truncateString(s[1:])
    elif right % 3 == 0:
        return truncateString(s[:-1])
    else:
        return s
        
def test():
    testeql(truncateString("312248"), "2")

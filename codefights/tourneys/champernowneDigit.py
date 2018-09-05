def champernowneDigit(n):
    def c(n):
        result = ""
        for i in range(1, n+1):
            result += str(i)
        return result

    s = c(n)
    return int(s[n-1])

def test():
    testeql(champernowneDigit(11), 0)
    testeql(champernowneDigit(16), 1)

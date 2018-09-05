def checkio(str_number, radix):
    # easy solution: try int(str_number, radix), except: return -1
    digits = reversed(str_number)
    total = 0
    for i, digit in enumerate(digits):
        if digit.isdigit():
            digitValue = int(digit)
        else:
            digitValue = 10 + ord(digit) - ord('A')
        if digitValue >= radix:
            return -1
        total += radix ** i * digitValue
    return total

#These "asserts" using only for self-checking and not necessary for auto-testing
def main():    
    assert checkio("AF", 16) == 175, "Hex"
    assert checkio("101", 2) == 5, "Bin"
    assert checkio("101", 5) == 26, "5 base"
    assert checkio("Z", 36) == 35, "Z base"
    assert checkio("AB", 10) == -1, "B > A > 10"

def test():
    testeql(checkio("AF", 16), 175)
    testeql(checkio("AB", 10), -1)
    testeql(checkio("909", 9), -1)

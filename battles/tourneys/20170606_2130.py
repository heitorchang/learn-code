def buildPalindromePhail(st):
    i = len(st)
    while True:
        canConvert = True
        j = 0
        while j < i - j - 1:
            if i - j - 1 < len(st) and st[j] != st[i - j - 1]:
                pr('i j st[i-j-1]')
                st += st[i-j-1]
            j += 1
        if canConvert:
            for j in range(len(st), i):
                st += st[i - j - 1]
            return st
        i += 1
    # does not pass

# auxiliary functions for buildPalindrome
def isPalindrome(st):
    return st == st[::-1]

def reverse(st):
    return st[::-1]
    
def buildPalindrome(st):
    # aliciasavelly translated from JS
    if isPalindrome(st):
        return st
    for i in range(len(st)):
        # pr('st[i:]')
        if isPalindrome(st[i:]):
            # return st + st[i-1::-1]
            return st + reverse(st[:i])
        

def convertCell(rep):
    col = rep[0]
    row = rep[1]
    c = ord(col) - 64
    return [int(c), int(row)]

def chessBoardCellColor(cell1, cell2):
    a = convertCell(cell1)
    b = convertCell(cell2)
    return a[0] % 2 == a[1] % 2 and b[0] % 2 == b[1] % 2
    # partially correct
        
def test():
    testeql(buildPalindrome("abcdc"), "abcdcba")

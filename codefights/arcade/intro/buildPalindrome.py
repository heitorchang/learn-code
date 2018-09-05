def test():
    testeql(buildPalindrome("ababab"), "abababa")
    testeql(buildPalindrome("abcdc"), "abcdcba")
    testeql(buildPalindrome("abcde"), "abcdedcba")


def isPalindrome(s):
    return s == s[::-1]
    
def buildPalindrome(st):
    if isPalindrome(st):
        return st
    # figure out if end is already a palindrome
    center = 0
    for i in range(len(st)):
        if isPalindrome(st[i:]):
            center = i
            break
    return st + st[center-1::-1]

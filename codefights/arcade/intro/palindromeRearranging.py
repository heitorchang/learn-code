from collections import defaultdict

def palindromeRearranging(inputString):
    lst = list(inputString)
    letters = set(inputString)
    count = defaultdict(int)
    for letter in letters:
        count[letter] = lst.count(letter)
    print(count)
    foundOdd = False
    for letter in letters:
        if count[letter] % 2 == 1:
            if foundOdd:
                # found more than one odd, must not be a palindrome
                return False
            foundOdd = True
    return True

def palindromeRearrangingConsume(inputString):
    # does not work if it runs into lone character before string
    # is consumed
    print('inp ', inputString)
    if len(inputString) < 2:
        return True
    head = inputString[0]
    
    inputString = inputString[1:]  # remove head
    match = inputString.find(head)

    if match == -1:
        return False
    match += 1  # account for head that was skipped

    # re-run, excluding first char and matching char
    return palindromeRearranging(inputString[:match] + inputString[match+1:])

def test():
    testeql(palindromeRearranging("aabb"), True)
    testeql(palindromeRearranging("abbcabb"), True)
    

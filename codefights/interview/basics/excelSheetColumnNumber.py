description = """
Given a column title as it would appear in an Excel spreadsheet, return its corresponding column number. Column names and numbers follow a consistent pattern:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

Example

For s = "AB", the output should be
excelSheetColumnNumber(s) = 28.

Input/Output

    [time limit] 4000ms (py3)

    [input] string s

    A string of uppercase English letters.

    Guaranteed constraints:
    1 ≤ s.length ≤ 6.

    [output] integer

"""

def test():
    testeql(excelSheetColumnNumber("A"), 1)
    testeql(excelSheetColumnNumber("AB"), 28)









    

def letterToNumber(letter):
    return ord(letter) - 64

def excelSheetColumnNumber(s):
    rev = list(map(letterToNumber, s))[::-1]
    num = 0
    for i in range(len(rev)):
        num += rev[i] * 26 ** i
    return num


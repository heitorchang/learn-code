description = """
Spreadsheet software uses a consistent naming pattern for columns, in which the first column is named A, the second column is named B, the 27th column is named AA, the 28th is named AB, and so on.
Given a positive integer number, return the corresponding column title as it would appear in a spreadsheet.

Example

    For number = 27, the output should be
    columnTitle(number) = "AA";
    For number = 2, the output should be
    columnTitle(number) = "B".

Input/Output

    [time limit] 4000ms (py3)

    [input] integer number

    A positive integer.

    Guaranteed constraints:
    1 ≤ number ≤ 2147483647.

    [output] string

    The column title that corresponds to number.

"""

def test():
    testeql(columnTitle(16808), "XVL")
    testeql(columnTitle(2), "B")
    testeql(columnTitle(26), "Z")
    testeql(columnTitle(27), "AA")
    testeql(columnTitle(52), "AZ")
    testeql(columnTitle(53), "BA")









def numberToLetter(n):
    if n == 0:
        return 'Z'
    else:
        return chr(64 + n)
    
def columnTitle(number):
    # A = 1   / 0
    # Z = 26  / 26
    # AA = 27 / 26 + 1
    # AB = 28 / 26 + 2
    # AZ = 52 / 26 + 26
    # BA = 53 / 2*26 + 1
    # YZ = 676 / 25*26 + 26
    # ZZ = 702 / 26*26 + 26
    # AAA = 703 / 1*(26^2) + 1*(26) + 1

    # Rosen, p. 249 Construction base b expansions
    # Does not work because there is no 'Zero'
    # k = 0
    # b = 26
    # expansion = []
    # while number != 0:
    #     expansion.append(number % b)
    #     number //= b
    # expansion.reverse()
    
    letters = 0
    p = 0
    while 26 ** p < number:
        p += 1

    ords = []
    for i in range(p):
        r = number % 26
        if r == 0:
            r = 26
            number -= 26
        ords.append(r)
        number //= 26
    return ''.join(map(numberToLetter, ords[::-1]))

description = """
For code = "010010000110010101101100011011000110111100100001", the output should be
messageFromBinaryCode(code) = "Hello!".

The first 8 characters of the code are 01001000, which is 72 in the binary numeral system. 72 stands for H in the ASCII-table, so the first letter is H.
Other letters can be obtained in the same manner.

Input/Output

    [time limit] 4000ms (py3)

    [input] string code

    A string, the encrypted message consisting of characters '0' and '1'.

    Guaranteed constraints:
    0 < code.length < 800.

    [output] string

    The decrypted message.
"""

def messageFromBinaryCode(code):
    chunks = [code[start:start+8] for start in range(0,len(code),8)]
    out = ""
    for c in chunks:
        out += chr(int(c, 2))
    return out

def test():
    testeql(messageFromBinaryCode("010010000110010101101100011011000110111100100001"), "Hello!")

description = """
A character in UTF-8 can be anywhere from 1 to 4 bytes long. The bytes are 8 bits long and are subject to the following rules:

    For a 1-byte character, the first bit is a 0, followed by its unicode code.
    For an n-byte character, the first n bits are all 1s and the n + 1 bit is 0. This is followed by n - 1 bytes in which the 2 most significant bits (that is, the leftmost 2) are 10.

This is how the UTF-8 encoding would work:

   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Given an array of integers representing the data, return true if it can be converted to a valid UTF-8 encoding, otherwise return false.

Example

    For stream = [197, 130, 1], the output should be
    streamValidation(stream) = true.

    The input stream, when converted from decimal to binary numbers, represents the following octet sequence: 11000101 10000010 00000001. The first 2 bits are 1s and the 3rd bit is 0, meaning that this sequence is a valid UTF-8 encoding of a 2-byte character followed by a 1-byte character, making the answer true.

    For stream = [235, 140, 4], the output should be
    streamValidation(stream) = false.

    The input stream, when converted from decimal to binary numbers, represents the following octet sequence: 11101011 10001100 00000100. The first 3 bits are all 1s and the 4th bit is 0, meaning that this is a 3-byte character. The next byte is a correct continuation byte since it starts with 10. However, the second continuation byte is invalid because it does not start with 10, making the answer false.

Input/Output

    [time limit] 4000ms (py3)

    [input] array.integer stream

    An array of integers.

    Guaranteed constraints:
    1 ≤ stream.length ≤ 1100,
    0 ≤ stream[i] ≤ 255.

    [output] boolean

    Return true if the input array represents a valid UTF-8 encoding, otherwise return false.

"""

def firstBitsMatch(n, mask, length):
    check = n ^ mask
    threshold = (1 << (8 - length)) - 1
    # the idea is to ensure the most significant bits (leftmost) all
    # match. In case they don't, XOR will result in a '1' at the
    # non-matching position. So we check that the result is no
    # greater than the number of "wild" bits to the right
    
    # pr('bin(check)')
    # pr('bin(threshold)')
    if check > threshold:
        return False
    return True
    
def streamValidation(stream):
    index = 0
    while index < len(stream):
        n = stream[index]
        if firstBitsMatch(n, 0b11111000, 5):
            # five 1s in a row is not valid
            return False
        elif firstBitsMatch(n, 0b11110000, 5):
            # four 1s in a row, expecting three 10xxxxxx
            try:
                n1 = stream[index+1]
                n2 = stream[index+2]
                n3 = stream[index+3]
                if not firstBitsMatch(n1, 0b10000000, 2):
                    return False
                if not firstBitsMatch(n2, 0b10000000, 2):
                    return False
                if not firstBitsMatch(n3, 0b10000000, 2):
                    return False
                index += 4
            except IndexError:
                return False
        elif firstBitsMatch(n, 0b11100000, 4):
            # three 1s in a row, expecting two 10xxxxxx
            try:
                n1 = stream[index+1]
                n2 = stream[index+2]
                if not firstBitsMatch(n1, 0b10000000, 2):
                    return False
                if not firstBitsMatch(n2, 0b10000000, 2):
                    return False
                index += 3
            except IndexError:
                return False
        elif firstBitsMatch(n, 0b11000000, 3):
            # two 1s in a row, expecting one 10xxxxxx
            try:
                n1 = stream[index+1]
                if not firstBitsMatch(n1, 0b10000000, 2):
                    return False
                index += 2
            except IndexError:
                return False
        elif n > 0x7f:
            return False
        else:
            index += 1
    return True

def streamValidationAndMask(stream):
    i = 0
    while i < len(stream):
        if stream[i] & 0b10000000 == 0:
            i+=1
        else:
            if stream[i] & 0b11100000 == 0b11000000:
                cont = 1
            elif stream[i] & 0b11110000 == 0b11100000:
                cont = 2
            elif stream[i] & 0b11111000 == 0b11110000:
                cont = 3
            else:
                return False
            
            if i + cont >= len(stream):
                return False

            i += 1

            for _ in range(cont):
                if stream[i] & 0b11000000 != 0b10000000:
                    return False
                i += 1
            
    return True


    
def test():
    testeql(streamValidation([197, 130, 1]), True)
    testeql(streamValidation([235, 140, 4]), False)
    testeql(streamValidationAndMask([197, 130, 1]), True)
    testeql(streamValidationAndMask([235, 140, 4]), False)
    # testeql(firstBitsMatch(0b10110011, 0b10000000, 2), True)
    # testeql(firstBitsMatch(0b11001100, 0b10000000, 2), False)
    # testeql(firstBitsMatch(0b11000000, 0b10000000, 2), False)
    # testeql(firstBitsMatch(0b11000000, 0b11000000, 3), True)
    # testeql(firstBitsMatch(0b11100000, 0b10000000, 2), False)
    # testeql(firstBitsMatch(0b11001100, 0b10000000, 2), False)
    # testeql(firstBitsMatch(0b11001100, 0b10000000, 2), False)
    # testeql(firstBitsMatch(0b10110000, 0b11110000, 5), False)

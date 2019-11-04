description = """
A media access control address (MAC address) is a unique identifier assigned to network interfaces for communications on the physical network segment.

The standard (IEEE 802) format for printing MAC-48 addresses in human-friendly form is six groups of two hexadecimal digits (0 to 9 or A to F), separated by hyphens (e.g. 01-23-45-67-89-AB).

Your task is to check by given string inputString whether it corresponds to MAC-48 address or not.

Example

    For inputString = "00-1B-63-84-45-E6", the output should be
    isMAC48Address(inputString) = true;
    For inputString = "Z1-1B-63-84-45-E6", the output should be
    isMAC48Address(inputString) = false;
    For inputString = "not a MAC-48 address", the output should be
    isMAC48Address(inputString) = false.

Input/Output

    [time limit] 4000ms (py3)

    [input] string inputString

    Guaranteed constraints:
    15 ≤ inputString.length ≤ 20.

    [output] boolean

    true if inputString corresponds to MAC-48 address naming rules, false otherwise.

"""

def test():
    testeql(isMAC48Address("00-1B-63-84-45-E6"), True)
    testeql(isMAC48Address("Z1-1B-63-84-45-E6"), False)


def isMAC48Address(s):
    if len(s) != 17:
        return False

    parts = s.split("-")
    if len(parts) != 6:
        return False

    for p in parts:
        try:
            n = int(p, 16)
            if not (0 <= n <= 255):
                return False
        except ValueError:
            return False
    return True
            

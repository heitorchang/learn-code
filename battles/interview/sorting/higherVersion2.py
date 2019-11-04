description = """
You have two version strings composed of several non-negative decimal fields that are separated by periods ("."). Both strings contain an equal number of numeric fields. Return 1 if the first version is higher than the second version, -1 if it is smaller, and 0 if the two versions are the same.

The syntax follows the regular semver (semantic versioning) ordering rules:

1.0.5 < 1.1.0 < 1.1.5 < 1.1.10 < 1.2.0 < 1.2.2
< 1.2.10 < 1.10.2 < 2.0.0 < 10.0.0

Example

    For ver1 = "1.2.2" and ver2 = "1.2.0", the output should be
    higherVersion2(ver1, ver2) = 1;
    For ver1 = "1.0.5" and ver2 = "1.1.0", the output should be
    higherVersion2(ver1, ver2) = -1;
    For ver1 = "1.0.5" and ver2 = "1.00.05", the output should be
    higherVersion2(ver1, ver2) = 0.

Input/Output

    [time limit] 4000ms (py3)

    [input] string ver1

    Correct version as a string.

    Guaranteed constraints:

    1 ≤ ver1.length ≤ 350.

    [input] string ver2

    Correct version as a string.

    Guaranteed constraints:

    1 ≤ ver2.length ≤ 350.

    [output] integer

    Return 1 if ver1 is higher than ver2, -1 if it's smaller, and 0 if the two versions are the same.

"""

def test():
    testeql(higherVersion2("1.1", "1.01"), 0)
    testeql(higherVersion2("1.0.5", "1.1.0"), -1)
    testeql(higherVersion2("1.00001", "1.10"), -1)

def compareArrays(a, b):
    if len(a) == 0:
        return 0
    if a[0] == b[0]:
        return compareArrays(a[1:], b[1:])
    elif a[0] > b[0]:
        return 1
    return -1
    
def parseVersionString(s):
    parts = s.split(".")
    return list(map(int, parts))
    
def higherVersion2(ver1, ver2):
    return compareArrays(parseVersionString(ver1), parseVersionString(ver2))

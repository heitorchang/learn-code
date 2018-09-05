description = """
You have an array of non-negative integers numbers, each less than 10numbers.length. Add leading zeros if necessary so that for each i, numbers[i] has exactly numbers.length digits. Now, write these integers under each other in the same order that they appear in the input array.

From this process, you obtain a square that consists of digits. If you read them from left to right, starting from the topmost row, and drop the leading zeros, you get the initial array. What array will you get if you read the digits from the top down, starting from the leftmost column, and ignoring leading zeros?

Example

For numbers = [12, 345, 67, 5], the output should be
directionOfReading(numbers) = [0, 300, 1460, 2575].

The square obtained in the intermediate step looks like this:

0012
0345
0067
0005
"""

def directionOfReading(numbers):
    strs = [str(n) for n in numbers]
    # maxlen = max(strs, key=len)
    maxlen = len(numbers)
    
    strspad = [s.zfill(maxlen) for s in strs]
    anss = [""] * maxlen
    rows = len(strspad)
    cols = maxlen
    print(strspad)
    for c in range(cols):
        for r in range(rows):
            anss[c] += strspad[r][c]
            
    return [int(s) for s in anss]


def test():
    testeql(directionOfReading([12,345,67,5]), [0,300,1460,2575])
    testeql(directionOfReading([9]), [9])
    testeql(directionOfReading([1, 2, 3, 4, 5, 6, 7, 8, 9]), [0, 0, 0, 0, 0, 0, 0, 0, 123456789])
    testeql(directionOfReading([23,345,28]), [30,242,358])

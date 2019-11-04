description = """
You are given an n x n 2D matrix that represents an image. Rotate the image by 90 degrees (clockwise).

Try to solve this in-place - in a real interview, you will only be allowed to use O(1) additional memory.

Example

For

a = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

the output should be

rotateImage(a) =
    [[7, 4, 1],
     [8, 5, 2],
     [9, 6, 3]]

Input/Output

    [time limit] 4000ms (py3)

    [input] array.array.integer a

    Guaranteed constraints:
    1 ≤ a.length ≤ 100,
    a[i].length = a.length,
    1 ≤ a[i][j] ≤ 104.

    [output] array.array.integer

"""

def test():
    testeql(rotateImage([[1,2,3], 
                         [4,5,6], 
                         [7,8,9]]),
            [[7,4,1], 
             [8,5,2], 
             [9,6,3]])






















# 250 xp, 1000 coins

def rotateImageMySolution(a):
    # uses O(n) memory, not ideal
    n = len(a)
    target = [[0 for _ in range(n)] for _ in range(n)]

    for r in range(n):
        for c in range(n):
            target[c][n-r-1] = a[r][c]
    return target

def rotateImage(a):
    # solution by darth_tytus
    return [[row[i] for row in a][::-1]
            for i in range(len(a))]
    

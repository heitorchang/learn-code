"""
Let's learn about list comprehensions! You are given three integers X, Y, and Z and representing the dimensions of a cuboid along with an integer N . You have to print a list of all possible coordinates given by (i,j,k) on a 3D grid where the sum of i+j+k is not equal to N. Here,
0 <= i < X,
0 <= j < Y,
0 <= k < Z,

Input Format

Four integers X, Y, Z, N each on four separate lines, respectively.

Constraints

Print the list in lexicographic increasing order.

Sample Input
"""

def solution(x, y, z, n):
    print([[i, j, k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i + j + k != n])

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    solution(x, y, z, n)

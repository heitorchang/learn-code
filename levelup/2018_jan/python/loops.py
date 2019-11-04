"""
Task 
Read an integer N. For all non-negative integers i < N, print i^2. See the sample for details.

Input Format

The first and only line contains the integer, N

Output Format

Print N lines, one corresponding to each i.
"""

def main(N):
    for i in range(N):
        print(i ** 2)

if __name__ == "__main__":
    N = int(input())
    main(N)

def test():
    testeql(main(4), None)

description = """
The school term starts soon, and the students need to be sorted into their respective sections. There are n students numbered 1 to n, and  sections numbered 1 to m .

Section i needs to have exactly a_i students. To simplify the process, the school has decided to assign students to sections in increasing student number, which means the first a_1 students will be assigned section 1, the next a_2 students will be assigned section 2, and so on.

Your student number is k. Which section will you be assigned to?

Complete the function whichSection which takes in two integers n and k and an integer array a and returns the section number you will be assigned to, assuming you are student number k.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whichSection function below.
def whichSection(n, k, a):
    # Return the section number you will be assigned to assuming you are student number k.
    for i, section in enumerate(a, 1):
        k -= section
        if k <= 0:
            return i

boilerplate = """
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        nkm = input().split()

        n = int(nkm[0])
        k = int(nkm[1])
        m = int(nkm[2])
        a = list(map(int, input().rstrip().split()))

        result = whichSection(n, k, a)

        fptr.write(str(result) + '\n')

    fptr.close()
"""

test(whichSection(470, 143, [11, 24, 420, 6, 9]), 3)

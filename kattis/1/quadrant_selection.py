# difficulty 1.2

import sys

# input
inp = sys.stdin.readlines()

x = int(inp[0])
y = int(inp[1])

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)

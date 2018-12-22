"""

import sys

# input
inp = sys.stdin.readlines()

x = int(inp[0])
n = int(inp[1])

months = map(int, inp[2:])

"""

def tarifa(x, n, *months):
    ans = (n + 1) * x
    print(ans - sum(months))
    return ans - sum(months)


test(tarifa(10, 3, 4, 6, 2), 28)

import sys

inp = sys.stdin.readlines()

x = int(inp[0])
n = int(inp[1])

months = map(int, inp[2:])

def tarifa(x, n, *months):
    ans = (n + 1) * x
    print(ans - sum(months))

tarifa(x, n, *months)

https://open.kattis.com/

# Python 3 

Do not 'return' anything, but 'print' expected output

# multiple lines input

import sys

# input
inp = sys.stdin.readlines()

x = int(inp[0])
y = int(inp[1])



# single line input

import sys
line = sys.stdin.readline()

# x = number of articles to publish
# y = impact factor required

# impact = number of citations / number of articles
# find minimal number of citations required, if impact is rounded up

x, y = map(int, line.split())

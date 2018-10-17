import sys
line = sys.stdin.readline()

# x = number of articles to publish
# y = impact factor required

# impact = number of citations / number of articles
# find minimal number of citations required, if impact is rounded up

x, y = map(int, line.split())

print(x * (y - 1) + 1)

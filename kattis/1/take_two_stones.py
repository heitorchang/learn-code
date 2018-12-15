# seems like you just need to find remainder

import sys
line = sys.stdin.readline()

winner = "Alice" if int(line) % 2 == 1 else "Bob"
print(winner)

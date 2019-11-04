# You would like to write a function that takes x, y, L and R and returns True if x ** y lies in the interval (L, R] and False otherwise.

# Which of these is most efficient?

# 1. if L < x ** y <= R:
# 2. if x ** y > L and x ** y <= R:
# 3. if x ** y in range(L+1, R+1):

# My initial answer: 1 and 2 (incorrect)
# Correct answer: 1 is best

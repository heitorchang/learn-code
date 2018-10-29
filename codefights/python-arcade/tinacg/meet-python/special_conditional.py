# One of these doesn't work the same way as others. Which one?
# a and b are booleans

not (a == b)  # initial answer, incorrect

not a == b

a == not b  # correct answer (it's a syntax error)

a == (not b)

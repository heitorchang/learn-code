from pairtest import pairtest

# Define the challenge function as f()

def f(a, b):
    return a + b

pairtest(
    f(1, 2), 3,
    f(9, 9), 18,
    f(10, 5), 15,
    f(9, 3), 12,
)

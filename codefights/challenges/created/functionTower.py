description = """
You are given a **Function Tower** that is made of **Function Bricks** as an array of strings. Each string is a level in the tower. Values flow downward starting from the first string, the topmost level.

A brick is the substring `[ f ]` (including its endpoint brackets, `[ ]`), where `f` is either a constant (a positive integer) or a function of one parameter (`x`). 

Functions are labeled as `x + n` or `x * n`, where `n` is a positive integer.

The output of a brick flows to all bricks directly below it. A constant brick ignores input, and always outputs the number it holds. 

The value of `x` fed to a function brick is the **sum of the outputs of all bricks directly above it**. A function brick will output the result of the arithmetic function called with this value of `x`.

Your task is to return the sum of all outputs of the bottommost level.

It is guaranteed that a function brick has at least one brick above it to serve as input. You do not need to check for errors.

__Example__


"""

class Tower:
    pass


class Brick:
    pass
    

def functionBars(bars):
    pass

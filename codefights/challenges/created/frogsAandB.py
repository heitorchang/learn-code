desc = """
Frogs A and B are playful frogs who live on the number line. Their favorite game is *Ribbit-Bump*.

The rules for *Ribbit-Bump* are:

* Frog A starts at `0` (zero), and jumps `x` units to the right every second.
* Frog B starts on any positive integer `b`, and jumps `y` units to the left every second.
* If the frogs bump into each other on the ground at some point, return that point.
* If the frogs do not bump into each other, return `-1`.

All values are integers.

__Examples__

Suppose Frog B starts at `8` and both frogs jump `2` units.

After 1 second, A will be at `2` and B will be at `6`. The next second, they will both bump each other at `4`. So we return `4`.

Suppose Frog B starts at `9` and both frogs jump `3` units.

Now, at `t = 1`, we have `a = 3, b = 6`.

At `t = 2`, we have `a = 6, b = 3`. A and B have passed each other and will not bump into each other so the game is over. Return `-1`.
"""

def frogsAandB(b, x, y):
    a = 0

    assert x <= b
    assert y <= b
    
    while b > a:
        a += x
        b -= y

        print(a, b)

        if a == b:
            return a
    return -1


def gcd(a,b):
    """Compute the greatest common divisor of a and b"""
    while b > 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    """Compute the lowest common multiple of a and b"""
    return a * b / gcd(a, b)

    
pairtest(frogsAandB(8, 2, 2), 4,
         frogsAandB(9, 3, 3), -1,
         frogsAandB(30, 5, 10), 10,
         frogsAandB(7, 5, 6), -1,
         frogsAandB(10, 1, 10), -1,
         frogsAandB(120, 8, 12), 48,
         frogsAandB(240, 2, 8), 48,
         frogsAandB(210, 7, 3), 147,
         frogsAandB(2381, 992, 130), -1
         )

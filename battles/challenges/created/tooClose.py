desc = """
You are given a list of up to `8` positive integers. Two integers are **too close for comfort** if they are adjacent and the absolute value of the difference between them is **less than `10`**.

There are no duplicate values.

Return the total number of *permutations* of the list where no integers are **too close for comfort**.

__Example__

For:

```
values = [1, 21, 11, 5]
```

The only comfortable permutations are:

```
[1, 11, 21, 5]
[11, 1, 21, 5]
[5, 21, 1, 11]
[5, 21, 11, 1]
```

The expected output is `4`.

"""

import numpy as np
from itertools import permutations

def isOK(lst):
    a = np.array(lst)
    d = abs(np.ediff1d(lst))
    return np.all(d >= 10)


def tooCloseForComfort(values):
    if len(values) > 8:
        raise ValueError("Too many values, max is 8")
    if len(set(values)) != len(values):
        raise ValueError("Cannot have duplicate entries")
    
    tot = 0
    for p in permutations(values):
        ok = isOK(p)
        if ok:
            tot += 1
    return tot

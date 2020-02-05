debug = True

import matplotlib.pyplot as plt
import numpy as np

if not debug:
    import pandas as pd
    from sklearn.discriminant_analysis import LinearDiscriminantAnalysis


def classification(A, B, unknown, m=None, b1=None, b2=None):
    if debug:
        if m and b1 and b2:
            yint1 = [0, b1]
            xint1 = [-b1/m, 0]
            yint2 = [0, b2]
            xint2 = [-b2/m, 0]
            plt.plot(xint1, yint1)
            plt.plot(xint2, yint2)
        plt.plot([p[0] for p in A], [p[1] for p in A], 'go')
        plt.plot([p[0] for p in B], [p[1] for p in B], 'bo')
        plt.plot([p[0] for p in unknown], [p[1] for p in unknown], 'rx')
        plt.axis('equal')
        plt.xlim(0, 5)
        plt.ylim(0, 5)
        plt.show()

    if not debug:
        dataarr = [a + ['A'] for a in A] + [b + ['B'] for b in B]
        df = pd.DataFrame(dataarr, columns=['x', 'y', 'type'])
    
        array = df.values
        clf = LinearDiscriminantAnalysis()
        clf.fit(array[:,0:2], array[:,2])
        pred = clf.predict(unknown)
        print(np.count_nonzero(pred == 'B'))

        
import numpy as np
import pandas as pd
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

def taleOfTwoCities(a, b, unknown):
    dataarr = [m + ['A'] for m in a] + [n + ['B'] for n in b]
    df = pd.DataFrame(dataarr, columns=['x', 'y', 'type'])

    array = df.values
    clf = LinearDiscriminantAnalysis()
    clf.fit(array[:,0:2], array[:,2])
    pred = clf.predict(unknown)
    return np.count_nonzero(pred == 'B')


print()
"""
ans = taleOfTwoCities([[1,1],[1,2],[2,1]],
                      [[1,4],[2,3],[2,4],[3,2],[3,3],[3,4]],
                      [[2.3,3.5],[4.2,3.4],[1.2,1.6],[2.7,2.9],[1.5, 0.8]])
print(ans)
"""

desc = """
The head of Signalia County's taxation service urgently needs your help with assigning the correct tax brackets for this year's brand new properties.

All new properties fall in a fairly limited area that lies at the border of Ananasville and Bananaville. This border between the two cities is a road that runs in a straight line (in the area being considered).

Ananasville is to the south of the road, and Bananaville is to the north (North points up in the diagram)

You will be given three lists of `(x, y)` float coordinates, `A, B, unknown` representing:

```
A: old properties in Ananasville (shown in green in the diagram)
B: old properties in Bananaville (shown in blue)
unknown: the new properties that need to be assigned (shown as red Xs)
```

Your task is to return the total number of `unknown` properties that belong in Bananaville (to the north of the road).

__Constraints__

* All three lists contain more than one point.
* Due to recent zoning restrictions, unknown properties will not be found close to the road.
* All values are positive.

__Example__

For

```
A: [[1,1],[1,2],[2,1]]
B: [[1,4],[2,3],[2,4],[3,2],[3,3],[3,4]]
unknown: [[2.3,3.5],[4.2,3.4],[1.2,1.6],[2.7,2.9],[1.5, 0.8]]
```

As shown in the diagram, there are three X (unknowns) above the road. You should return 3.
"""

from random import random

def tTop(m, b, size, n):
    s = []
    tot = 0
    while tot < n:
        trialx = round(random() * size, 2)
        trialy = round(random() * size, 2)
        if trialy > m * trialx + b:
            s.append([trialx, trialy])
            tot += 1

    yint1 = [0, b]
    xint1 = [-b/m, 0]
    print(s)
    plt.plot(xint1, yint1)
    plt.plot([p[0] for p in s], [p[1] for p in s], 'go')

def tBot(m, b, size, n):
    s = []
    tot = 0
    while tot < n:
        trialx = round(random() * size, 2)
        trialy = round(random() * size, 2)
        if trialy < m * trialx + b:
            s.append([trialx, trialy])
            tot += 1

    yint1 = [0, b]
    xint1 = [-b/m, 0]
    print(s)
    plt.plot(xint1, yint1)
    plt.plot([p[0] for p in s], [p[1] for p in s], 'go')

def tAll(m, b, roadSize, size, n):
    tBot(m, b-roadSize, size, n)	
    tTop(m, b+roadSize, size, n)
    plt.show(block=False)

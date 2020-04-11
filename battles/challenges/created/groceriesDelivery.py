story = """
With her college classes cancelled due to the citywide quarantine, Tina has a lot of free time in her hands and volunteered to help her elderly neighbors get their groceries without having to leave their homes.

Tina's neighborhood in Narsheville has streets laid out in a square grid (shown in ASCII Art in the example section below), with North-to-South streets named `A Street` to `I Street`, and East-to-West streets numbered `1st Street` to `9th Street`. All streets are one-way, and while riding her scooter, Tina has to obey the street's direction.

As indicated by the arrows, Streets A, C, E, G and I go North, B, D, F and H go South, 1, 3, 5, 7 and 9 go East, and 2, 4, 6 and 8 go West.

Although nobody's in a rush and the blocks are only 100 meters long, Tina doesn't want to waste gas. Help her calculate the shortest route she can take:

* Starting at `home`
* then going to the `store`
* then delivering the groceries to each house coordinate in `deliveries`. The order given here is arbitrary--you should find the optimal path that covers all houses.
* finally, returning `home`.

For convenience, we are defining each of these point coordinates as street intersections. They consist of a capital letter and a number, such as `"E3"`, meaning the intersection of E Street and 3rd Street. 

Return the minimum number of blocks Tina must travel with her scooter to complete her delivery help.

*Note*: The author solution involves a bit of brute force, so the more adventurous Coders may try adding more destinations to their solutions and see how they run. I want to ensure my solution works for at most **5 elderlies' houses**


__Example__


For ```
home: "B3"
store: "F4"
deliveries: ["E5", "A2", "C1"]

Tina lives at the intersection B3 (Home)
The store is at F4
Xavier lives at E5
Yvonne lives at A2
Zora lives at C1.

   |   |   |   |   |   |   |   |   | 
9 -+->-+->-+->-+->-+->-+->-+->-+->-+-
   |   |   |   |   |   |   |   |   | 
   ^   v   ^   v   ^   v   ^   v   ^ 
   |   |   |   |   |   |   |   |   | 
8 -+-<-+-<-+-<-+-<-+-<-+-<-+-<-+-<-+-
   |   |   |   |   |   |   |   |   | 
   ^   v   ^   v   ^   v   ^   v   ^ 
   |   |   |   |   |   |   |   |   | 
7 -+->-+->-+->-+->-+->-+->-+->-+->-+-
   |   |   |   |   |   |   |   |   | 
   ^   v   ^   v   ^   v   ^   v   ^ 
   |   |   |   |   |   |   |   |   | 
6 -+-<-+-<-+-<-+-<-+-<-+-<-+-<-+-<-+-
   |   |   |   |   |   |   |   |   | 
   ^   v   ^   v   ^   v   ^   v   ^ 
   |   |   |   |   |   |   |   |   | 
5 -+->-+->-+->-+->-X->-+->-+->-+->-+-
   |   |   |   |   |   |   |   |   |   
   ^   v   ^   v   ^   v   ^   v   ^ 
   |   |   |   |   |   |   |   |   | 
4 -+-<-+-<-+-<-+-<-+-<-S-<-+-<-+-<-+-
   |   |   |   |   |   |   |   |   |  
   ^   v   ^   v   ^   v   ^   v   ^  
   |   |   |   |   |   |   |   |   | 
3 -+->-H->-+->-+->-+->-+->-+->-+->-+-
   |   |   |   |   |   |   |   |   |  
   ^   v   ^   v   ^   v   ^   v   ^  
   |   |   |   |   |   |   |   |   | 
2 -Y-<-+-<-+-<-+-<-+-<-+-<-+-<-+-<-+-
   |   |   |   |   |   |   |   |   |  
   ^   v   ^   v   ^   v   ^   v   ^  
   |   |   |   |   |   |   |   |   | 
1 -+->-+->-Z->-+->-+->-+->-+->-+->-+-
   |   |   |   |   |   |   |   |   | 
   A   B   C   D   E   F   G   H   I

One possible optimal route is:

Home to Store: 7 blocks
Store to Xavier: 2 blocks
Xavier to Zora: 10 blocks
Zora to Yvonne: 3 blocks
Yvonne to Home: 2 blocks

Total number of blocks: 24
"""


from itertools import product, permutations
from collections import deque, OrderedDict
from scipy.sparse.csgraph import dijkstra
from scipy import sparse
import numpy as np
import unittest

ELIM = "I"
NLIM = "9"

def pairtest(*pair_args):
    tc = unittest.TestCase('__init__')

    trial = pair_args[::2]
    expected = pair_args[1::2]

    for t, e in zip(trial, expected):
        if isinstance(t, float):
            tc.assertAlmostEqual(t, e)
        else:
            tc.assertEqual(t, e)
            
    print("\n\n* All tests passed \\(^o^)/ \n")


def leftint(pt):
    ns, we = pt
    if ns == 'A':
        raise ValueError("already at west end")
    return chr(ord(ns) - 1) + we


def rightint(pt):
    ns, we = pt
    if ns == ELIM:
        raise ValueError("already at east end")
    return chr(ord(ns) + 1) + we


def upint(pt):
    ns, we = pt
    if we == NLIM:
        raise ValueError("already at north end")
    return ns + chr(ord(we) + 1)


def downint(pt):
    ns, we = pt
    if we == '1':
        raise ValueError("already at south end")
    return ns + chr(ord(we) - 1)

def isns(pt):
    ns = pt[0]
    if ns in "ACEGI":
        return True
    return False


def iswe(pt):
    we = pt[1]
    if we in "13579":
        return True
    return False

def shortestDists():
    # build adjacency list
    adj = OrderedDict()
    ns = "ABCDEFGHI"
    we = "123456789"
    
    for inters in product(ns, we):
        inters = ''.join(inters)
        adj[inters] = []
        if isns(inters):
            try:
                adj[inters].append(upint(inters))
            except ValueError:
                pass
        else:
            try:
                adj[inters].append(downint(inters))
            except ValueError:
                pass

        if iswe(inters):
            try:
                adj[inters].append(rightint(inters))
            except ValueError:
                pass

        else:
            try:
                adj[inters].append(leftint(inters))
            except ValueError:
                pass

    # Convert adjacency list to adj matrix
    ks = list(adj.keys())
    
    matrix = [[0 for _ in range(len(adj))] for _ in range(len(adj))]

    for k in ks:
        for dest in adj[k]:
            matrix[ks.index(k)][ks.index(dest)] = 1

    row_ind = []
    col_ind = []
    data = []
    
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 1:
                row_ind.append(row)
                col_ind.append(col)
                data.append(1)

    # add endpoints to create NxN matrix
    row_ind.append(0)
    col_ind.append(len(ks))
    data.append(1e7)

    row_ind.append(len(ks))
    col_ind.append(0)
    data.append(1e7)
    
    mat_coo = sparse.coo_matrix((data, (row_ind, col_ind)))
    d = dijkstra(mat_coo)

    # start = ks.index(a)
    # end = ks.index(b)

    return ks, d


def routedist(points):
    ks, distances = shortestDists()
    total = sum(distances[a][b] for a, b in zip(points, points[1:]))

    return total


def groceriesDelivery(home, store, deliveries):
    ks, distances = shortestDists()
    home_idx = ks.index(home)
    store_idx = ks.index(store)
    deliveries_idx = [ks.index(d) for d in deliveries]

    total = 0


    # home to store
    total += distances[home_idx][store_idx]

    rest_dist = 1e7

    for p in permutations(deliveries_idx):
        p = list(p)
        p.insert(0, store_idx)
        p.append(home_idx)
        p_dist = routedist(p)
        if p_dist < rest_dist:
            rest_dist = p_dist
    
    return round(total + rest_dist)


map = """
   |   |   |   |   |   |   |   |   | 
9 -+->-+->-+->-+->-+->-+->-+->-+->-+-
   |   |   |   |   |   |   |   |   | 
   ^   v   ^   v   ^   v   ^   v   ^ 
   |   |   |   |   |   |   |   |   | 
8 -+-<-+-<-+-<-+-<-+-<-+-<-+-<-+-<-+-
   |   |   |   |   |   |   |   |   | 
   ^   v   ^   v   ^   v   ^   v   ^ 
   |   |   |   |   |   |   |   |   | 
7 -+->-+->-+->-+->-+->-+->-+->-+->-+-
   |   |   |   |   |   |   |   |   | 
   ^   v   ^   v   ^   v   ^   v   ^ 
   |   |   |   |   |   |   |   |   | 
6 -+-<-+-<-+-<-+-<-+-<-+-<-+-<-+-<-+-
   |   |   |   |   |   |   |   |   | 
   ^   v   ^   v   ^   v   ^   v   ^ 
   |   |   |   |   |   |   |   |   | 
5 -+->-+->-+->-+->-X->-+->-+->-+->-+-
   |   |   |   |   |   |   |   |   |   
   ^   v   ^   v   ^   v   ^   v   ^ 
   |   |   |   |   |   |   |   |   | 
4 -+-<-+-<-+-<-+-<-+-<-S-<-+-<-+-<-+-
   |   |   |   |   |   |   |   |   |  
   ^   v   ^   v   ^   v   ^   v   ^  
   |   |   |   |   |   |   |   |   | 
3 -+->-H->-+->-+->-+->-+->-+->-+->-+-
   |   |   |   |   |   |   |   |   |  
   ^   v   ^   v   ^   v   ^   v   ^  
   |   |   |   |   |   |   |   |   | 
2 -Y-<-+-<-+-<-+-<-+-<-+-<-+-<-+-<-+-
   |   |   |   |   |   |   |   |   |  
   ^   v   ^   v   ^   v   ^   v   ^  
   |   |   |   |   |   |   |   |   | 
1 -+->-+->-Z->-+->-+->-+->-+->-+->-+-
   |   |   |   |   |   |   |   |   | 
   A   B   C   D   E   F   G   H   I

Home to Store: 7
Store to Xavier: 2
Xavier to Zora: 10
Zora to Yvonne: 3
Yvonne to Home: 2

Total: 24
"""


mapvertices = """
   |   |   |   |   |   |   |   |   | 
9 -72>-73>-74>-75>-76>-77>-78>-79>-80
   |   |   |   |   |   |   |   |   | 
   ^   v   ^   v   ^   v   ^   v   ^ 
   |   |   |   |   |   |   |   |   | 
8 -63<-64<-65<-66<-67<-68<-69<-70<-71
   |   |   |   |   |   |   |   |   | 
   ^   v   ^   v   ^   v   ^   v   ^ 
   |   |   |   |   |   |   |   |   | 
7 -54>-55>-56>-57>-58>-59>-60>-61>-62
   |   |   |   |   |   |   |   |   | 
   ^   v   ^   v   ^   v   ^   v   ^ 
   |   |   |   |   |   |   |   |   | 
6 -45<-46<-47<-48<-49<-50<-51<-52<-53
   |   |   |   |   |   |   |   |   | 
   ^   v   ^   v   ^   v   ^   v   ^ 
   |   |   |   |   |   |   |   |   | 
5 -36>-37>-38>-39>-40>-41>-42>-43>-44
   |   |   |   |   |   |   |   |   |   
   ^   v   ^   v   ^   v   ^   v   ^ 
   |   |   |   |   |   |   |   |   | 
4 -27<-28<-29<-30<-31<-32<-33<-34<-35
   |   |   |   |   |   |   |   |   |  
   ^   v   ^   v   ^   v   ^   v   ^  
   |   |   |   |   |   |   |   |   | 
3 -18>-19>-20>-21>-22>-23>-24>-25>-26
   |   |   |   |   |   |   |   |   |  
   ^   v   ^   v   ^   v   ^   v   ^  
   |   |   |   |   |   |   |   |   | 
2 -9-<-10<-11<-12<-13<-14<-15<-16<-17
   |   |   |   |   |   |   |   |   |  
   ^   v   ^   v   ^   v   ^   v   ^  
   |   |   |   |   |   |   |   |   | 
1 -0->-1->-2->-3->-4->-5->-6->-7->-8-
   |   |   |   |   |   |   |   |   | 
   A   B   C   D   E   F   G   H   I 
"""


"""
pairtest(leftint("C1"), "B1",
         rightint("G3"), "H3",
         upint("E2"), "E3",
         downint("H8"), "H7",

         isns("A1"), True,
         isns("A2"), True,
         isns("B1"), False,
         isns("C1"), True,
         isns("D1"), False,
         isns("E1"), True,
         isns("F1"), False,
         isns("G1"), True,
         isns("H1"), False,
         isns("I1"), True,

         iswe("A1"), True,
         iswe("A2"), False,
         )
"""



"""
pairtest(shortestDist("A1", "D1"), 3,
         shortestDist("A1", "D2"), 6,
         shortestDist("A1", "A9"), 8,

         shortestDist("B3", "F4"), 7,
         
         )
"""

"""
pairtest(routedist([0, 1, 2, 3]), 3,
         routedist([0, 9, 19, 28]), 6)
"""

pairtest(groceriesDelivery("B3", "F4", ["E5", "A2", "C1"]), 24,
         groceriesDelivery("H2", "A2", ["A9", "H9"]), 28,
         groceriesDelivery("A3", "A8", ["A5"]), 20,
         groceriesDelivery("A3", "A5", ["A8"]), 16,
         groceriesDelivery("F1", "C8", ["B4", "E7", "A3"]), 36,
         groceriesDelivery("D3", "A8", ["C3", "H7", "E6", "F9"]), 32,
         groceriesDelivery("C3", "B7", ["B2", "E5", "A6", "D7", "F2"]), 28,
         groceriesDelivery("A2", "H7", ["E2", "F8", "G3", "D1", "I6"]), 40,

)

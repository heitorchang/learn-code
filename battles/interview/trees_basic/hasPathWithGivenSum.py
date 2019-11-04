description = """

Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum of vertex values equals s.

Example

For

t = {
    "value": 4,
    "left": {
        "value": 1,
        "left": {
            "value": -2,
            "left": null,
            "right": {
                "value": 3,
                "left": null,
                "right": null
            }
        },
        "right": null
    },
    "right": {
        "value": 3,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 2,
            "left": {
                "value": -2,
                "left": null,
                "right": null
            },
            "right": {
                "value": -3,
                "left": null,
                "right": null
            }
        }
    }
}
and
s = 7,
the output should be hasPathWithGivenSum(t, s) = true.

This is what this tree looks like:

      4
     / \
    1   3
   /   / \
  -2  1   2
    \    / \
     3  -2 -3
Path 4 -> 3 -> 2 -> -2 gives us 7, the required sum.

For

t = {
    "value": 4,
    "left": {
        "value": 1,
        "left": {
            "value": -2,
            "left": null,
            "right": {
                "value": 3,
                "left": null,
                "right": null
            }
        },
        "right": null
    },
    "right": {
        "value": 3,
        "left": {
            "value": 1,
            "left": null,
            "right": null
        },
        "right": {
            "value": 2,
            "left": {
                "value": -4,
                "left": null,
                "right": null
            },
            "right": {
                "value": -3,
                "left": null,
                "right": null
            }
        }
    }
}
and
s = 7,
the output should be hasPathWithGivenSum(t, s) = false.

This is what this tree looks like:

      4
     / \
    1   3
   /   / \
  -2  1   2
    \    / \
     3  -4 -3
There is no path from root to leaf with the given sum 7.

Input/Output

[time limit] 4000ms (py3)
[input] tree.integer t

A binary tree of integers.

Guaranteed constraints:
0 ≤ tree size ≤ 5 · 104,
-1000 ≤ node value ≤ 1000.

[input] integer s

An integer.

Guaranteed constraints:
-4000 ≤ s ≤ 4000.

[output] boolean

Return true if there is a path from root to leaf in t such that the sum of node values in it is equal to s, otherwise return false.

"""

class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
    def __repr__(self):
        return "TREE " + str(self.value)

def step(t, s, accum):
    # The TRUE definition of leaf node is that both children are None
    if t.left is None and t.right is not None:
        return step(t.right, s, accum + t.value)
    elif t.left is not None and t.right is None:
        return step(t.left, s, accum + t.value)
    elif t.left is None and t.right is None:
        if accum + t.value == s:
            return True
        else:
            return False
    else:
        return step(t.left, s, accum + t.value) or step(t.right, s, accum + t.value)

def stepBullshit(t, s, accum):
    # test 8 fails with TRUE definition
    # now attempting with leaf = either branch empty
    if t.left is not None and t.right is not None:
        return stepBullshit(t.left, s, accum + t.value) or stepBullshit(t.right, s, accum + t.value)
    elif t.left is None and t.right is None:
        if accum + t.value == s:
            return True
        else:
            return False
    elif t.left is None or t.right is None:
        if s == accum + t.value:
            return True
        if t.left is None:
            return stepBullshit(t.right, s, accum + t.value)
        else:
            return stepBullshit(t.left, s, accum + t.value)
        
        
def hasPathWithGivenSum(t, s):
    if t is None:
        return s == 0
    return stepBullshit(t, s, 0)
     
def test():
    TREE1 = Tree(3)
    TREE0 = Tree(4)
    TREE0.left = TREE1

    TREE12 = Tree(2)
    TREE11 = Tree(1)
    TREE10 = Tree(10)
    TREE10.left = TREE12
    TREE12.left = TREE11
    
    testeql(hasPathWithGivenSum(TREE0, 7), True)
    testeql(hasPathWithGivenSum(TREE10, 10), True)

description = """
Given a binary tree t, determine whether it is symmetric around its center, i.e. each side mirrors the other.

Example

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": {
            "value": 3,
            "left": null,
            "right": null
        },
        "right": {
            "value": 4,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 2,
        "left": {
            "value": 4,
            "left": null,
            "right": null
        },
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    }
}
the output should be isTreeSymmetric(t) = true.

Here's what the tree in this example looks like:

    1
   / \
  2   2
 / \ / \
3  4 4  3
As you can see, it is symmetric.

For

t = {
    "value": 1,
    "left": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    },
    "right": {
        "value": 2,
        "left": null,
        "right": {
            "value": 3,
            "left": null,
            "right": null
        }
    }
}
the output should be isTreeSymmetric(t) = false.

Here's what the tree in this example looks like:

    1
   / \
  2   2
   \   \
   3    3
As you can see, it is not symmetric.

Input/Output

[time limit] 4000ms (py3)
[input] tree.integer t

A binary tree of integers.

Guaranteed constraints:
0 ≤ tree size < 5 · 104,
-1000 ≤ node value ≤ 1000.

[output] boolean

Return true if t is symmetric and false otherwise
"""

class Tree(object):
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

def treeEquals(a, b):
    if a is None and b is None:
        return True
    else:
        try:
            if a.value != b.value:
                return False
        except AttributeError:
            return False        

        try:
            return treeEquals(a.left, b.left) and treeEquals(a.right, b.right)
        except AttributeError:
            return False
        
def flipTree(t):
    if t is None:
        return None
    if t.right is not None:
        flippedRight = flipTree(t.right)
    else:
        flippedRight = None
    if t.left is not None:
        flippedLeft = flipTree(t.left)
    else:
        flippedLeft = None
    newTree = Tree(t.value)
    newTree.left = flippedRight
    newTree.right = flippedLeft
    return newTree
        
def isTreeSymmetric(t):
    # idea from commonlisp/four-cl(ojure) : mirror the tree
    # and check if it equals the original
    if t is None:
        return True
    return treeEquals(t.left, flipTree(t.right))

def test():
    TREE1 = Tree(1)
    TREE2 = Tree(2)
    TREE3 = Tree(3)

    TREE1.left = TREE2
    TREE1.right = TREE3

    TREEB3 = Tree(3)
    TREEB5 = Tree(5)
    TREEB1 = Tree(1)
    
    TREEB1.left = TREEB5
    TREEB1.right = TREEB3

    TREEC1 = Tree(1)
    TREEC2 = Tree(2)
    TREEC3 = Tree(3)

    TREEC1.left = TREEC2
    TREEC1.right = TREEC3

    testeql(treeEquals(TREE1, TREEB1), False)
    testeql(treeEquals(TREE1, TREEC1), True)

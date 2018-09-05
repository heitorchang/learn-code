description = """
For the purposes of this challenge, we define a binary search tree to be a binary tree with the following properties:

The data value of every node in a node's left subtree is less than the data value of that node.
The data value of every node in a node's right subtree is greater than the data value of that node.
The data value of every node is distinct.
For example, the image on the left below is a valid BST. The one on the right fails on several counts: 
- All of the numbers on the right branch from the root are not larger than the root. 
- All of the numbers on the right branch from node 5 are not larger than 5. 
- All of the numbers on the left branch from node 5 are not smaller than 5. 
- The data value 1 is repeated.
"""


""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    elts = []

    # Idea: use in-order traversal to build elts then check if it's ordered

    def inorder_traverse(root):
        if root.left:
            inorder_traverse(root.left)
        elts.append(root.data)
        if root.right:
            inorder_traverse(root.right)

    inorder_traverse(root)

    for i in range(1, len(elts)):
        if elts[i] - elts[i-1] <= 0:
            return False
    return True

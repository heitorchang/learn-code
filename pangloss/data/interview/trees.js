data = data.concat([

////////////////////////////////////////////////////////////
//
// TREES
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Trees',
    title: 'Binary Tree traversal',
    reference: 'Foundations of CS',
    description: `A binary tree consists of a record with a left and right branch, and may be traversed recursively. Starting on the root node, draw a curve counterclockwise (moving to the left at first). In preorder traversal, we print the node as the curve touches its left edge. For postorder, we use each node's right edge. For inorder, we use each node's bottom edge.`,
    code: `
class Tree:  # a single node is a tree
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def preorder(self):
        print(self.value, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value, end=" ")

    def inorder(self):
        if self.left:
            self.left.inorder()

        print(self.value, end=" ")
        
        if self.right:
            self.right.inorder()
    
    `
  },

  { // begin new topic
    topic: 'Trees',
    title: 'Red-Black Tree',
    reference: '',
    description: `A red-black tree is a self-balancing binary search tree. The color property of each node is used to balance the tree upon insertions or deletions. Rebalancing involves recoloring and rotating the tree.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Trees',
    title: 'BFS (Breadth-First Search)',
    reference: '',
    description: `See Graphs: BFS`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Trees',
    title: 'DFS (Depth-First Search)',
    reference: '',
    description: `See Graphs: DFS`,
    code: `
    
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },


]);

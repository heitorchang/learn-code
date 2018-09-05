from queue import Queue

class Tree:  # a single node is a tree
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    # Depth-first search
    # most commonly seen using recursion on the
    # branches of the tree

    # See also iterative method with stack in dfs method
    
    # Foundations of CS Tree
    #         +
    #        / \
    #       a   *
    #          / \
    #         -   d
    #        / \
    #       b   c

    # Visualize a circle around each node
    # Then, visualize a curve starting at the root
    # and making its ways starting on the left,
    # and moving counterclockwise
    
    # preorder print order is the sequence where this curve
    # touches the left side of the circle around a node
    # + a * - b c d

    # postorder prints when the curve touches the right side
    # a b c - d * +

    # inorder prints when the curve touches the bottom
    # a + b - c * d
    
    def preorder(self):
        # print("Preorder")
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

        # print in between left and right
        print(self.value, end=" ")
        
        if self.right:
            self.right.inorder()

    # Breadth-first search
    # Also called level-order
    def bfs(self):
        q = Queue()
        q.put(self)

        while q.qsize() > 0:
            cur_node = q.get()
            if cur_node.left:
                q.put(cur_node.left)
            if cur_node.right:
                q.put(cur_node.right)
            print(cur_node.value, end=" ")
            
    def __repr__(self):  # uses Breadth-first search
        tree_repr = ""
        
        q = Queue()
        # visited = []  # since tree only grows downward,
                        # we do not need to mark nodes as visited
        q.put(self)

        # keep track of depth to print tree
        cur_depth = 0
        depth_q = Queue()
        depth_q.put(cur_depth)
        last_depth = 0
        
        while q.qsize() > 0:
            cur_node = q.get()
            cur_value = cur_node.value
            
            cur_depth = depth_q.get()
            
            if cur_node.left:
                q.put(cur_node.left)
                depth_q.put(cur_depth+1)
                
            if cur_node.right:
                q.put(cur_node.right)
                depth_q.put(cur_depth+1)
                
            if cur_depth > last_depth:
                # print()  # went deeper
                tree_repr += "\n"
                last_depth = cur_depth
                
            # print(cur_value, end=" ")
            tree_repr += cur_value + " "
            
        # print()
        tree_repr += "\n"
        return tree_repr

    # Depth-first search with stack
    def dfs(self):
        stack = []
        stack.append(self)

        result = []
        while stack:
            cur_node = stack.pop()
            result.append(cur_node.value)
            if cur_node.left:
                stack.append(cur_node.left)
            if cur_node.right:
                stack.append(cur_node.right)
        return result  # reversed values of postorder traversal
        
def leaf(value):  # shortcut for a leaf
    return Tree(value, None, None)

t_3 = Tree(3, leaf(4), leaf(5))
t_2 = Tree(2, leaf(6), leaf(7))
t_1 = Tree(1, t_3, None)
t_0 = Tree(0, t_1, t_2)
        
t_alt = Tree(0,
             Tree(1, Tree(3, leaf(4), leaf(5)), None),
             Tree(2, leaf(6), leaf(7)))

# https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search
t_wikipedia = Tree("F",
                   Tree("B", leaf("A"),
                        Tree("D", leaf("C"), leaf("E"))),
                   Tree("G", None, Tree("I", leaf("H"), None)))

t_foundations = Tree("+", leaf("a"), Tree("*", Tree("-", leaf("b"), leaf("c")), leaf("d")))

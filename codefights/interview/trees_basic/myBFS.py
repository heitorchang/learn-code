# I onlyremember that BFS uses a queue

class Tree:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None

    def __repr__(self):
        return "TREE(%d)" % self.value

def myBFS(t):
    q = []
    q.append(t)
    nodes = []
    
    while q:
        curNode = q.pop()
        if curNode.left:
            q.insert(0, curNode.left)
        if curNode.right:
            q.insert(0, curNode.right)
        # print(curNode)
        nodes.append(curNode.value)
    return nodes
        
def test():
    #      1
    #     / \
    #    2   3
    #   / \   \
    #  4  5    6
    
    TREE4 = Tree(4)
    TREE5 = Tree(5)
    TREE6 = Tree(6)
    TREE2 = Tree(2)
    TREE3 = Tree(3)
    TREE1 = Tree(1)
    
    TREE1.left = TREE2
    TREE1.right = TREE3

    TREE2.left = TREE4
    TREE2.right = TREE5

    TREE3.right = TREE6
    
    testeql(myBFS(TREE1), [1,2,3,4,5,6])


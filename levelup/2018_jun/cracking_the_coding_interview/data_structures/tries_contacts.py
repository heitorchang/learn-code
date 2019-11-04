description = """
We're going to make our own Contacts application! The application must perform two types of operations:

add name, where name is a string denoting a contact name. This must store name as a new contact in the application.
find partial, where partial is a string denoting a partial name to search the application for. It must count the number of contacts starting with partial and print the count on a new line.
Given n sequential add and find operations, perform each operation in order.
"""

class Node:
    def __init__(self, letter=None):
        self.letter = letter
        self.count = 1
        self.children = []

    def hasChild(self, letter):
        for c in self.children:
            if c.letter == letter:
                return True
        return False

    def getChild(self, letter):
        for ch in self.children:
            if ch.letter == letter:
                return ch
                
    def __repr__(self):
        return "{} ({}) {}".format(self.letter, self.count, self.children)

t = Node()

def contacts(t, op, s):
    if op == 'add':
        curNode = t
        for c in s:
            if curNode.hasChild(c):
                curNode.getChild(c).count += 1
            else:
                curNode.children.append(Node(c))
            curNode = curNode.getChild(c)
    else:  # op is find
        # navigate t to find s
        curNode = t
        for c in s:
            curNode = curNode.getChild(c)
            if curNode is None:
                print(0)
                return 
        print(curNode.count)

contacts(t, 'add', 'ch')
contacts(t, 'add', 'cat')
contacts(t, 'add', 'cate')
print(contacts(t, 'find', 'ca'))
print(t)
        

def test():
    pass


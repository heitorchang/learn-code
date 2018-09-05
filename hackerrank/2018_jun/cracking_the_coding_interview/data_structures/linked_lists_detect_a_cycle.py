description = """
A linked list is said to contain a cycle if any node is visited more than once while traversing the list. For example, in the following graph there is a cycle formed when node  points back to node .

image

Function Description

Complete the function has_cycle in the editor below. It must return a boolean True if the graph contains a cycle, or False.
"""

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle(head):
    if head.next is None:
        return False
    else:
        if head.data is None:
            return True
        head.data = None  # some sentinel value to indicate it was visited
        return has_cycle(head.next)
        

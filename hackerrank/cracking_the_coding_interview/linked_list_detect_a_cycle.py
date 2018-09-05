"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""


def has_cycle_mark_visited(head):
    # first attempt, ugly
    if not head.next:
        return False
    try:
        if head.visited:
            return True
    except AttributeError:
        head.visited = True
    return has_cycle(head.next)

def has_cycle(head):
    # consider two pointers as "cars on a racetrack". If there is a loop, the two pointers will eventually collide
    if not head:
        return False
    fast = head.next
    slow = head
    while fast is not None and fast.next is not None and slow is not None:
        if fast == slow:
            return True
        fast = fast.next.next
        slow = slow.next
    return False

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    prev = l
    head = l
    
    # make sure head is not k
    while head:
        if head.value == k:
            head = head.next
        else:
            break

    cur = head 

    while cur:
        if cur.value == k:
            prev.next = cur.next
        else:
            # advance only if value is not k
            prev = cur
        cur = cur.next

    return head

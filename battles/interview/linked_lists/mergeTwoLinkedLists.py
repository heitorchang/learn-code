# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def mergeTwoLinkedLists(l1, l2):
    ans = []
    while True:
        if l1 is None and l2 is None:
            break
        try:
            v1 = l1.value
        except AttributeError:
            v1 = float('inf')
        
        try:
            v2 = l2.value
        except AttributeError:
            v2 = float('inf')
        
        if v1 < v2:
            ans.append(v1)
            l1 = l1.next
        else:
            ans.append(v2)
            l2 = l2.next
    return ans

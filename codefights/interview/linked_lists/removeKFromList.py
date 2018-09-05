description = """
Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in the list, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers l and a non-negative integer k, remove all elements from list l that have a value equal to k.

Example

For l = [3, 1, 2, 3, 4, 5] and k = 3, the output should be
removeKFromList(l, k) = [1, 2, 4, 5];
For l = [1, 2, 3, 4, 5, 6, 7] and k = 10, the output should be
removeKFromList(l, k) = [1, 2, 3, 4, 5, 6, 7].
Input/Output

[time limit] 4000ms (py3)
[input] linkedlist.integer l

A singly linked list of integers.

Guaranteed constraints:
0 ≤ list size ≤ 105,
-1000 ≤ element value ≤ 1000.

[input] integer k

A non-negative integer.

Guaranteed constraints:
-1000 ≤ k ≤ 1000.

[output] linkedlist.integer

Return l with all the values equal to k removed.
"""

class ListNode(object):
   def __init__(self, x):
     self.value = x
     self.next = None

def test():
    LL0 = ListNode(3)
    LL1 = ListNode(1)
    LL2 = ListNode(2)
    LL3 = ListNode(3)
    LL4 = ListNode(4)
    LL5 = ListNode(5)

    LL0.next = LL1
    LL1.next = LL2
    LL2.next = LL3
    LL3.next = LL4
    LL4.next = LL5

    LR0 = ListNode(1)
    LR1 = ListNode(2)
    LR2 = ListNode(4)
    LR3 = ListNode(5)

    LR0.next = LR1
    LR1.next = LR2
    LR2.next = LR3
    
    # testeql(removeKFromList(LL0, 3), LR0)
    testeql(removeKFromList(LL0, 3), [1,2,4,5])

def removeKFromListNonOptimal(L, k):
    result = []
    while L is not None:
        pr('L.value')
        if L.value != k:
            result.append(L.value)
        L = L.next
    return result

def removeKFromListTopVoted(l, k):
    c = l
    while c:
        if c.next and c.next.value == k:
            c.next = c.next.next
        else:
            c = c.next
    return l.next if l and l.value == k else l

def removeKFromListOtherSolution(l, k):
    h = l;    
    
    if h == None:
        return h
    
    while h != None and h.value == k:
        temp = h.next
        h.next = None
        h = temp
        l = h
    
    if h == None:
        return h
    
    while h.next != None:
        if h.next.value == k:
            h.next = h.next.next
        else:
            h = h.next

    return l

def removeKFromList(L, k):
    result = L
    while L is not None:
        if result.value == k:
            result = result.next
        L = L.next
    return result

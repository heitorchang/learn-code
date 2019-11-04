description = """

Note: Try to solve this task in O(n) time using O(1) additional space, where n is the number of elements in l, since this is what you'll be asked to do during an interview.

Given a singly linked list of integers, determine whether or not it's a palindrome.

Example

    For l = [0, 1, 0], the output should be
    isListPalindrome(l) = true;
    For l = [1, 2, 2, 3], the output should be
    isListPalindrome(l) = false.

Input/Output

    [time limit] 4000ms (py3)

    [input] linkedlist.integer l

    A singly linked list of integers.

    Guaranteed constraints:
    0 ≤ list size ≤ 5 · 105,
    -109 ≤ element value ≤ 109.

    [output] boolean

    Return true if l is a palindrome, otherwise return false.

"""


# Definition for singly-linked list:
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None

def test():
    print("isListPalindrome tests")
    LN0 = ListNode(0)
    LN1 = ListNode(1)
    LN2 = ListNode(0)
    
    LN0.next = LN1
    LN1.next = LN2
    testeql(isListPalindrome(LN0), True)

    LNB0 = ListNode(0)
    LNB1 = ListNode(1)
    LNB2 = ListNode(1)

    LNB0.next = LNB1
    LNB1.next = LNB2
    testeql(isListPalindrome(LNB0), False)







    





# solution by mike_e2

def isListPalindrome(l):
    if l == None:
        return True
    
    # set i to point to middle of list using runner j
    i = j = l
    
    while j.next != None:
        j = j.next.next
        if j == None:
            break
        i = i.next

    # reverse second half of list 
    h = i.next
    k = None
    
    while h != None:
        j = h.next
        h.next = k
        k = h
        i.next = h
        h = j
    
    # match first half to reversed second half
    i = i.next
    
    while i != None:        
        if l.value != i.value:
            return False      
        i = i.next
        l = l.next

    return True


def isListPalindromeCheat(l):
    m = []
    while l is not None:
        m.append(l.value)
        l = l.next
    return m == m[::-1]

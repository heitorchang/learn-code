# Linked lists

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    """add, delete, nth, reverse, __len__"""
    def __init__(self):
        self.head = None


    def add(self, value):
        """Define new node's value and next, then make it the list's head"""
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    def delete(self, to_delete):
        """delete the first occurrence of value"""
        current_node = self.head
        previous_node = None

        while current_node:
            if current_node.value == to_delete:
                break
            previous_node = current_node
            current_node = current_node.next

        if current_node is None:
            print("Item not found")
            return None

        if previous_node is None:
            # special case (head is removed)
            self.head = self.head.next
        else:
            previous_node.next = current_node.next


    def nth(self, n):
        """print nth item in list"""
        current_node = self.head
        for i in range(n):
            current_node = current_node.next
        print(current_node.value)


    def reverse(self):
        """Uses O(n) memory"""
        reversed = LinkedList()
        current_node = self.head

        while current_node:
            # insert current_node in reversed
            reversed.add(current_node.value)
            current_node = current_node.next
        return reversed


    def print_me(self):
        current_node = self.head
        while True:
            if current_node:
                print(current_node.value)
                current_node = current_node.next
            else:
                break


    def __len__(self):
        length = 0
        current_node = self.head
        while current_node:
            length += 1
            current_node = current_node.next
        return length


def test_delete_head():
    alist = LinkedList()
    alist.add(3)
    alist.add(4)
    alist.add(5)
    alist.delete(5)
    alist.print_me()


def test_delete_mid():
    alist = LinkedList()
    alist.add(3)
    alist.add(4)
    alist.add(5)
    alist.delete(4)
    alist.print_me()


def test_delete_last():
    alist = LinkedList()
    alist.add(3)
    alist.add(4)
    alist.add(5)
    alist.delete(3)
    alist.print_me()


def test_delete_not_found():
    alist = LinkedList()
    alist.add(3)
    alist.add(4)
    alist.add(5)
    alist.delete(9)
    alist.print_me()


def test_reverse():
    alist = LinkedList()
    # 5 4 3
    alist.add(3)
    alist.add(4)
    alist.add(5)

    print("original:")
    alist.print_me()

    revlist = alist.reverse()
    print("reversed:")
    revlist.print_me()


def test_nth():
    alist = LinkedList()
    alist.add(3)
    alist.add(4)
    alist.add(5)

    alist.nth(0)
    alist.nth(1)


def test_print_rev():
    alist = LinkedList()
    alist.add(3)
    alist.add(4)
    alist.add(5)

    for i in range(len(alist) - 1, -1, -1):
        alist.nth(i)

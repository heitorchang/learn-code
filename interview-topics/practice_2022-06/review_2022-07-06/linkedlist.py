class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def print_me(self):
        cur = self.head
        while cur:
            print(cur.value, end=", ")
            cur = cur.next
        print()


    def add(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node


    def delete(self, to_delete):
        cur = self.head
        prev = None

        while cur:
            if cur.value == to_delete:
                break
            prev = cur
            cur = cur.next

        if cur is None:
            print("to_delete", to_delete, "not found")
            return

        if prev is None:
            self.head = self.head.next
        else:
            prev.next = cur.next
            return to_delete


    def delete_all(self, to_delete):
        cur = self.head
        prev = None

        # if head is to be deleted
        while cur and cur.value == to_delete:
            self.head = cur.next
            cur = cur.next

        while cur:
            while cur and cur.value != to_delete:
                prev = cur
                cur = cur.next
            if cur is None:
                return self.head
            prev.next = cur.next
            cur = cur.next


def test_add():
    alist = LinkedList()
    alist.add(3)
    alist.add(90)
    alist.print_me()


def test_delete():
    alist = LinkedList()
    alist.add(3)
    alist.add(4)
    alist.add(5)
    alist.print_me()
    alist.delete(4)
    alist.print_me()
    alist.delete(99)


def test_delete_all():
    alist = LinkedList()
    alist.add(1)
    alist.add(1)
    alist.add(1)
    alist.add(5)
    alist.add(1)
    alist.add(5)
    alist.delete_all(1)
    alist.print_me()

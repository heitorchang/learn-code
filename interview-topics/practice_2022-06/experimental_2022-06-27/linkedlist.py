class Node:
    def __init__(self, value):
        self.value = value
        self.next_node = None


class LinkedList:
    def __init__(self):
        self.head = None


    def count(self):
        total = 0
        current_node = self.head
        while current_node:
            total += 1
            current_node = current_node.next_node
        return total


    def add(self, value):
        """first, define the new node fully, then set self.head to the new node"""
        new_node = Node(value)
        new_node.next_node = self.head
        self.head = new_node


    def delete_all(self, value_to_delete):
        """
        remember that previous_node is None. if there is a match, advance head or previous_node's next,
        depending on whether previous_node is None or not.
        otherwise, advance both previous_node and current_node.
        """

        current_node = self.head
        previous_node = None

        while current_node:
            if current_node.value == value_to_delete:
                if previous_node is None:
                    self.head = current_node.next_node
                else:
                    previous_node.next_node = current_node.next_node
            else:
                previous_node = current_node
            current_node = current_node.next_node


    def print_me(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end="")
            current_node = current_node.next_node
            if current_node:
                print(", ", end="")
        print()


def test_linked_list():
    alist = LinkedList()
    alist.add(3)
    alist.add(3)
    alist.add(3)
    alist.add(2)
    alist.add(2)
    alist.add(3)
    alist.add(2)
    alist.add(1)
    print("before delete")
    alist.print_me()

    alist.delete_one(2)
    alist.delete_one(3)

    print("after delete")
    alist.print_me()


def test_delete_single_node():
    alist = LinkedList()
    alist.add(3)
    alist.delete_one(3)
    alist.print_me()


def test_delete_pair():
    alist = LinkedList()
    alist.add(3)
    alist.add(3)
    alist.delete_one(3)
    alist.print_me()


def test_delete_all_no_match():
    alist = LinkedList()
    alist.add(2)
    alist.add(2)

    alist.delete_all(1)
    alist.print_me()


def test_delete_all_single():
    alist = LinkedList()
    alist.add(1)

    alist.delete_all(1)
    alist.print_me()


def test_delete_all_pair():
    alist = LinkedList()
    alist.add(1)
    alist.add(1)
    alist.add(1)
    alist.add(1)

    alist.delete_all(1)
    alist.print_me()


def test_delete_all_mixed():
    alist = LinkedList()
    alist.add(1)
    alist.add(2)
    alist.add(2)
    alist.add(1)
    alist.add(1)
    alist.add(2)
    alist.add(2)
    alist.add(3)

    alist.delete_all(1)
    alist.print_me()


def test_delete_all_mixed_ends():
    alist = LinkedList()
    alist.add(1)
    alist.add(1)
    alist.add(2)
    alist.add(1)
    alist.add(1)
    alist.add(1)
    alist.add(2)
    alist.add(1)
    alist.add(2)
    alist.add(2)
    alist.add(1)
    alist.add(5)
    alist.add(1)
    alist.add(3)
    alist.add(2)
    alist.add(1)
    alist.add(1)

    alist.delete_all(1)
    alist.print_me()


def test_count():
    alist = LinkedList()
    alist.add(2)
    alist.add(3)
    alist.add(4)
    print(alist.count())

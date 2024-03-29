class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Given a reference (pointer to pointer)
# to the head of a list and an int,
# inserts a new node on the front of the list.


def push(head_ref, new_data):
    new_node = Node(0)
    new_node.data = new_data
    new_node.next = (head_ref)
    (head_ref) = new_node
    return head_ref

# Given a reference (pointer to pointer)
# to the head of a list and a key,
# deletes all occurrence of the given key
# in linked list


def deleteKey(head_ref, key):

    # Store head node
    temp = head_ref
    prev = None

    # If head node itself holds the key
    # or multiple occurrences of key
    while (temp != None and temp.data == key):
        head_ref = temp.next  # Changed head
        temp = head_ref         # Change Temp

    # Delete occurrences other than head
    while (temp != None):

        # Search for the key to be deleted,
        # keep track of the previous node
        # as we need to change 'prev.next'
        while (temp != None and temp.data != key):
            prev = temp
            #debug
            print("set prev to", temp.data)
            temp = temp.next

        # If key was not present in linked list
        if (temp == None):
            return head_ref

        # Unlink the node from linked list
        prev.next = temp.next

        # Update Temp for next iteration of outer loop
        temp = prev.next
    return head_ref

# This function prints contents of linked list
# starting from the given node


def printList(node):
    while (node != None):
        print(node.data, end=" ")
        node = node.next


# Driver Code
if __name__ == '__main__':

    # Start with the empty list
    head = None

    head = push(head, 5)
    head = push(head, 1)
    head = push(head, 1)
    head = push(head, 1)
    key = 1  # key to delete

    print("Created Linked List: ")
    printList(head)

    # Function call
    head = deleteKey(head, key)
    print("\nLinked List after Deletion is: ")

    printList(head)

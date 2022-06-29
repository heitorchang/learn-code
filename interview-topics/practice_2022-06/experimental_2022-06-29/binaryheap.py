# min priority queue


#####
# BUGGY: cannot pop (delete)
#####

# add: insert at end, then perc_up
# remove: save value at 0. pop last item, put in index 0 and perc_down (using min_child)

class MinPriorityQueue:
    def __init__(self):
        self.heap = []

    def parent(self, index):
        return (index - 1) // 2

    def left(self, index):
        return (2 * index) + 1

    def right(self, index):
        return (2 * index) + 2

    def insert(self, item):
        self.heap.append(item)
        self.perc_up()

    def print_me(self):
        for i in range(len(self.heap)):
            print(f"{self.heap[i]}", end=" ")
            try:
                print(f"[{self.heap[self.left(i)]}, ", end="")
            except IndexError:
                print("no left child", end=" ")

            try:
                print(f"{self.heap[self.right(i)]}]")
            except IndexError:
                print("no right child")

    def min_child(self, parent_index):
        left_index = self.left(parent_index)
        right_index = self.right(parent_index)

        #debug
        print(left_index, right_index, self.heap)

        if left_index >= len(self.heap):
            return None

        if left_index < len(self.heap) - 1 and right_index >= len(self.heap):
            return left_index

        if self.heap[left_index] < self.heap[right_index]:
            return left_index
        return right_index


    def perc_down(self):
        index = 0

        while self.left(index) < len(self.heap):
            min_child_index = self.min_child(index)
            if self.heap[index] > self.heap[min_child_index]:
                self.heap[index], self.heap[min_child_index] = self.heap[min_child_index], self.heap[index]
                index = min_child_index
            else:
                break

    def perc_up(self):
        index = len(self.heap) - 1
        while index > 0:
            parent_index = self.parent(index)
            if self.heap[index] < self.heap[parent_index]:
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def pop(self):
        result = self.heap.pop(0)
        last = self.heap.pop()
        self.heap.insert(0, last)
        self.perc_down()
        return result

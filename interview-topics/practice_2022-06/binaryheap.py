class MinBinaryHeap:
    def __init__(self):
        self.heap = []


    def left_child(self, index):
        return (2 * index) + 1


    def right_child(self, index):
        return (2 * index) + 2


    def parent(self, index):
        return (index - 1) // 2


    def add(self, item):
        """insert item at end and percolate it up"""
        self.heap.append(item)
        self.perc_up()


    def perc_up(self):
        current_index = len(self.heap) - 1
        while current_index > 0:
            parent_index = self.parent(current_index)
            if self.heap[current_index] < self.heap[parent_index]:
                self.heap[current_index], self.heap[parent_index] = self.heap[parent_index], self.heap[current_index]
                current_index = parent_index
            else:
                break

    def delete(self):
        """Save top (first) item to return, move last item to front and percolate it down"""
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        else:
            top = self.heap.pop(0)
            last = self.heap.pop()
            self.heap.insert(0, last)
            self.perc_down()
            return top


    def get_min_child(self, index):
        left_child_index = self.left_child(index)
        right_child_index = self.right_child(index)
        try:
            left = self.heap[left_child_index]
        except IndexError:
            left = None

        try:
            right = self.heap[right_child_index]
        except IndexError:
            right = None

        if left is None and right is None:
            return None

        if left is None:
            return right_child_index

        if right is None:
            return left_child_index

        if left < right:
            return left_child_index
        return right_child_index


    def perc_down(self):
        current_index = 0
        while self.left_child(current_index) < len(self.heap):
            min_child_index = self.get_min_child(current_index)
            if self.heap[current_index] > self.heap[min_child_index]:
                self.heap[current_index], self.heap[min_child_index] = self.heap[min_child_index], self.heap[current_index]
            else:
                return
            current_index = min_child_index


    def print_me(self):
        for i in range(len(self.heap)):
            print(self.heap[i], end=" [")
            try:
                print(self.heap[self.left_child(i)], end=", ")
            except IndexError:
                print("no left child", end=", ")
            try:
                print(self.heap[self.right_child(i)], end="]")
            except IndexError:
                print("no right child", end="]")
            print()


def test_heap():
    h = MinBinaryHeap()
    h.add(8)
    h.add(15)
    h.add(71)
    h.add(391)
    h.add(33)
    h.add(91)
    h.add(5)
    h.add(9)
    h.print_me()

    while len(h.heap) > 0:
        print(h.delete())

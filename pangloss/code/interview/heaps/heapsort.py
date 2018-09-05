class Heap():
    def __init__(self, unsorted):
        self.a = unsorted
        self.heapSize = len(unsorted)

    # consider this structure
    #      0
    #     / \
    #    1   2
    #   / \ / \
    #  3  4 5  6
    
    def left(self, i):
        """index of left child"""
        return 2*i + 1

    def right(self, i):
        """index of right child"""
        return 2*i + 2

    def maxHeapify(self, i):
        left = self.left(i)
        right = self.right(i)
        if left < self.heapSize and self.a[left] > self.a[i]:
            largest = left
        else:
            largest = i
        if right < self.heapSize and self.a[right] > self.a[largest]:
            largest = right
        if largest != i:
            self.a[i], self.a[largest] = self.a[largest], self.a[i]
            self.maxHeapify(largest)

    def buildMaxHeap(self):
        for i in range(self.heapSize//2 - 1, -1, -1):
            self.maxHeapify(i)

    def heapsort(self):
        self.buildMaxHeap()
        for i in range(self.heapSize - 1, 0, -1):
            self.a[0], self.a[i] = self.a[i], self.a[0]
            self.heapSize -= 1
            self.maxHeapify(0)
        self.heapSize = len(self.a)
        return self.a

def main():
    h = Heap([4,1,3,2,16,9,10,14,8,7])
    h.heapsort()
    print(h.a)    

def main2():
    h = Heap([16,4,10,14,7,9,3,2,8,1])
    h.maxHeapify(1)
    print(h.a)
    
def test():
    testeql(Heap([3,1,2]).heapsort(), [1,2,3])
    testeql(Heap([3,7,5,6,1,2,4]).heapsort(), [1,2,3,4,5,6,7])

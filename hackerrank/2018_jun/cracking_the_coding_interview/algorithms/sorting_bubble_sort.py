description = """
Consider the following version of Bubble Sort:

for (int i = 0; i < n; i++) {
    
    for (int j = 0; j < n - 1; j++) {
        // Swap adjacent elements if they are in decreasing order
        if (a[j] > a[j + 1]) {
            swap(a[j], a[j + 1]);
        }
    }
    
}
Task 
Given an -element array, , of distinct elements, sort array  in ascending order using the Bubble Sort algorithm above. Once sorted, print the following three lines:

Array is sorted in numSwaps swaps., where  is the number of swaps that took place.
First Element: firstElement, where  is the first element in the sorted array.
Last Element: lastElement, where  is the last element in the sorted array.
"""

def bubble_sort(a):
    ct = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                ct += 1
                a[j], a[j+1] = a[j+1], a[j]
    return (ct, a[0], a[-1])

def test():
    ct, first, last = bubble_sort([3,1,2])
    print(ct, first, last)

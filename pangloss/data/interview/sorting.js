data = data.concat([

//////////////////////////////////////////////////////////////////////
//
// SORTING
//
//////////////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Sorting',
    title: 'Bubble Sort',
    reference: 'Intro to Algorithms, 40',
    description: ``,
    code: `
def bubbleSort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1, i, -1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr    
    `
  },

  { // begin new topic
    topic: 'Sorting',
    title: 'Insertion Sort',
    reference: 'Intro to Algorithms, 18',
    description: `The numbers we wish to sort are the keys. The procedure is like sorting a hand of playing cards. To find the correct position for a card, we compare it with each of the cards already in the hand, from right to left. Insertion sort rearranges the array in place.`,
    code: `
def insertionSort(arr):
    # begin at the second element
    for j in range(1, len(arr)):
        key = arr[j]
        # insert arr[j] into the sorted sequence arr[0:j]
        i = j - 1
        while i >= 0 and arr[i] > key:
            arr[i+1] = arr[i]
            i -= 1
        arr[i+1] = key
    return arr
    `
  },

  { // begin new topic
    topic: 'Sorting',
    title: 'Merge Sort',
    reference: 'http://interactivepython.org/courselib/static/pythonds/SortSearch/TheMergeSort.html',
    description: ``,
    code: `
def mergeSort(arr):
    n = len(arr)
    if n > 1:
        middle = n // 2
        left = arr[:middle]
        right = arr[middle:]

        mergeSort(left)
        mergeSort(right)

        # merge
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1
    return arr    
    `
  },

  { // begin new topic
    topic: 'Sorting',
    title: 'sorted() function',
    reference: '',
    description: ``,
    code: `
optional parameters:
reverse=True
key=str.lower  # function of one argument applied to each item 
    `
  },

  { // begin new topic
    topic: 'Sorting',
    title: 'Sort a mixed list of strings and integers',
    reference: '',
    description: ``,
    code: `
a = [28, 14, '28', '23', 20]
s = sorted(a, key=int)  # [14, 20, '23', 28, '28']

# downside: must then convert resulting list to a uniform type
    `
  },

  { // begin new topic
    topic: 'Sorting',
    title: 'Sort namedtuples by attributes',
    reference: '',
    description: ``,
    code: `
from collections import namedtuple
from operator import attrgetter

Person = namedtuple('Person', 'name age')
people = [Person("Joe", 34), Person("Amy", 34),
          Person("Jen", 52)]
ps = sorted(people, key=attrgetter('age', 'name'))    
    `
  },

  { // begin new topic
    topic: 'Sorting',
    title: 'Sort list of lists by column',
    reference: 'https://stackoverflow.com/questions/4233476/sort-a-list-by-multiple-attributes',
    description: ``,
    code: `
from operator import itemgetter
    
w = [[12, 'tall', 'blue', 1],
     [2, 'short', 'red', 9],
     [4, 'tall', 'blue', 13]]
s = sorted(w, key=itemgetter(1, 0))
    `
  },

  { // begin new topic
    topic: 'Sorting',
    title: 'Radix Sort',
    reference: 'Algorithms, 198',
    description: `Use a stable sorting algorithm to sort by the ones place, then the tens place, and so on.`,
    code: `
from operator import itemgetter

def radix_sort(lst):
    # set up the list, separating numbers into digits
    lst_str = list(map(str, lst))
    len_longest = len(max(lst_str, key=len))
    lst_pad = [s.zfill(len_longest) for s in lst_str]

    for i in range(len_longest - 1, -1, -1):
        lst_pad.sort(key=itemgetter(i))
    return list(map(int, lst_pad))
    `
  },

  
  { // begin new topic
    topic: 'Sorting',
    title: 'Quicksort',
    reference: 'Intro to Algorithms, 171',
    description: ``,
    code: `
def quicksort(arr):
    def partition(left, right):
        i = left - 1
        for j in range(left, right):
            if arr[j] <= arr[right]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i+1], arr[right] = arr[right], arr[i+1]
        return i + 1

    def quicksortHelper(left, right):
        if left < right:
            middle = partition(left, right)
            quicksortHelper(left, middle - 1)
            quicksortHelper(middle + 1, right)

    quicksortHelper(0, len(arr) - 1)
    return arr    
    `
  },


  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },

  
]);

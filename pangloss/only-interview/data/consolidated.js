var data = [];
data = data.concat([

  { // begin new topic
    topic: 'Random Numbers',
    title: 'Shuffle an array',
    reference: '',
    description: ``,
    code: `
from random import shuffle
    
a = list(range(10))
shuffle(a)
a  # [7, 5, 3, 8, 0, 4, 2, 9, 6, 1]
    `
  },

  { // begin new topic
    topic: 'Random Numbers',
    title: 'Integer, generating a random value',
    reference: '',
    description: ``,
    code: `
from random import randint

n = randint(1, 10)  # both endpoints are included
    `
  },

  { // begin new topic
    topic: 'Random Numbers',
    title: 'SystemRandom',
    reference: '',
    description: `A class that creates random bytes suitable for use in cryptography (if the underlying OS supports it)`,
    code: `
from random import SystemRandom

sr = SystemRandom()
n = sr.randint(1, 10)    
    `
  },

  { // begin new topic
    topic: 'Random Numbers',
    title: 'Floating-point, generating a random value',
    reference: '',
    description: ``,
    code: `
from random import uniform

n = uniform(0.5, 2.5)  # the endpoint may not be included
    `
  },

  { // begin new topic
    topic: 'Random Numbers',
    title: 'Pick a random element',
    reference: '',
    description: ``,
    code: `
from random import choice
    
a = [1, 2, 3, 4, 5, 6]
choice(a)
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

data = data.concat([

////////////////////////////////////////////////////////////
//
// LINKED LISTS
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Linked Lists',
    title: 'List Node',
    reference: '',
    description: ``,
    code: `
class ListNode(object):
    def __init__(self, x):
        self.value = x
        self.next = None
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

data = data.concat([

////////////////////////////////////////////////////////////
//
// LOOPS
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Loops',
    title: 'While loops: know where variables are when they end',
    reference: '',
    description: ``,
    code: `
n = 0
while n < 10:
    n += 1

print(n)  # 10
    `
  },

  { // begin new topic
    topic: 'Loops',
    title: 'While loops: use while True as alternative to do-while',
    reference: '',
    description: `There is no do-while loop in Python. To avoid writing update conditions twice, put a condition inside the while loop to break out.`,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },


]);

data = data.concat([

////////////////////////////////////////////////////////////
//
// QUEUES
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Queues',
    title: 'deque initialization',
    reference: 'https://docs.python.org/3/library/collections.html#collections.deque',
    description: ``,
    code: `
from collections import deque

d = deque([3, 5, 2])
d.append(9)
left = d.popleft()  # 3
d.appendleft(1)
# deque([1, 5, 2, 9])
    
# maxlen is optional
d_fixed_size = deque(range(20), maxlen=5) 
# deque([15, 16, 17, 18, 19], maxlen=5)

d_fixed_size.appendleft(0)
# deque([0, 15, 16, 17, 18], maxlen=5)
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

data = data.concat([

////////////////////////////////////////////////////////////
//
// SEARCHING
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Searching',
    title: 'Binary search',
    reference: 'http://code.activestate.com/recipes/81188-binary-search/',
    description: ``,
    code: `
def binarySearch(arr, x):
    # returns the index of x in arr, or -1 if not found
    # arr must be sorted
    left = 0
    right = len(arr) - 1
    while True:
        if right < left:
            return -1

        midpoint = (left + right) // 2
        if arr[midpoint] < x:
            left = midpoint + 1
        elif arr[midpoint] > x:
            right = midpoint - 1
        else:
            return midpoint    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

data = data.concat([

////////////////////////////////////////////////////////////
//
// DICTIONARIES
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Dictionaries',
    title: 'Invert keys and values',
    reference: '',
    description: `Assume it is one-to-one. Otherwise a single, random key will become the value in the inverted dict.`,
    code: `
d = {'a': 1, 'b': 2, 'c': 30, 'd': 400}

d_inv = {v: k for k, v in d.items()}
#   {400: 'd', 1: 'a', 2: 'b', 30: 'c'}
    `
  },

  { // begin new topic
    topic: 'Dictionaries',
    title: 'Counter',
    reference: '',
    description: `A dict subclass for counting hashable items. Also called a bag or multiset`,
    code: `
from collections import Counter

s = "abracadabra"
s_ctr = Counter(s)  # Counter({'a': 5, 'b': 2, 'r': 2, 'd': 1, 'c': 1})

p = "panama"
p_ctr = Counter(p)

s_ctr - p_ctr  # Counter({'a': 2, 'b': 2, 'r': 2, 'd': 1, 'c': 1})

# total of all counts
sum(s_ctr.values())  # 11

s_ctr.values()  # dict_values([2, 1, 2, 5, 1])
s_ctr.keys()    # dict_keys(['b', 'd', 'r', 'a', 'c'])
    `
  },

  { // begin new topic
    topic: 'Dictionaries',
    title: 'namedtuple',
    reference: 'Python Fluente, p. 56',
    description: `A lightweight, dictionary-like object. Fields are accessed with dot notation.`,
    code: `
from collections import namedtuple

Card = namedtuple("CardDisplay", 'rank suit')
# alternatively namedtuple("CardDisplay", ['rank', 'suit'])

big_two = Card(2, 'Spades')
print(big_two.suit)

print(big_two._asdict())
    `
  },
  
  { // begin new topic
    topic: 'Dictionaries',
    title: 'Creating a dict',
    reference: 'Python Fluente, p. 95',
    description: ``,
    code: `
a = dict(a=1, b=2)
b = {'a': 1, 'b': 2}
c = dict(zip(['a', 'b'], [1, 2]))
d = dict([('a', 1), ('b', 2)])
e = dict({'a': 1, 'b': 2})
    `
  },

  { // begin new topic
    topic: 'Dictionaries',
    title: 'dictcomp (dict comprehension)',
    reference: 'Python Fluente, p. 96',
    description: ``,
    code: `
DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
]

cc = {country: code for code, country in DIAL_CODES}
    `
  },

  { // begin new topic
    topic: 'Dictionaries',
    title: 'Get default value if key not found',
    reference: '',
    description: ``,
    code: `
d = {'a': 1, 'b': 2}
c = d.get('c', 99)
    `
  },

  { // begin new topic
    topic: 'Dictionaries',
    title: 'Set to default value if key not found',
    reference: '',
    description: `If the key, k, is in dict d, return d[k]. Otherwise, set d[k] = default value`,
    code: `
d = {'a': 1, 'b': 2}
b = d.setdefault('b', 99)
c = d.setdefault('c', 99)
b, c, d  # (2, 99, {'c': 99, 'a': 1, 'b': 2})
    `
  },

  { // begin new topic
    topic: 'Dictionaries',
    title: 'defaultdict',
    reference: '',
    description: `Values are created on-demand when a missing key is searched. A function or class is passed as the argument to defaultdict
<br><br>
Note: dd.get(missing_key) returns None`,
    code: `
from collections import defaultdict

dd = defaultdict(list)
dd['a'] = [10]
dd['c'] = [30]

letters = 'abcde'
for i, letter in enumerate(letters):
    dd[letter].append(i+1)

dd  # defaultdict(<class 'list'>,
  # {'e': [5], 'c': [30, 3], 'a': [10, 1],
  #  'd': [4], 'b': [2]})
    `
  },


  { // begin new topic
    topic: 'Dictionaries',
    title: 'OrderedDict',
    reference: '',
    description: `Maintain keys in the order of insertion. popitem(last=True) removes, by default, last-in, first-out.`,
    code: `
from collections import OrderedDict
from operator import itemgetter

d = {'a': 1, 'b': 2, 'c': 3}
od = OrderedDict(sorted(d.items(), key=itemgetter(0)))
    `
  },

  { // begin new topic
    topic: 'Dictionaries',
    title: 'Subclass UserDict instead of dict',
    reference: 'Python Fluente, p. 107',
    description: ``,
    code: `
from collections import UserDict

class StrKeyDict(UserDict):
    pass
    `
  },

  { // begin new topic
    topic: 'Dictionaries',
    title: 'Update a dictionary',
    reference: '',
    description: ``,
    code: `
d = {'a': 1, 'b': 2}
w = {'z': 26}

d.update(w)  # {'z': 26, 'a': 1, 'b': 2}

u = [('c', 3), ('d', 4)]  # or tuple of tuples
d.update(u)  # {'z': 26, 'd': 4, 'a': 1, 'b': 2, 'c': 3}
    `
  },

  { // begin new topic
    topic: 'Dictionaries',
    title: 'Sort by value',
    reference: 'https://stackoverflow.com/questions/613183/how-to-sort-a-dictionary-by-value',
    description: ``,
    code: `
d = {'a': 3, 'b': 1, 'c': 2}
sorted(d, key=d.get)  # ['b', 'c', 'a']
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

data = data.concat([

////////////////////////////////////////////////////////////
//
// BITS
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Bits',
    title: 'Turning individual bits on or off',
    reference: 'https://codefights.com/interview-practice/topics/bits/tutorial',
    description: `Given an arbitrary bit sequence, turn a specific bit on or off`,
    code: `
def turn_bit_on(n, idx):
    """Turn n's bit on (set to 1) at index idx,
    where the rightmost bit is 0,
    then the second-to-last is 1"""

    # idea:
    #    0b?????
    # OR 0b00100
    #    -------
    #        x   will always equal 1

    on_seq = 1 << idx
    return n | on_seq

def turn_bit_off(n, idx):
    """Turn n's bit off (set to 0) at index idx,
    where the rightmost bit is 0,
    then the second-to-last is 1"""

    # idea:
    #     0b?????
    # AND 0b11011
    #     -------
    #         x   will always equal 0

    bit_len = n.bit_length()
    off_seq = ~(1 << idx)  # use NOT operator

    return n & off_seq    
    `
  },

  { // begin new topic
    topic: 'Bits',
    title: 'Representing numbers in binary',
    reference: '',
    description: ``,
    code: `
# decimal to binary
n = 30
s = bin(n)[2:]  # '11110'

# binary to decimal
x = int(s, 2)   # int(string, base)
testeql(n, x)
    `
  },

  { // begin new topic
    topic: 'Bits',
    title: 'Find the single number among pairs of numbers',
    reference: 'HackerRank, CodeFights',
    description: `Given an array where there is a single unique number and every other number occurs twice, find this single number.
      <br><br>
    Trick: an XOR operation will set the first number, and is reversible. When numbers overlap, the latest operation will be reversed when the number is encountered again.
      <br><br>
      Note: XOR is commutative, a ^ b == b ^ a, and associative, a ^ (b ^ c) == (a ^ b) ^ c.
    `,
    code: `
def single_integer(a):
    runningVal = 0
    for i in a:
        runningVal ^= i
    return runningVal    
    `
  },

  { // begin new topic
    topic: 'Bits',
    title: 'Invert ones and zeros',
    reference: '',
    description: ``,
    code: `
# use the NOT operator, ~ (tilde)

x = 0b10011
n = ~x
print(x | n)  # -1 (see Twos' complement)
    `
  },

  { // begin new topic
    topic: 'Bits',
    title: 'Twos\' complement',
    reference: 'https://stackoverflow.com/questions/34300336/negative-numbers-to-binary-system-with-python',
    description: `See a negative value as a series of bits without the minus sign`,
    code: `
n = -12
width = 16
bin(n + (1 << width))
`
  },

  { // begin new topic
    topic: 'Bits',
    title: 'Toggle a bit',
    reference: '',
    description: `Toggle a bit at index idx, swapping a 0 with a 1 and a 1 with a 0.`,
    code: `
def toggle_bit(n, idx):
    """Toggle bit at index idx,
    where the rightmost bit is 0,
    then the second-to-last is 1"""

    toggle_mask = 1 << idx
    return n ^ toggle_mask  # use XOR
    `
  },

  { // begin new topic
    topic: 'Bits',
    title: 'Create byte sequence from hex values',
    reference: 'Python Fluente, 133',
    description: ``,
    code: `
b = bytes.fromhex("31 4b ce a9")  # b'1K\\xce\\xa9'
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

data = data.concat([

////////////////////////////////////////////////////////////
//
// SETS
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Sets',
    title: 'Operations',
    reference: 'https://docs.python.org/3/library/stdtypes.html#set',
    description: ``,
    code: `
s = {1, 2}
t = {1, 2, 3, 4, 5}
u = {1, 2, 3, 4, 5}

n = 1

n in s      # True
n not in s  # False

s < t   # Is s a proper subset of t? True
u < t   # False, because r == t

s <= t  # Is s a subset of t? True 

s > t   # Is s a proper superset of t? False
s >= t  # Is s a superset of t? False

== # Equals 
|  # Union
&  # Intersection
-  # Difference
^  # symmetric difference, elements in either set
   # but not in both
    `
  },

  { // begin new topic
    topic: 'Sets',
    title: 'Set literal',
    reference: '',
    description: ``,
    code: `
s = {1, 2, 3}
t = {1}
empty_is_a_dict = {}
empty_set = set()
    `
  },

  { // begin new topic
    topic: 'Sets',
    title: 'frozenset can be included in other sets',
    reference: '',
    description: `Because a set can only include hashable items, a set cannot be included in another set. However, a frozenset is hashable.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Sets',
    title: 'setcomps (set comprehensions)',
    reference: 'Python Fluente, p. 113',
    description: ``,
    code: `
s = {x for x in range(10) if x % 2 == 1}  # odd numbers
    `
  },

  { // begin new topic
    topic: 'Sets',
    title: 'Apply functions to many iterables',
    reference: 'Python Fluente, p. 114',
    description: `The union of four sets, a, b, c, and d, can be computed with one function call`,
    code: `
a.union(b, c, d)    
    `
  },

  { // begin new topic
    topic: 'Sets',
    title: 'Elementwise modifications',
    reference: 'Python Fluente, p. 115',
    description: ``,
    code: `
s.add(e)      # add e to s
s.clear()     # remove all elements from s
s.copy()      # returns a shallow copy of s
s.pop()       # removes and returns an arbitrary element 
s.discard(e)  # removes e if it exists, otherwise does nothing
s.remove(e)   # removes e if it exists, otherwise throws KeyError
s.update(t)   # update s with the union of itself and t. t may be a list
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

  
  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },
  
]);

data = data.concat([

  { // begin new topic
    topic: 'Mathematics',
    title: 'Exponentials and logarithms',
    reference: 'Algoritmos, 41-42',
    description: ``,
    code: `
(a ** m) ** n == a ** (m * n)
(a ** m) * (a ** n) == a ** (m + n)

In Python, log(n) is the natural logarithm

a == b ** (log_b(a))
log(a * b) == log(a) + log(b)
log(a ** n) == n * log(a)
log_b(a) == log_c(a) / log_c(b)  # change of base, c can be any base
log(1 / a) == -log(a)
log_b(a) == 1 / log_a(b)
a ** (log_b(c)) == c ** (log_b(a))
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

data = data.concat([

//////////////////////////////////////////////////////////////////////
//
// DYNAMIC PROGRAMMING
//
//////////////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Dynamic Programming',
    title: 'Coin counting',
    reference: 'https://www.topcoder.com/community/data-science/data-science-tutorials/dynamic-programming-from-novice-to-advanced/',
    description: `Given a list of N coins valued (V1, V2, V3, ...) and a total sum S, find the minimum number of coins to total S (we can use as many coins of one type as we want), or report that it is not possible to get to sum S`,
    code: `
 def minCoins(coins, s):
    dp = [float('inf')] * (s+1)
    dp[0] = 0

    for i in range(s+1):
        for j in range(len(coins)):
            if coins[j] <= i and dp[i-coins[j]] + 1 < dp[i]:
                dp[i] = dp[i-coins[j]] + 1
    return dp[-1]   
    `
  },

  { // begin new topic
    topic: 'Dynamic Programming',
    title: 'Top-down vs. Bottom-up',
    reference: 'Intro to Algorithms, 365',
    description: `Using a top-down approach, the procedure is written recursively in a natural matter, but also uses memoization to save the result of each subproblem.<br><br>A bottom-up approach typically depends on some natural notion of the "size" of a subproblem, such that solving a subproblem depends only on solving "smaller" subproblems. Subproblems are sorted by size and solved in order, smallest first`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Dynamic Programming',
    title: 'Memoization',
    reference: 'Python Fluente, 240',
    description: `Memoization is the process of storing previously computed results in a quickly accessible place (a dictionary). The built-in <code>@functools.lru_cache</code> (Least Recently Used Cache) is an easy way to memoize a function.<br><br>
    The signature is: <code>@functools.lru_cache(maxsize=128, typed=False)</code><br><br>
    If maxsize is None, the cache can grow without bound. If typed is True, arguments of different types will be cached separately.
    `,
    code: `
import functools

@functools.lru_cache()
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
    `
  },

  { // begin new topic
    topic: 'Dynamic Programming',
    title: 'Rod cutting',
    reference: 'Intro to Algorithms, 362',
    description: `A rod of length L is to be cut into several pieces, or left intact. Given an array of prices for pieces of increasing lengths, determine the most money that can be made from this rod.`,
    code: `
def cutRodBottomUp(prices, length):
    prices = [0] + prices
    r = [0] * (length+1)
    r[0] = 0
    for j in range(1, length+1):
        q = float('-inf')
        for i in range(1, j+1):
            q = max(q, prices[i] + r[j-i])
        r[j] = q
    return r[length]
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },



  ]);

data = data.concat([

////////////////////////////////////////////////////////////
//
// BOOLEANS
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Booleans',
    title: 'all(), any()',
    reference: '',
    description: ``,
    code: `
# no need to make a list inside all or any (with [ ])

array = [1,2,3,4,5]
all(value > 2 for value in array)

any(value % 2 == 1 for value in array)
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

data = data.concat([

////////////////////////////////////////////////////////////
//
// FUNCTIONS
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Functions',
    title: 'Estimate from midpoints',
    reference: '',
    description: `Given a target, update guesses until the desired value is within a tolerance`,
    code: `
def sqrtEstimateMidpoint(x):
    left = 0
    right = x
    
    while True:
        midpoint = (right + left) / 2
        squareMidpoint = midpoint * midpoint

        if abs(squareMidpoint - x) < 1e-4:
            return midpoint
            
        if squareMidpoint > x:
            right = midpoint
        else:
            left = midpoint
    
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Recursion, basic (Fibonacci sequence)',
    reference: '',
    description: `Fibonacci sequence, not optimal but conceptually easy to understand.`,
    code: `
def fibRec(n):
    """Return the nth Fibonacci number. fib(0) = 0 and fib(1) = 1"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibRec(n-1) + fibRec(n-2)

def test():
    """0, 1, 1, 2, 3, 5, 8"""
    testeql(fibRec(6), 8)
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'First-class function, definition',
    reference: 'Python Fluente, 175',
    description: `A first-class function:
<ul>
      <li>can be created at runtime</li>
      <li>can be assigned to a variable or inside a data structure</li>
      <li>can be passed as an argument to a function</li>
      <li>can be returned as the result of a function call</li>
</ul>
    `,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'map, starmap',
    reference: 'Python Fluente, 476',
    description: `map applies the given function to each element of the given iterable. starmap(f, iter) returns an iterable that applies f(*item_iter) for each item_iter that iter produces`,
    code: `
def square(x):
    return x * x

a = [1, 2, 3, 4, 5]
list(map(square, a))  # [1, 4, 9, 16, 25]

# alternative way, with listcomp
[square(n) for n in a]

# starmap    
import itertools, operator
list(itertools.starmap(operator.mul, enumerate('abc', 1)))
# ['a', 'bb', 'ccc']
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Higher-order function, definition',
    reference: 'Python Fluente, 177',
    description: `A higher-order function is a function that accepts a function as an argument or returns a function.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'applying a function to dynamic list of arguments',
    reference: 'Python Fluente, 178',
    description: `<code>apply</code> was removed because a function can be called with starred arguments`,
    code: `
# instead of apply(fn, args, kwargs), call

fn(*args, **kwargs)
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'filter',
    reference: '',
    description: `If predicate is True, the value is kept. itertools.filterfalse keeps items for which the predicate is False`,
    code: `
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, range(10)))  # [1, 3, 5, 7, 9]

list(filter(lambda x: x > 2, range(6)))  # [3, 4, 5]
    
# alternative way, with listcomp
[n for n in range(10) if n % 2 == 1]
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'reduce',
    reference: 'Python Fluente, 179',
    description: `reduce applies the given function to items of the iterable successively, returning the accumulated result`,
    code: `
from functools import reduce
from operator import mul

reduce(mul, range(1, 7))  # 720, same as factorial(6)
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'lambda creates anonymous functions',
    reference: 'Python Fluente, 180',
    description: `Lambdas are generally used in higher-order functions. In the example, we sort by the word ending to look for rhymes`,
    code: `
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted(fruits, key=lambda word: word[::-1])
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Check if an object is callable',
    reference: 'Python Fluente, 181',
    description: ``,
    code: `
callable(2)  # False
callable(lambda x: x+1)  # True
callable(callable)  # True
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Variable number of arguments',
    reference: '',
    description: ``,
    code: `
def describe(category, *items, **properties):
    print(category)
    print(' '.join(items))
    print('\n'.join("%s : %s" % (key, val) for key, val in properties.items()))

describe("Games", 'Poker', 'Blackjack', 'Chess', owner="Joe", winner="Tim")
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'methodcaller',
    reference: 'Python Fluente, 197',
    description: ``,
    code: `
from operator import methodcaller

hyphenate = methodcaller('replace', ' ', '-')
hyphenate("something to do")  # 'something-to-do'
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'partial application',
    reference: 'Python Fluente, 198',
    description: `<code>partial</code> freezes part of the arguments passed to a function. By default, only the leftmost arguments may be frozen.<br><br>
    <code>partialmethod</code> works for methods.`,
    code: `
from unicodedata import normalize
from functools import partial

# typically, we would call normalize('NFC', s)
nfc = partial(normalize, 'NFC')
nfc('café')
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Closures',
    reference: 'Python Fluente, 232',
    description: `A closure is a function that has access to existing free variables when the function is defined, so that they may be used later when the scope of the definition is no longer available`,
    code: `
# calculate the average of a series of values
def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)  # here, series is a free variable
        total = sum(series)
        return total / len(series)

    return averager

# inefficient because the sum is repeatedly computed
    
# nonlocal is not needed because we were not assigning to series,
# only calling append (lists are mutable)

# a better solution uses 'count' and 'total',
# with nonlocal in averager

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Single-dispatch',
    reference: '',
    description: `Decorating a simple function with <code>@functools.singledispatch</code> makes it a generic function (a group of functions that behaves in different ways, depending on the type of the first argument) `,
    code: `
from functools import singledispatch
import numbers
import html

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return "<pre>{}</pre>".format(content)

@htmlize.register(str)  # specify the type of the argument
def _(text):  # the name of a specific function is irrelevant; use _
    content = html.escape(text).replace('\n', '<br>\n')
    return "<p>{}</p>".format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return "<pre>{0} (0x{0:x})</pre>".format(n)
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'A function may alter mutable arguments',
    reference: 'Python Fluente, 269',
    description: ``,
    code: `
def f(a, b):
    a += b
    return a

x = 1
y = 2
f(x, y)  # 3, but x is not altered

a = [1, 2]
b = [3, 4]
f(a, b)  # a becomes [1, 2, 3, 4]

t = (10, 20)
u = (30, 40)
f(t, u)  # (10, 20, 30, 40), but t is not altered
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Avoid mutable parameters as default values',
    reference: 'Python Fluente, 270',
    description: `The default value is evaluated when the function is defined, so when the mutable object is changed, this change will affect all future calls to that function. The solution is to use None as the default value, and make a copy of the argument passed.`,
    code: `
class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Rich comparisons, autocompleting',
    reference: 'https://docs.python.org/3/library/functools.html',
    description: `The decorator <code>@functools.total_ordering</code> supplies the class' remaining rich comparison ordering methods when one or more are of them defined.`,
    code: `
@total_ordering
class Student:
    def _is_valid_operand(self, other):
        return (hasattr(other, "lastname") and
                hasattr(other, "firstname"))
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))    
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Newton\'s method to approximate an equation\'s solution',
    reference: 'SICP PDF, 108',
    description: `If x->g(x) is a differentiable function, then a solution of the equation g(x) = 0 is a fixed point of the function x->f(x), where f(x) = x - (g(x) / Dg(x)), where Dg(x) is the derivative of g evaluated at x.<br><br>A number x is a fixed point of a function f if f(x) = x. For some functions, repeatedly applying f(x), f(f(x)), f(f(f(x)))... can be done to find x.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Fixed point, finding',
    reference: 'SICP, 103',
    description: `Find x such that f(x) = x`,
    code: `
def fixedPoint(f, x):
    prev = x
    trial = f(x)
    while abs(trial - prev) > 0.0001:
        prev = trial
        trial = f(trial)
    return trial

def fixedSqrt(x):
    return fixedPoint(lambda y: 0.5 * (x/y + y), x)

fixedSqrt(2)  # 1.414213562...
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },

]);

data = data.concat([

  { // begin new topic
    topic: 'Metaprogramming',
    title: 'Dynamic attributes',
    reference: 'Python Fluente, 644',
    description: `The special methods __getattr__ and __setattr__ are called to evaluate access to attributes.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Metaprogramming',
    title: 'Descriptors',
    reference: 'https://docs.python.org/3/howto/descriptor.html , Python Fluente, 687',
    description: `A descriptor is an object attribute with binding behavior, whose attribute access has been overridden by methods in the descriptor protocol. These methods are __get__, __set__, and __delete__`,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },


]);

data = data.concat([

////////////////////////////////////////////////////////////
//
// LISTS
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Lists',
    title: '1D Initialization',
    reference: '',
    description: ``,
    code: `
size = 5

arr = [0] * size
    
# Do not use this pattern with reference values,
# such as arr = [another_arr] * 9
# Changes to one part will also occur in any other
# corresponding places.
    `
  },

  { // begin new topic
    topic: 'Lists',
    title: '2D Initialization',
    reference: '',
    description: ``,
    code: `
# arr_2d[row][col]
rows = 3
cols = 5

arr_2d = [[0 for _ in range(cols)] for _ in range(rows)]
    `
  },
  
  { // begin new topic
    topic: 'Lists',
    title: '3D Initialization',
    reference: '',
    description: ``,
    code: `
# arr_3d[layer][row][col]
layers = 2
rows = 3
cols = 4

arr_3d = [[[0 for _ in range(cols)] for _ in range(rows)] for _ in range(layers)]
    `
  },

  { // begin new topic
    topic: 'Lists',
    title: 'Slicing',
    reference: '',
    description: ``,
    code: `
a = [1, 2, 3]
r = list(range(2, 11))  # ranges do not include endpoint; ends at 10

# r[20] raises IndexError
r[::-1]    # reverse
r[1:20:2]  # step of 2, out of bounds endpoint does not raise Error
    `
  },

  { // begin new topic
    topic: 'Lists',
    title: 'Zip two lists together',
    reference: '',
    description: `Zip ends with shortest list, use zip_longest to fill in blanks`,
    code: `
names = ['Joe', 'Alice', 'Ken', 'Tim', 'Sarah']
scores = [68, 72, 99, 74, 75]

# a student passes with a score of 75 or higher
[(name, score >= 75) for (name, score) in zip(names, scores)]

from itertools import zip_longest

trees = ['elm', 'ash', 'fir']
heights = [78, 62]

print(list(zip_longest(trees, heights, fillvalue=0)))
    `
  },

  { // begin new topic
    topic: 'Lists',
    title: 'Transpose a 2D list',
    reference: '',
    description: `Use list() on zip(), if needed`,
    code: `
# if the list is perfectly rectangular
arr_tr = zip(*arr)

# otherwise, to fill in spaces
from itertools import zip_longest

arr_tr = zip_longest(*arr, fillvalue=0)  # or ' ', etc.
    `
  },


  { // begin new topic
    topic: 'Lists',
    title: 'Shallow copy',
    reference: 'Python Fluente, 264',
    description: `A shallow copy duplicates the references found in the outermost collection.`,
    code: `
a = [3, [5, 4], (7, 8, 9)]
b = list(a)  # shallow copy
c = a[:]  # also a shallow copy

import copy
d = copy.copy(a)  # another way of making a shallow copy
    `
  },

  { // begin new topic
    topic: 'Lists',
    title: 'Deep copy',
    reference: 'Python Fluente, 267',
    description: ``,
    code: `
import copy

a = [2, 3]
b = [1, a, (4, 5)]
c = copy.deepcopy(b)
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },


]);

data = data.concat([

  { // begin new topic
    topic: 'Geometry',
    title: 'Law of cosines',
    reference: 'https://en.wikipedia.org/wiki/Law_of_cosines',
    description: `The law of cosines relates the lengths of a triangle's sides to the cosine of one of its angles.`,
    code: `
from math import cos, sqrt

def sideLen(a, b, angleC):
    return sqrt(a**2 + b**2 - 2*a*b*cos(angleC))
    `
  },

  { // begin new topic
    topic: 'Geometry',
    title: 'Radians to degrees',
    reference: '',
    description: ``,
    code: `
from math import pi
    
def radToDeg(r):
    return r / pi * 180
    `
  },

  { // begin new topic
    topic: 'Geometry',
    title: 'Degrees to radians',
    reference: '',
    description: ``,
    code: `
from math import pi
    
def degToRad(d):
    return d / 180 * pi
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

data = data.concat([

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },
  
]);

data = data.concat([

  { // begin new topic
    topic: 'Concurrency',
    title: 'Concurrency and parallelism',
    reference: 'Python Fluente, 594',
    description: `Concurrency is about structure, and parallelism is about execution. Concurrency produces a way to structure a solution to a problem that may be (but not necessarily) parallelizable.`,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },


]);

data = data.concat([

////////////////////////////////////////////////////////////
//
// STACKS
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Stacks',
    title: 'Lists behave like LIFO stacks',
    reference: 'https://docs.python.org/3/tutorial/datastructures.html',
    description: `Add to a stack with <code>append()</code> and remove with <code>pop()</code>`,
    code: `
stack = [3, 4]
stack.append(5)  # [3, 4, 5]
stack.pop()  # 5
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

data = data.concat([

  { // begin new topic
    topic: 'Datetime',
    title: 'now',
    reference: '',
    description: `Note: date does not have now()`,
    code: `
from datetime import datetime

now = datetime.now()
# datetime.datetime(2017, 10, 30, 19, 50, 29, 702774)
    `
  },

  { // begin new topic
    topic: 'Datetime',
    title: 'Format date with strftime',
    reference: '',
    description: `The mnemonic for strftime and strptime is that 'f' stands for format, and 'p' stands for parse`,
    code: `
from datetime import date, datetime
dt = datetime(2017, 10, 15, 23, 22)
d = date(2017, 2, 15)

print(dt.strftime("%H:%M %d/%m/%y"))  # 23:22 15/10/17
print(d.strftime("%d/%m/%y"))  # 15/02/17
    `
  },

  { // begin new topic
    topic: 'Datetime',
    title: 'Parse date with strptime',
    reference: '',
    description: `The mnemonic for strftime and strptime is that 'f' stands for format, and 'p' stands for parse. strptime is a class method of datetime.datetime.`,
    code: `
from datetime import datetime
d = datetime.strptime("02/15/97", "%m/%d/%y")
# datetime.datetime(1997, 2, 15, 0, 0) 
    `
  },

  { // begin new topic
    topic: 'Datetime',
    title: 'Weekdays',
    reference: '',
    description: `weekday() may be called by both a date and a datetime.<br><br>0 = Mon, 1 = Tue, 2 = Wed, 3 = Thu, 4 = Fri, 5 = Sat, 6 = Sun`,
    code: `
    
    `
  },

]);

data = data.concat([

////////////////////////////////////////////////////////////
//
// NUMBER MANIPULATION
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Number Manipulation',
    title: 'Convert decimal to bin, oct, hex',
    reference: '',
    description: ``,
    code: `
n = 123
b = bin(n)[2:]  # discard initial 0b
o = oct(n)[2:]
h = hex(n)[2:]
    `
  },

  { // begin new topic
    topic: 'Number Manipulation',
    title: 'Convert arbitrary base to decimal',
    reference: '',
    description: ``,
    code: `
n = '3eg'  # some number in base 19
d = int(n, 19)  # 1365 in decimal

# If coding literally, write:
h = 0xfe
o = 0o755
b = 0b1101
    `
  },

  { // begin new topic
    topic: 'Number Manipulation',
    title: 'Process integer\'s digits right-to-left',
    reference: 'CodeFights Tourneys',
    description: `Given a decimal integer, do something digit-by-digit, starting from ones (right side)`,
    code: `
n = 12345
while n > 0:
    digit = n % 10
    print(digit)
    n //= 10
    `
  },

  { // begin new topic
    topic: 'Number Manipulation',
    title: 'Convert integer to list of digits',
    reference: '',
    description: ``,
    code: `
n = 12345
digits = list(map(int, str(n)))
    `
  },

  { // begin new topic
    topic: 'Number Manipulation',
    title: 'Change a decimal integer to arbitrary base',
    reference: 'Rosen p. 249',
    description: `Valid for 2 <= base <= 9`,
    code: `
def changeBase(n, base):
    digits = []

    while n > 0:
        digits.append(n % base)
        n //= base
    return ''.join(map(str, digits))[::-1]
    `
  },

  { // begin new topic
    topic: 'Number Manipulation',
    title: 'Convert list of ints to string',
    reference: '',
    description: ``,
    code: `
a = [1, 2, 3]
''.join(map(str, a))
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },


]);

data = data.concat([

////////////////////////////////////////////////////////////
//
// GRAPHS
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Graphs',
    title: 'Detect a cycle in an undirected graph',
    reference: 'https://algocoding.wordpress.com/2015/04/02/detecting-cycles-in-an-undirected-graph-with-dfs-python/',
    description: ``,
    code: `
def isCyclic(m):
    visited = set()
    found = False
   
    def isCyclicStep(v, parent):
        nonlocal found
        
        if found:
            return
        visited.add(v)
        for vertex, connected in enumerate(m[v]):
            if connected and vertex in visited and vertex != parent:
                found = True
            if connected and not vertex in visited:
                isCyclicStep(vertex, v)

    for i in range(len(m)):
        if not i in visited:
            isCyclicStep(i, i)
        if found:
            break
    return found    
    `
  },

  { // begin new topic
    topic: 'Graphs',
    title: 'Representation, Adjacency List',
    reference: '',
    description: `An adjacency list may be a list of lists or a dictionary, where the source (initial) vertex is the key and sink (terminal) vertices are stored in a corresponding list.`,
    code: `
adjLists = [[1, 2], [2, 3], [4], [4, 5], [5], []]

adjListsDict = {}
adjListsDict[0] = [1, 2]
adjListsDict[1] = [3]
    `
  },

  { // begin new topic
    topic: 'Graphs',
    title: 'Representation, Adjacency Matrix',
    reference: '',
    description: `The adjacency matrix is an n x n matrix with True or False values, where True represents an edge between the row-numbered vertex and the column-numbered vertex. An undirected graph is symmetric.<br><br>In the example below, the first line is the number of vertices and each subsequent line, an edge.`,
    code: `
GRAPH = """
3
0 1
1 2
2 0
"""

def buildAdjMatrix(s):
    lines = filter(lambda line: len(line.strip()) > 0, s.split("\n"))
    nodes = int(next(lines))
    m = [[0 for _ in range(nodes)] for _ in range(nodes)]
    for edgeStr in lines:
        ends = list(map(int, edgeStr.split()))
        m[ends[0]][ends[1]] = m[ends[1]][ends[0]] = 1
    return m
    `
  },

  { // begin new topic
    topic: 'Graphs',
    title: 'BFS (Breadth-First Search)',
    reference: '',
    description: ``,
    code: `
from collections import deque
    
def bfsConnectedComponent(m, start):
    """Given an adjacency matrix and starting node, return the set
    of vertices connected to the starting node"""
    
    q = deque([start])  # queue, use append and popleft
    visited = {start}  # set
    component = []  # output
    
    while len(q) > 0:
        cur = q.popleft()
        component.append(cur)
            
        for vertex, connected in enumerate(m[cur]):
            # vertex is the column index in matrix (i)
            # connected is the True/False, 1 or 0 value
            if connected and not vertex in visited:
                q.append(vertex)
                visited.add(vertex)        
    return component    
    `
  },

  { // begin new topic
    topic: 'Graphs',
    title: 'DFS (Depth-First Search), iterative',
    reference: 'https://www.hackerearth.com/pt-br/practice/algorithms/graphs/depth-first-search/tutorial/',
    description: `The difference between DFS and BFS is that DFS uses a stack (vertices encountered last are processed first), while BFS uses a queue (vertices encountered first as immediate neighbors are processed first)`,
    code: `
def dfsIterative(m, start):
    """Given an adjacency matrix and starting node,
    traverse the graph"""
    
    s = [start]  # list, use as stack
    visited = {start}  # set
    out = []
    
    while len(s) > 0:
        cur = s.pop()
        out.append(cur)
            
        for vertex, connected in enumerate(m[cur]):
            # vertex is column in matrix (i)
            # connected is the True/False, 1 or 0 value
            if connected and not vertex in visited:
                s.append(vertex)
                visited.add(vertex)
    return out    
    `
  },

  { // begin new topic
    topic: 'Graphs',
    title: 'DFS (Depth-First Search), recursive',
    reference: 'https://www.hackerearth.com/pt-br/practice/algorithms/graphs/depth-first-search/tutorial/',
    description: ``,
    code: `
def dfsRecursive(m, start):
    visited = set()
    out = []
    def dfsRecursiveStep(start):
        visited.add(start)
        out.append(start)
        for vertex, connected in enumerate(m[start]):
            # vertex is column in matrix (i)
            # connected is the True/False, 1 or 0 value
            if connected and not vertex in visited:
                dfsRecursiveStep(vertex)
    dfsRecursiveStep(start)
    return out

    `
  },


]);

data = data.concat([

////////////////////////////////////////////////////////////
//
// TESTING
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Testing',
    title: 'assert (simple testing)',
    reference: '',
    description: ``,
    code: `
def f(x):
    return x + 1

def test():
    """
    Message string after assertion is optional, will appear on failure.
    Display "OK" at the end to indicate success.
    Call test() in interactive session.
    """
    assert f(99) == 100, "f of 99"
    assert f(f(9)) == 11, "Chain of f"
    assert f(f(0)) == 2
    print("OK")
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

data = data.concat([

////////////////////////////////////////////////////////////
//
// Iteration, Iterators, Generators
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Iteration',
    title: 'Fibonacci sequence',
    reference: '',
    description: ``,
    code: `
def fib_iter(n):
    """Iterative version of Fibonacci sequence"""
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def test():
    """[0, 1, 1, 2, 3, 5, 8]"""
    testeql(fib_iter(0), 0)
    testeql(fib_iter(1), 1)
    testeql(fib_iter(3), 2)
    testeql(fib_iter(6), 8)
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'Why sequences are iterable',
    reference: 'Python Fluente, 453',
    description: `To iterate over an object x, <code>iter(x)</code> is called. This call checks if <code>__iter__</code> is implemented. If not, __getitem__ is called, starting with the index 0. If neither methods are implemented, TypeError is raised.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'Iterable, definition',
    reference: 'Python Fluente, 455, 461',
    description: `An iterable is any object from which the built-in function iter can obtain an iterator. Sequences are always iterable. While iterators are iterable, iterables are not iterators. Do not define __next__ and __iter__ in the same class, making it an iterable and iterator at the same time. One should be able to instantiate multiple, independent iterators from the same object.`,
    code: `
class C:
    def __init__(self):
        self.items = ['a','b']
    def __getitem__(self, index):
        return self.items[index]

c = C()
i = iter(c)
next(i)  # 'a'
next(i)  # 'b'
next(i)  # StopIteration
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'Iterator, definition',
    reference: 'Python Fluente, 458',
    description: `An iterator is any object that implements __next__, returning the next item in the sequence, and raises StopIteration when there are no more items. Iterators also implement __iter__, making them iterable. An iterator cannot be rewound; a new one (with initial state) must be created. The __iter__ method in an iterator may be: return self`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'Generator as __iter__',
    reference: 'Python Fluente, 462',
    description: `Any function that has <code>yield</code> is a generator. yield may be used more than once in a generator definition.`,
    code: `
import re

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = re.findall(r'\\w+', text)
        
    def __iter__(self):
        for word in self.words:
            yield word
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'genexps (generator expressions)',
    reference: 'Python Fluente, 470',
    description: ``,
    code: `
import re

class Sentence:
    def __init__(self, text):
        self.text = text
    def __iter__(self):
        return (match.group() for match in re.finditer(r'\\w+', self.text))

s = Sentence("a man a plan a canal panama")
i = iter(s)
list(s)
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'count produces numbers by steps',
    reference: 'Python Fluente, 473',
    description: `itertools.count returns a generator. Does not end.`,
    code: `
gen = count(1, 0.5)
next(gen)  # 1
next(gen)  # 1.5    
next(gen)  # 2.0
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'takewhile predicate is True',
    reference: 'Python Fluente, 473',
    description: `An itertools generator that consumes another generator and stops when the given predicate is False`,
    code: `
gen = takewhile(lambda n: n < 3, count(1, 0.5))
list(gen)  # [1, 1.5, 2.0, 2.5]
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'compress keeps values for corresponding True values',
    reference: 'Python Fluente, 475',
    description: `itertools.compress consumes two iterables in parallel, returning the values of the first argument for which corresponding values of the second argument are True. The returned object is an iterator. 1 and 0 may be used instead of True and False`,
    code: `
a = compress([1,2,3,4,5], [True, False, False, True, True])
list(a)  # [1, 4, 5]
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'dropwhile predicate is True',
    reference: 'Python Fluente, 475',
    description: `itertools.dropwhile evaluates the predicate for items in the second argument. Once it is False, the remaining items are returned, and no more items are checked by the predicate.`,
    code: `
d = dropwhile(lambda n: n < 3, count(1, 0.5))
next(d)  # 3.0
next(d)  # 3.5
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'islice for iterables',
    reference: 'Python Fluente, 475',
    description: `itertools.islice(it, stop) and islice(it, start, stop, step=1) works for any iterable and is lazy`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'enumerate() pairs an index with the corresponding element',
    reference: 'Python Fluente, 476',
    description: `enumerate(iter, start=0)`,
    code: `
squares = [0, 1, 4, 9, 16, 25, 36, 49]

for (i, sq) in enumerate(squares):
    if sq % 2 == 1:  # if square is odd
        print("The square of", i, "is odd")
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'accumulate builds up partial results',
    reference: 'Python Fluente, 476',
    description: `itertools.accumulate produces accumulated sums. If a function of two arguments is given, it is applied to the first and second items, then to this result and the third item, and so on.`,
    code: `
a = [1, 2, 3, 4, 0, 6]
list(accumulate(a, lambda a, b: a * b))
# [1, 2, 6, 24, 0, 0]
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'chain joins given iterables',
    reference: 'Python Fluente, 478',
    description: `itertools.chain joins its arguments in order. chain.from_iterable(iter) joins the iterables within the given iterable.`,
    code: `
list(chain('ABC', range(1, 4)))
# ['A', 'B', 'C', 1, 2, 3]

list(chain(enumerate("ABC")))
# [(0, 'A'), (1, 'B'), (2, 'C')]
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'cycle repeatedly',
    reference: 'Python Fluente, 480',
    description: `itertools.cycle(iter) saves a copy of each item in iter and repeatedly produces them without end.`,
    code: `
list(islice(cycle(range(1, 4)), 10))
# [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'repeat an item',
    reference: 'Python Fluente, 480',
    description: `repeat(item, times=[forever]) repeats the given item the number of times given`,
    code: `
list(repeat(9, 3))
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'reversed',
    reference: 'Python Fluente, 483',
    description: `reversed(seq) returns a reverseiterator of a sequence or object that implements __reversed__`,
    code: `
reversed([1,2,3])    
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'groupby a given key',
    reference: 'Python Fluente, 483',
    description: `itertools.groupby(iter, key=None) produces tuples in the form (key, group) where key is the grouping criterion and group is the generator producing the corresponding items. Grouped items must be placed together in given iter.`,
    code: `
animals = ['bee', 'cat', 'duck', 'dog', 'tiger', 'sheep']
animals = sorted(animals, key=len)
[(length, list(group)) for (length, group) in groupby(animals, len)]
# [(3, ['bee', 'cat', 'dog']), (4, ['duck']), (5, ['tiger', 'sheep'])]    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'tee returns n generators',
    reference: 'Python Fluente, 483',
    description: `itertools.tee(iter, n=2) returns n independent generators that produce the items in iter.`,
    code: `
g1, g2 = tee('ABC')
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'yield from',
    reference: 'https://docs.python.org/3/whatsnew/3.3.html#pep-380',
    description: `yield from allows a generator to delegate part of its operations to another generator. For simple iterators, it replaces a for loop`,
    code: `
# for simple generators, yield from iterable is equivalent to:
    
for item in iterable:
    yield item
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'iterate until a sentinel is reached',
    reference: 'Python Fluente, 488',
    description: `iter(callable, sentinel) returns an iterator that stops when the sentinel was supposed to be returned.`,
    code: `
from random import randint
    
def d6():
    return randint(1, 6)

list(iter(d6, 1))
# [6, 3, 4, 2, 3, 6] : 1 is not present
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'Coroutines',
    reference: 'Python Fluente, 515',
    description: `Syntactically, coroutines look like generators. However, in a coroutine, yield will usually appear on the right side of an assignment. Unlike generators, you can both send and receive data to a coroutine.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'Interleave two lists',
    reference: 'https://stackoverflow.com/questions/7946798/interleaving-two-lists-in-python',
    description: `Note: lists must have the same length.`,
    code: `
from itertools import chain

a = [1, 2, 3]
b = ['a', 'b', 'c']

c = chain(*zip(a, b))
list(c)  # [1, 'a', 2, 'b', 3, 'c']
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'Group sequence into subsequences',
    reference: '',
    description: ``,
    code: `
size = 3
a = 'abcdefghijklmnopqrstuvwxyz'
[a[size*i:size*(i+1)] for i in range(len(a)//size+1)]
# ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']
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

data = data.concat([

////////////////////////////////////////////////////////////
//
// TRIES
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Tries',
    title: 'Trie for words',
    reference: 'https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014',
    description: `A trie is a tree with an empty node at its root (typically). For representing words, each child node holds a letter. To identify a word as a 'search hit', we assign a value such as 5 for the node holding the last letter of the word.`,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

data = data.concat([

////////////////////////////////////////////////////////////
//
// INPUT/OUTPUT
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Input/Output',
    title: 'HackerRank Format',
    reference: 'HackerRank',
    description: `input(), map(int, array), etc.`,
    code: `
# in Python 2, raw_input() is used; it returns a string
s = input()
n = int(input())

int_list = map(int, input().split())
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

data = data.concat([

  { // begin new topic
    topic: 'Python Syntax',
    title: 'Unpacking a list',
    reference: 'Python Fluente, 54',
    description: ``,
    code: `
t = (20, 8)
divmod(*t)
    
from itertools import product
    
strs = ['abc', 'def', 'ghi']
list(product(*strs))
    `
  },

  { // begin new topic
    topic: 'Python Syntax',
    title: 'Data Structure Literals',
    reference: '',
    description: ``,
    code: `
a_list = [1, 2, 3]
a_set = {1, 2, 2, 3}  # set() is an empty set
a_dict = {'a': 1, 'b': 2}  # {} is an empty dict

type(a_list)  # get type
    `
  },

  { // begin new topic
    topic: 'Python Syntax',
    title: 'Assign by capturing a group of items',
    reference: '',
    description: ``,
    code: `
a, b, *rest = range(5)
# 0, 1, [2, 3, 4]

a, *middle, end = range(5)
# 0, [1, 2, 3], 4    
    `
  },

  { // begin new topic
    topic: 'Python Syntax',
    title: 'Scope of variables, global',
    reference: 'Python Fluente, 230',
    description: ``,
    code: `
b = 6
    
def f(a):
    global b  # refer to global variable outside this function
    print(a)
    print(b)
    b = 9

f(3)  # 3 ; 6
b     # 9
    `
  },

  { // begin new topic
    topic: 'Python Syntax',
    title: 'Scope of variables, nonlocal',
    reference: 'https://www.smallsurething.com/a-quick-guide-to-nonlocal-in-python-3/',
    description: `nonlocal allows you to assign to variables in an outer, but not global, scope`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Python Syntax',
    title: 'Variable typing',
    reference: 'Python Fluente, 391',
    description: `Python is strongly typed and dynamically typed. In a weakly typed language, variables may be implicitly converted to a diffent type (PHP, JavaScript). In a statically typed language, type checking is done at compile time.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Python Syntax',
    title: 'else with control structures',
    reference: '',
    description: `An else block after a for or while loop will be executed if the loop exits normally (that is, was not interrupted by a break). After a try block, else will be executed if no exception was raised. A better keyword would be 'then'.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Python Syntax',
    title: 'Context managers',
    reference: 'Python Fluente, 507',
    description: `The contextlib module contains several utilities. Some of them are: closing (for objects that implement close()), suppress (ignore specific exceptions), @contextmanager (create a context manager from a simple generator), ContextDecorator (a base class for context managers), and ExitStack (exit multiple context managers).`,
    code: `
    
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

data = data.concat([

  { // begin new topic
    topic: 'Matrices',
    title: 'Transpose a matrix',
    reference: 'Codefights forum',
    description: ``,
    code: `
a = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
tr = zip(*a)
    
list(tr)
# [(1,4,7,10), (2,5,8,11), (3,6,9,12)]
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

data = data.concat([

////////////////////////////////////////////////////////////
//
// TOPIC NAME
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Decorators',
    title: 'Decorators, definition',
    reference: 'Python Fluente, 223',
    description: `A decorator is a callable that accepts another function as an argument (the decorated function). <br><br>
      A decorator can do some processing with the decorated function and return it or substitute it with another function. <br><br>
      Decorators are executed immediately after the decorated function is defined (typically when the module is imported, called import time)`,
    code: `
@deco
def target():
    print("Running target()")

# is the same as

def target():
    print("Running target()")

target = deco(target)
    `
  },

  { // begin new topic
    topic: 'Decorators',
    title: 'Substituting the decorated function',
    reference: 'Python Fluente, 223',
    description: ``,
    code: `
def deco(func):
    def inner():
        print("Running inner()")
    return inner

@deco
def target():
    print("Running target()")

target()  # Running inner()
    `
  },

  { // begin new topic
    topic: 'Decorators',
    title: 'Register functions in a registry',
    reference: 'Python Fluente, 224',
    description: ``,
    code: `
registry = []
def register(func):
    print("Running register(%s)" % func)
    registry.append(func)
    return func

@register
def f1():
    print("Running f1()");

@register
def f2():
    print("Running f2()");
    `
  },

  { // begin new topic
    topic: 'Decorators',
    title: 'Copy attributes of decorated function to decorator',
    reference: 'Python Fluente, 239',
    description: `To avoid __name__ and __doc__ being masked by a decorator, use <code>@functools.wraps</code>`,
    code: `
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        # code omitted
    `
  },

  { // begin new topic
    topic: 'Decorators',
    title: 'Stacking decorators',
    reference: 'Python Fluente, 246',
    description: `Nesting decorators work inside out`,
    code: `
@d1
@d2
def f():
    return "f"

# is the same as

f = d1(d2(f))
    `
  },

  { // begin new topic
    topic: 'Decorators',
    title: 'Decorators with arguments',
    reference: 'Python Fluente, 247',
    description: `To have a decorator that accepts arguments, we must create a decorator factory that accepts arguments and returns a decorator.`,
    code: `
registry = set()

def register(active=True):
    def decorate(func):
        print('running register(active=%s) -> decorate(%s)'
              % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate

@register(active=False)  # same as register(active=False)(f1)
def f1():
    print('running f1()')
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

data = data.concat([

////////////////////////////////////////////////////////////
//
// ARRAYS
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Arrays',
    title: 'Type codes',
    reference: '',
    description: ``,
    code: `
from array import array

my_array = array('?')

# replace ? with a type code:
    
b signed 1-byte integer
B unsigned 1-byte integer
u Unicode character
l signed 4-byte integer
L unsigned 4-byte integer
f floating point (4 bytes)
d floating point (8 bytes)
    `
  },

  { // begin new topic
    topic: 'Arrays',
    title: 'Keep array sorted with insort',
    reference: '',
    description: ``,
    code: `
from array import array    
from bisect import insort

a = array('l', sorted([3,2,9,5,10,-1]))
insort(a, 7) 
a  # array('l', [-1, 2, 3, 5, 7, 9, 10])
    `
  },

  { // begin new topic
    topic: 'Arrays',
    title: 'array, definition',
    reference: 'https://docs.python.org/3/library/array.html',
    description: `A Python array is an object type which can compactly represent an array of basic values: characters, integers, and floats, Though they behave mostly like lists, they can only store the type declared.`,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

data = data.concat([

////////////////////////////////////////////////////////////
//
// TREES
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Trees',
    title: 'Binary Tree traversal',
    reference: 'Foundations of CS',
    description: `A binary tree consists of a record with a left and right branch, and may be traversed recursively. Starting on the root node, draw a curve counterclockwise (moving to the left at first). In preorder traversal, we print the node as the curve touches its left edge. For postorder, we use each node's right edge. For inorder, we use each node's bottom edge.`,
    code: `
class Tree:  # a single node is a tree
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def preorder(self):
        print(self.value, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value, end=" ")

    def inorder(self):
        if self.left:
            self.left.inorder()

        print(self.value, end=" ")
        
        if self.right:
            self.right.inorder()
    
    `
  },

  { // begin new topic
    topic: 'Trees',
    title: 'Red-Black Tree',
    reference: '',
    description: `A red-black tree is a self-balancing binary search tree. The color property of each node is used to balance the tree upon insertions or deletions. Rebalancing involves recoloring and rotating the tree.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Trees',
    title: 'BFS (Breadth-First Search)',
    reference: '',
    description: `See Graphs: BFS`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Trees',
    title: 'DFS (Depth-First Search)',
    reference: '',
    description: `See Graphs: DFS`,
    code: `
    
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

data = data.concat([

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

data = data.concat([
//////////////////////////////////////////////////////////////////////
//
// COMBINATORICS
//
//////////////////////////////////////////////////////////////////////

  
  { // begin new topic
    topic: 'Combinatorics',
    title: 'Permutations, generating',
    reference: 'Python Fluente, 480',
    description: `permutations(iter, n=len(iter)) produces permutations of the items in iter of length n.`,
    code: `
import itertools
list(itertools.permutations('abc', 2))
# [('a', 'b'), ('a', 'c'), ('b', 'a'), ('b', 'c'), ('c', 'a'), ('c', 'b')]
    `
  },

  { // begin new topic
    topic: 'Combinatorics',
    title: 'Combinations, generating',
    reference: 'Python Fluente, 480',
    description: `itertools.combinations(iter, n) produces subsequences of length n. combinations_with_replacements allows elements to be repeated as many times as possible.`,
    code: `
import itertools
list(itertools.combinations('cba',2))
# [('c', 'b'), ('c', 'a'), ('b', 'a')]

[''.join(c) for c in itertools.combinations_with_replacement('cba', 3)]
# ['ccc', 'ccb', 'cca', 'cbb', 'cba', 'caa', 'bbb', 'bba', 'baa', 'aaa']
    `
  },


  { // begin new topic
    topic: 'Combinatorics',
    title: 'Permutations, number of',
    reference: 'Discrete Math, 408',
    description: `The number of r-permutations (permutations with r elements) of a set with n elements is: n! / (n - r)!. For example, to choose 3 winners out of 100, we have 100 people for first place, 99 for second, and 98 for third = 100 * 99 * 98. (100 - 3)! = 97!, which are the values cancelled outfrom 100!`,
    code: `
# r-permutations out of a list of n elements
n! / (n - r)!
    `
  },

  { // begin new topic
    topic: 'Combinatorics',
    title: 'Combinations, number of',
    reference: 'Discrete Math, 410',
    description: `The number of r-combinations (combinations with r elements) of a set with n elements is: n! / (r! * (n - r)!)`,
    code: `
# r-combinations out of a list of n elements
n! / (r! * (n - r)!)    
    `
  },

  {
    topic: 'Combinatorics',
    title: 'Product (Cartesian) combines elements of multiple lists',
    reference: 'Python Fluente, 478',
    description: `itertools.product(it1, it2, ... itn, repeat=1) produces tuples of n elements, where n are the number of given iterables. repeat indicates how many times the given iterables are repeated.`,
    code: `
import itertools

[''.join(p) for p in itertools.product("AB", "CD", "EF")]
# ['ACE', 'ACF', 'ADE', 'ADF', 'BCE', 'BCF', 'BDE', 'BDF']

[''.join(p) for p in itertools.product("AB", repeat=3)]
# ['AAA', 'AAB', 'ABA', 'ABB', 'BAA', 'BAB', 'BBA', 'BBB']
    `
  },

  { // begin new topic
    topic: 'Combinatorics',
    title: 'Permutations, iterative method',
    reference: '',
    description: `An iterative method to produce permutations of length n from a sequence a. The idea is to branch out at each step with all possible single items left from the remaining items, accumulating to each result.`,
    code: `
def permutation_branch(pair):
    """Given (base, rest), take each item in rest and append to base)"""
    out = []
    base, rest = pair
    for i, n in enumerate(rest):
        out.append((base + [n], rest[:i] + rest[i+1:]))
    return out

def my_permutations(a, n):
    a = list(a)
    out = [([], a)]
    
    for i in range(n):
        step = []
        for pair in out:
            step.extend(permutation_branch(pair))
        out = step
    return [p for (p, rest) in out]
    `
  },

  { // begin new topic
    topic: 'Combinatorics',
    title: 'Combinations with bit strings',
    reference: '',
    description: `A combination can be thought of a mapping between a bit string and the indices of the whole collection. If an index is 1 (True), the element is in the combination; 0 (False) means it is not. We iterate through bit strings with n ones (making it have n elements).`,
    code: `
def push_rightmost_bit(bs):
    """Find next bit string with the same number of ones"""
    rightmost_10 = bs.rfind("10")
    if rightmost_10 == -1:
        return False  # cannot push any more
    # count number of ones to the right of 10
    ones_to_move = bs[rightmost_10 + 1:].count("1")
    zeros_left = len(bs) - rightmost_10 - ones_to_move - 2
    return bs[:rightmost_10] + "01" + ("1" * ones_to_move) + ("0" * zeros_left)

def bitstring_combination(a, bs):
    return [elem for (i, elem) in enumerate(a) if bs[i] == "1"]

def my_combinations(a, n):
    a = list(a)
    len_a = len(a)
    bs = ('1' * n) + ('0' * (len_a - n))
    out = []
    while bs:
        out.append(bitstring_combination(a, bs))
        bs = push_rightmost_bit(bs)
    return out
    
    `
  },


]);

data = data.concat([

////////////////////////////////////////////////////////////
//
// TOPIC NAME
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Tuples',
    title: 'ids of elements never change',
    reference: 'Python Fluente, 263',
    description: `Although tuples are considered immutable, in reality only the ids of the elements they contain never change. A tuple may contain lists, and these may be changed in-place.`,
    code: `
t1 = (1, 2, [30, 40])
t2 = (1, 2, [30, 40])

t1 == t2  # True
    
t1[-1].append(99)
t1 == t2  # False
    `
  },

  { // begin new topic
    topic: 'Tuples',
    title: 'Shortcuts for copying will return the same tuple',
    reference: 'Python Fluente, 280',
    description: `Two shortcuts for creating shallow copies of lists will not work for tuples. They will return the reference to the same tuple`,
    code: `
t = (1, 2)
t2 = tuple(t)  # t2 is t will be True
t3 = t[:]  # t3 is t will be True
    `
  },

  { // begin new topic
    topic: 'Tuples',
    title: 'namedtuple',
    reference: 'Python Fluente, p. 56',
    description: `A lightweight, dictionary-like object. Fields are accessed with dot notation.`,
    code: `
from collections import namedtuple

Card = namedtuple("CardDisplay", 'rank suit')
# alternatively namedtuple("CardDisplay", ['rank', 'suit'])

big_two = Card(2, 'Spades')
print(big_two.suit)

print(big_two._asdict())
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },


]);

data = data.concat([


//////////////////////////////////////////////////////////////////////
//
// STRINGS
//
//////////////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Strings',
    title: 'Reverse',
    reference: '',
    description: ``,
    code: `
"abc"[::-1]

s = "esrever"
r = s[::-1]
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Check if upper, lower, digit, etc.',
    reference: '',
    description: `Given a string, check if all its characters are uppercase, lowercase, digits, etc.`,
    code: `
s = "my string"
s.islower()
s.isupper()
s.isdigit()
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Convert to upper and lowercase',
    reference: '',
    description: ``,
    code: `
s = "PyThOn iZ kEwL"
s.upper()  # PYTHON IZ KEWL
s.lower()  # python iz kewl
s.swapcase()  # pYtHoN Iz KeWl
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

  { // begin new topic
    topic: 'Strings',
    title: 'Encode and decode (strings to bytes)',
    reference: 'Python Fluente, p. 131',
    description: ``,
    code: `
s = 'café'
b = s.encode('utf-8')
d = b.decode('utf-8')
`
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Case-insensitive comparisons',
    reference: 'Python Fluente, 133',
    description: `When dealing with non-ASCII characters, lower() is not reliable`,
    code: `
s = "AbCdE"
s.casefold()  # 'abcde'
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Unicode normalization',
    reference: 'Python Fluente, 150',
    description: `Normalization of Unicode strings allow for safer comparisons between them`,
    code: `
from unicodedata import normalize

s = "café"
normalize('NFC', s)  # 'café'

# NFC combines characters as much as possible
# (resulting in the shortest string)

# NFD decomposes characters into basic ones (letters and diacritics)

# NFC is recommended by the W3C

# NFKC and NFKD (the K stands for Compatibility) are stronger forms
# of normalization

# NFKC and NFKD cause loss of data (4^2 becomes 42) so must be used
# with caution
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Remove diacritics',
    reference: 'Python Fluente, 156',
    description: ``,
    code: `
import unicodedata
import string

def remove_diacritics(s):
    norm_s = unicodedata.normalize('NFD', s)
    result = ''.join(c for c in norm_s if not unicodedata.combining(c))
    return unicodedata.normalize('NFC', result)
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Generate the alphabet',
    reference: '',
    description: ``,
    code: `
alphabet = ''.join([chr(i) for i in range(ord('a'), ord('z')+1)])    
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

data = data.concat([

////////////////////////////////////////////////////////////
//
// HEAPS
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Heaps',
    title: 'Heapsort',
    reference: 'Intro to Algorithms, 151-160',
    description: ``,
    code: `
class Heap():
    def __init__(self, unsorted):
        self.a = unsorted
        self.heapSize = len(unsorted)

    # consider this structure
    #      0
    #     / \\
    #    1   2
    #   / \\ / \\
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
    `
  },

  { // begin new topic
    topic: 'Heaps',
    title: 'Heap data structure',
    reference: 'Intro to Algorithms, 152',
    description: `A heap may be stored in an array or a binary tree.`,
    code: `

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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },


]);

data = data.concat([

////////////////////////////////////////////////////////////
//
// Calculus
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Calculus',
    title: 'Integration, definite',
    reference: '',
    description: ``,
    code: `
def definite_integral(coeffs, a, b):
    """For the integral of a polynomial with given coefficients,
    where the rightmost element is a constant, second-to-last is x,
    third-to-last is x^2, etc.

    For definite_integral([1, 0, 1], 0, 2),
    the anti-derivative is (1/3)x^3 + x = [1/3, 0, 1]
    """
    anti_derivative = []  # ignore C, constant value
    len_coeffs = len(coeffs)
    for i, coeff in enumerate(coeffs):
        power = len_coeffs - i
        anti_derivative.append(1 / power * coeff)

    # compute anti_derivative with a and b
    len_anti_derivative = len(anti_derivative)
    result = 0
    for i, coeff in enumerate(anti_derivative):
        power = len_anti_derivative - i
        result += coeff * b ** power
        result -= coeff * a ** power
    return result    
    `
  },

  { // begin new topic
    topic: 'Calculus',
    title: 'Differentiation',
    reference: '',
    description: `Given an array of coefficients, where the rightmost element is a constant, second-to-last is x, third-to-last is x^2, etc. find the derivative`,
    code: `
def differentiate(coeffs):
    """Differentiate 2x^3 - 4x^2 + 10 (given as [2, -4, 0, 10]).
    The result is 6x^2 - 8x. [6, -8, 0]
    """
    len_terms = len(coeffs)
    result = []
    for i, coeff in enumerate(coeffs[:-1]):
        power = len_terms - i - 1
        result.append(power * coeff)
    return result    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },


]);

data = data.concat([

//////////////////////////////////////////////////////////////////////
//
// NUMBER THEORY
//
//////////////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Number Theory',
    title: 'Sieve of Eratosthenes',
    reference: 'CodeFights',
    description: ``,
    code: `
def primes(n):
    if n < 2:
        return []
    isPrime = [True] * (n+1)  # begin with all numbers prime
    for base in range(3, int(n ** 0.5) + 1, 2):  # potential primes
        # stop at sqrt(n) because the larger number would
        # have already been crossed out
        for multiple in range(base * 2, n+1, base):
            isPrime[multiple] = False
    primeList = [2]  # manually include the only even number
    for n in range(3, n+1, 2):  # consider all odd numbers
        if isPrime[n]:
            primeList.append(n)
    return primeList

def test():
    testeql(primes(73), [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73])    
    `
  },

  { // begin new topic
    topic: 'Number Theory',
    title: 'Compositeness Test (pseudoprimes)',
    reference: 'https://en.wikipedia.org/wiki/Fermat_primality_test',
    description: `Check if a given number is probably prime. Carmichael numbers are composite, but will fool Fermat's test (it is a flawed test).`,
    code: `
def isProbablePrime(n):
    if n == 2:
        return True
    if not n & 1:
        return False  # even numbers
    return pow(2, n-1, n) == 1    
    `
  },


  { // begin new topic
    topic: 'Number Theory',
    title: 'GCD (Euclid\'s algorithm)',
    reference: 'SICP, sec. 1.2.5, PDF p. 78',
    description: ``,
    code: `
from fractions import gcd

def sicp_gcd(a, b):
    if b == 0:
        return a
    return sicp_gcd(b, a % b)
    `
  },


  { // begin new topic
    topic: 'Number Theory',
    title: 'LCM (using GCD)',
    reference: 'https://www.programiz.com/python-programming/examples/lcm',
    description: ``,
    code: `
from fractions import gcd

def lcm(a, b):
    return (a * b) // gcd(a, b)
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

data = data.concat([

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Extend a built-in class',
    reference: 'Use a Cabeça Python',
    description: ``,
    code: `
class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        # list.__init__([])  # appears to be optional
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    def top3(self):
        return sorted(set(self))[:3]
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Instances may be callable',
    reference: 'Python Fluente, 182',
    description: `Defining __call__ inside a class definition allows instances of that class to be called.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'is compares identity and == value',
    reference: 'Python Fluente, 261',
    description: `<code>is</code> and <code>is not</code> compares the identity of objects, while == will compare their values`,
    code: `
alex_a = { 'name': 'Alex', 'born': 1990 }
alex_b = { 'name': 'Alex', 'born': 1990 }

id(alex_a)  # 17510012
id(alex_b)  # 17510274
    
alex_a == alex_b  # True
alex_a is alex_b  # False
    
alex_a is not alex_b  # True
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Use is to compare with None',
    reference: 'Python Fluente, 262',
    description: `Instead of using ==, use <code>is</code> and <code>is not</code> to check if a variable is or is not None`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Weakrefs',
    reference: 'Python Fluente, 276',
    description: `A weak reference does not increment the reference counter, so the object it refers to may be deleted when all its strong references are gone. Weakrefs are useful for caches. Weakref collections should be used instead of <code>weakref.ref</code> directly (WeakValueDictionary, WeakKeyDictionary, and WeakSet)<br><br>

    lists, dicts, ints, and tuples cannot be the target of a weakref, but user-defined types can. While a subclass of list may be the target of a weakref, a subclass of int or tuple cannot.
    `,
    code: `
import weakref

class Cheese:
    def __init__(self, kind):
        self.kind = kind

stock = weakref.WeakValueDictionary()
catalog = [Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

del catalog
sorted(stock.keys())  # ['Parmesan']

del cheese  # the temporary variable is a strong reference 
sorted(stock.keys())  # []
    `
  },
  
  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'classmethod (decorator)',
    reference: 'Python Fluente, 293',
    description: `@classmethod defines a method that operates on the class. The class itself (as <code>cls</code>) is received as the first argument, instead of what's typically the instance. This decorator is typically used for alternative constructors`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'staticmethod (decorator)',
    reference: 'Python Fluente, 293',
    description: `@staticmethod alters a method so that it doesn't receive the special first parameter. It is like a simple function that happens to be inside a class definition.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Read-only attributes',
    reference: 'Python Fluente, 299',
    description: ``,
    code: `
class Vector2d:
    def __init__(self, x, y):
        self.__x = float(x)  # use double underscore prefix
        self.__y = float(y)

    @property
    def x(self):
        return self.__x
        
    @property
    def y(self):
        return self.__y
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Hash value',
    reference: 'Python Fluente, 300',
    description: `Use XOR (^) to combine the hashes of the object's components.`,
    code: `
# in class Vector2d, with properties x and y

def __hash__(self):
    return hash(self.x) ^ hash(self.y)
    `
  },


  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Name mangling',
    reference: 'Python Fluente, 305',
    description: `Prefixing an attribute with two underscores will cause the attribute to become _ClassName__AttrName behind the scenes.<br><br>It may be better to explicitly use _ClassName_AttrName (single underscore prefix), because a single underscore has no special meaning. However, at a module level, names with a single underscore prefix will not be imported.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: '__slots__',
    reference: 'Python Fluente, 307',
    description: `__slots__ allows you to save memory. However, they are not inherited by subclasses. To define __slots__ is to say, "These are all the instance attributes for this class." Another downside of __slots__ is that an user will not be able to add other attributes to instances. To circumvent this, add '__dict__' to the __slots__ tuple. __weakref__ may also be added.`,
    code: `
class Vector2d:
    __slots__ = ('__x', '__y')
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Protocols',
    reference: 'Python Fluente, 322',
    description: `A protocol is an informal interface. For example, the protocol of a sequence implies onlt __len__ and __getitem__. Duck typing is calling an object a sequence because it behaves like one, not specifically because it is a subclass of sequence.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Attribute access',
    reference: 'Python Fluente, 329',
    description: `Implementing __getattr__ allows you to customize the result of <code>instance.x</code><br><br>__getattr__ is only called when the attribute, x, does not exist. If x is assigned to the instance, __getattr__ will no longer be called. __setattr__ must be defined to take care of this scenario.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'super()',
    reference: 'Python Fluente, 331, 401',
    description: `<code>super()</code> allows you to access methods from superclasses.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Interface and protocol, definition',
    reference: 'Python Fluente, 354, https://stackoverflow.com/questions/372042/difference-between-abstract-class-and-interface-in-python',
    description: `An interface is a set of method definitions. It is the subset of an object's public methods that allows it to play a specific role in the system.<br><br>A protocol is an informal interface. They are independent of inheritance. Protocols cannot be verified statically by the interpreter.<br><br>An analogy in the real world is the controls of a car. The interface of a car is the steering wheel, pedals, horn, and other controls.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Polymorphism, definition',
    reference: 'https://stackoverflow.com/questions/409969/polymorphism-define-in-just-two-sentences',
    description: `A language feature that allows values of different types to be handled by a uniform interface.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Goose typing',
    reference: 'Python Fluente, 361',
    description: `Goose typing is using <code>isinstance(obj, cls)</code>, where cls is an abstract base class (ABC). In other words, cls' metaclass is abc.ABCMeta`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Virtual subclass',
    reference: 'Python Fluente, 378, 796',
    description: `A virtual subclass does not inherit from a superclass, but it is registered as <code>TheSuperClass.register(TheSubClass)</code>, or with a decorator <code>@TheSuperClass.register</code>`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'API, definition',
    reference: 'https://www.reddit.com/r/learnprogramming/comments/1xvm9l/can_some_eli5_what_an_api_is/',
    description: `An API (Application Programming Interface) is the set of functions, protocols, and tools for building software. It allows a programmer to use and access code written by the API's author.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Subclass UserCollections instead of built-ins',
    reference: 'Python Fluente, 397',
    description: `Subclassing built-ins directly is unreliable because overwritten methods are not called. Instead, subclass UserList, UserDict, and UserString from the collections module.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'MRO (Method Resolution Order)',
    reference: 'Python Fluente, 399',
    description: `The __mro__ attribute in a class is a tuple in the MRO order. To call a specific superclass method, call the class method and pass the instance as its first argument.`,
    code: `
class B():
    def pong():
        print("PONG", self)

class C():
    def pong():
        print("PONG", self)

class D(B, C):
    def ping(self):
        print("PING", self)

d = D()
C.pong(d)
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Subclasses must explicitly call super\'s __init__',
    reference: 'https://stackoverflow.com/questions/3782827/why-arent-pythons-superclass-init-methods-automatically-invoked',
    description: `There is a difference between __init__ and __new__. The superclass' __init__ must be called explicitly.`,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

data = data.concat([

//////////////////////////////////////////////////////////////////////
//
// EMACS SETUP
//
//////////////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Emacs Setup',
    title: '.emacs',
    reference: '',
    description: `Add to your .emacs file`,
    code: `
(global-set-key (kbd "<f5>") 'run-python)

(setenv "PYTHONPATH" "/home/heitor/shared/python/my-modules/")

(setenv "PYTHONSTARTUP" "/home/heitor/shared/python/my-startup.py")

(defun my-python-test-buffer ()
  (interactive)
  (save-excursion
    (python-shell-send-string (trim-string (buffer-string)))
    (python-shell-send-string (concat "print('')\\n" "test()"))))

(add-hook 'python-mode-hook
          (lambda ()
            (local-set-key [M-return] 'my-python-test-buffer)))

(add-hook 'inferior-python-mode-hook
          (lambda ()
            (auto-complete-mode 1)))
    `
  },

  { // begin new topic
    topic: 'Emacs Setup',
    title: 'Python Startup',
    reference: '',
    description: ``,
    code: `
# file: my-startup.py

from math import exp, log, sin, cos, tan, asin, acos, atan, floor, ceil
import math
import re
from mytests import testeql, pr

# add common strings to include in autocomplete

print("testeql")
    `
  },

  { // begin new topic
    topic: 'Emacs Setup',
    title: 'Python mytests',
    reference: '',
    description: ``,
    code: `
# file: mytests.py

import sys

def testequal(expression, expected):
    print("testing", expression, "expecting", expected)

    # special case: floats, check up to 6 decimal places
    if isinstance(expression, float):
        test_passed = abs(expression - expected) < 1e-6
    else:
        test_passed = expression == expected
    if test_passed:
        print("(^o^) PASS\\n")
    else:
        print("(>_<) FAIL\\n")

# alias
testeql = testequal

def pr(s):
    """pr('a b c') prints each of the names separated by a space"""
    if type(s) != str:
        raise ValueError("Argument to pr() must be a string")
    frame = sys._getframe(1)
    names = s.split()
    for name in names:
        print(name, '=', repr(eval(name, frame.f_globals, frame.f_locals)), end=", ")
    print()
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

data = data.concat([


//////////////////////////////////////////////////////////////////////
//
// REGEX
//
//////////////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Regex',
    title: 'Substitutions',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `Replace all matches with a given replacement value<br><br>

sub(replacement, originalString, count=0)
<br><br>

subn(replacement, originalString, count=0) does the same thing, but returns a tuple of the new string and the number of replacements
`,
    code: `
p = re.compile(r'(blue|white|red)')
p.sub('color', 'blue socks and red shoes')
# 'color socks and color shoes'
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Groups (parenthesized)',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `A match can be divided into groups, indicated by parentheses. Groups are numbered by counting opening parentheses from left to right.
<br><br>
matchObject.groups() returns a tuple of the strings from group 1 and up.
`,
    code: `
p = re.compile('(a(b)c)d')
m = p.match("abcd")
m.group(0)  # 'abcd'
m.group(1)  # 'abc'
m.group(2)  # 'b'
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Special sequences',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `<p>The capitalized version of a special sequence is the inverse (\\d are digits, \\D are non-digits).</p>

<p>
<code>\\d</code> is any decimal digit, [0-9]
</p>

<p>
<code>\\s</code> is any whitespace character, [ \\t\\n\\r\\f\\v]
</p>

<p>
<code>\\w</code> is any alphanumeric character, [a-zA-Z0-9_]
</p>

<p>
| 'or' operator
</p>

<p>
^ matches the beginning of lines
</p>

<p>
$ matches the end of a line
</p>

<p>
\\A matches the start of the string
</p>

<p>
\\Z matches the end of the string
</p>

<p>
\\b word boundary
</p>

`,
    code: `    
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Repetition',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `
<p>
* represents greedy repetition of the preceding character (zero or more times)
</p>

<p>
+ matches one or more times
</p>

<p>
? matches either zero or one time
</p>

<p>
{m,n} matches at least m and at most n times (endpoints are included)
</p>

<p>
To make a qualifier non-greedy, add a ? to its right, *?, +?, ??, and {m,n}?. They will match as little text as possible.
</p>
`,
    code: `
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Compiling or using module-level functions',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `Compiling a pattern will save some function calls. Flags control the behavior of the RE.
<p>
ASCII (A) \\w, \\b, \\s, \\d match only ASCII characters
</p>

<p>
DOTALL (S) . matches any character, including newlines
</p>

<p>
IGNORECASE (I) case-insensitive matches
</p>

<p>
LOCALE (L) locale-aware match
</p>

<p>
MULTILINE (M) multi-line matching, affecting ^ and $
</p>

<p>
VERBOSE (X) enable verbose REs, which may be organized more clearly
</p>

`,
    code: `
import re

pat = re.compile(r'From\s+')
pat.match('From amk')  # <_sre.SRE_Match object ...>

re.match(r'From\s+', 'From amk')  # <_sre.SRE_Match object ...>
    `
  },


  { // begin new topic
    topic: 'Regex',
    title: 'Raw string',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `A raw string is prefixed with an r. Everything is taken literally, so there is no need to escape backslashes.<br><br><code>s = r'\\\\section'</code>`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Matching',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `
<p>
match() determines if the RE matches at the beginning of the string
</p>

<p>
search() looks for a match anywhere in the string
</p>

<p>
findall() finds all substrings and returns them as a list
</p>

<p>
finditer() finds all substrings and returns them as an iterator
</p>
`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Match object',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `When a match is found, a match object is returned.`,
    code: `
pat = re.compile(r'[a-z]*')
m = pat.match("joe123")
m.group()  # "joe"
m.start(), m.end()  # (0, 3)
m.span()  # (0, 3)
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Backreferences',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `A backreference allows you to specify that the contents of an earlier capturing group must also be found at the current location. \\1 will succeed if the contents of group 1 can be found at the current position.`,
    code: `
p = re.compile(r'(\\b\\w+)\\s+\\1')
p.search("Paris in the the spring").group()  # 'the the'
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Non-capturing group',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `(?:...) where ... is a regex, denotes a part of a RE, but where we are not interested in the group's contents.
`,
    code: `
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Named groups',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `(?P&lt;name&gt;...) allows you to retrieve the group's contents by its name`,
    code: `
p = re.compile(r'(?P<word>\\b\\w+\\b)')
m = p.search('(( lots of punctuation ))')
m.group('word')  # 'lots'
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Lookahead assertions',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `
    <p>
    (?=...) is a positive lookahead assertion. It succeeds if the contained RE ... successfully matches at the current location. The matching engine does not advance. The rest of the pattern is tried where the assertion started.
    </p>

<p>
(?!...) is a negative lookahead assertion. It succeeds if the RE ... doesn't match at the current position.
</p>
    `,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Regex',
    title: 'Splitting a string',
    reference: 'https://docs.python.org/3/howto/regex.html',
    description: `split(string, maxsplit=0) will split the string where the RE was found.
`,
    code: `
p = re.compile(r'\d+')
p.split('a1b2c3')  # ['a', 'b', 'c', '']
    `
  },

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: `
`,
    code: `
    `
  },


  ]);

data = data.concat([

////////////////////////////////////////////////////////////
//
// SQL
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'SQL',
    title: 'Inner Join',
    reference: 'Learning SQL, 81',
    description: `Retrieve an employee's name and heis or her department`,
    code: `
SELECT e.fname, e.lname, d.name
FROM employee AS e INNER JOIN department AS d
ON e.dept_id = d.dept_id
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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

data = data.concat([

//////////////////////////////////////////////////////////////////////
//
// STRING FORMATTING
//
//////////////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'String Formatting',
    title: '%-formatting',
    reference: 'https://docs.python.org/3.4/library/string.html',
    description: `Using % as placeholders is called the "old %-Formatting"`,
    code: `
%s string
%d integer
%f float
    
name = "World"
print("Hello, %s" % name)
    `
  },

  { // begin new topic
    topic: 'String Formatting',
    title: 'format() function',
    reference: '',
    description: ``,
    code: `
'{1} {0}'.format('one', 'two')  # 'two one'    
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
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


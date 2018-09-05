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

lst = [0] * size
    
# Do not use this pattern with reference values,
# such as lst = [another_lst] * 9
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
# lst_2d[row][col]
rows = 3
cols = 5

lst_2d = [[0 for _ in range(cols)] for _ in range(rows)]
    `
  },
  
  { // begin new topic
    topic: 'Lists',
    title: '3D Initialization',
    reference: '',
    description: ``,
    code: `
# lst_3d[layer][row][col]
layers = 2
rows = 3
cols = 4

lst_3d = [[[0 for _ in range(cols)] for _ in range(rows)] for _ in range(layers)]
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
lst_tr = zip(*lst)

# otherwise, to fill in spaces
from itertools import zip_longest

lst_tr = zip_longest(*lst, fillvalue=0)  # or ' ', etc.
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
    topic: 'Lists',
    title: 'Flatten a list of lists',
    reference: 'https://stackoverflow.com/questions/952914/making-a-flat-list-out-of-list-of-lists-in-python',
    description: ``,
    code: `
from itertools import chain
list(chain(*[[1, 2], [3], [4, 5, 6]]))  # use an asterisk

sum([[1, 2], [3], [4, 5]], [])
sum(zip([1, 2, 3], [4, 5, 6]), ())  # (1, 4, 2, 5, 3, 6)
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

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

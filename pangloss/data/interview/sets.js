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

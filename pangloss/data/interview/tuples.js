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

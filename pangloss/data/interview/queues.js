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

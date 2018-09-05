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

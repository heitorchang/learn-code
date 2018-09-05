data = data.concat([

//////////////////////////////////////////////////////////////////////
//
// COLLECTIONS (MODULE)
//
//////////////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'collections (module)',
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
    topic: 'collections (module)',
    title: 'namedtuple',
    reference: 'Python Fluente, p. 56',
    description: ``,
    code: `
from collections import namedtuple

Card = namedtuple("CardDisplay", 'rank suit')
# alternately namedtuple("CardDisplay", ['rank', 'suit'])

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

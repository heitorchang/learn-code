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

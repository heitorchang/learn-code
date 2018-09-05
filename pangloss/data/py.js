// Use text-mode

var data = [
/*
  {
    topic: 'TOPIC',
    title: 'CARD TITLE',
    reference: 'REFERENCE SOURCE',
    description: 'DESCRIPTION',
    code: `
CODE
CODE    
    `
  },
*/

  { // begin new topic
    topic: 'Types',
    title: 'Built-in core data types',
    reference: 'LearningPython5thEd. p. 96',
    description: `The primary object types are:<br><br>

    Numbers<br>Strings<br>Lists<br>Dictionaries<br>Tuples<br>Files<br>Sets<br>Booleans<br>Types<br>Functions<br>Modules<br>Classes<br>None`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Numbers',
    title: 'Random numbers',
    reference: 'LearningPython5thEd p. 98',
    description: ``,
    code: `
    import random
    
    random.random()  # float between 0 and 1, including 0, excluding 1
    random.choice([1, 2, 3])
    random.randint(a, b)  # range [a, b], including both end points
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Negative index',
    reference: 'LearningPython5thEd p. 99',
    description: `A negative index works backwards from the end`,
    code: `
    s = 'spam'
    s[-1]  # 'm'
    s[-2]  # 'a', second-to-last item
    `
  },

  { // begin new topic
    topic: 'Sequences',
    title: 'Copy (top-level)',
    reference: 'LearningPython5thEd p. 100',
    description: `A slice from end to end creates a top-level copy`,
    code: `
    s[:]
    `
  },

  { // begin new topic
    topic: 'Types',
    title: 'Immutability',
    reference: 'LearningPython5thEd p.101',
    description: `Out of the core types, <code>numbers, strings</code> and <code>tuples</code> are immutable.

    <code>Lists, dictionaries, sets</code> and <code>class instances</code> are mutable (they can be changed in place freely`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Changing in place by expanding',
    reference: 'LearningPython5thEd p. 102',
    description: `By converting a string to a list and back, elements of a string may be changed.`,
    code: `
    s = 'shrubbery'
    lst = list(s)
    lst[1] = 'c'
    ''.join(lst)  # 'scrubbery'
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Find and replace',
    reference: 'LearningPython5thEd p. 102',
    description: `Find and replace are methods of strings`,
    code: `
    s = 'spam'
    s.find('pa')  # 1
    s.replace('pa', 'xyz')  # 'sxyzm'
    s  # 'spam' (strings are immutable, replace returns a new string)
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Split',
    reference: 'LearningPython5thEd p. 103',
    description: ``,
    code: `
    line = 'aaa,bbb,ccc,dd'
    line.split(',')  # ['aaa', 'bbb', 'ccc', 'dd']
    `
  },

  { // begin new topic
    topic: 'Strings',
    title: 'Strip whitespace',
    reference: 'LearningPython5thEd p. 103',
    description: ``,
    code: `
    s = '  a,b,c\n'
    s.strip()   # remove whitespace from both ends
    s.lstrip()  # remove from left end
    s.rstrip()  # remove from right end
    `
  },

  { // begin new topic
    topic: 'Help',
    title: 'List of object attributes',
    reference: 'LearningPython5thEd p. 104',
    description: ``,
    code: `
    s = 'spam'
    dir(s)
    `
  },

  { // begin new topic
    topic: 'Help',
    title: 'Getting help',
    reference: 'LearningPython5thEd p. 104',
    description: `Retrieve documentation for an object, data type or method`,
    code: `
    s = 'spam'
    help(s.replace)
    help(0)
    `
  },

  { // begin new topic
    topic: 'Lists',
    title: 'Growing and shrinking',
    reference: 'LearningPython5thEd p. 109',
    description: ``,
    code: `
    lst = [123, 'spam', 1.23]
    lst.append('ni')
    lst  # [123, 'spam', 1.23, 'ni'] lst is modified

    lst.pop(2)  # 1.23 (remove item at given index and return it)
    lst  # [123, 'spam', 'ni']
    `
  },

  { // begin new topic
    topic: 'Lists',
    title: 'Sorting',
    reference: 'LearningPython5thEd p. 110',
    description: `Changes list in place`,
    code: `
    m = ['bb' ,'aa', 'cc']
    m.sort()
    m  # ['aa', 'bb', 'cc']
    `
  },

  { // begin new topic
    topic: 'Lists',
    title: 'Comprehensions',
    reference: 'LearningPython5thEd p. 111',
    description: `A comprehension is a way of processing structures.`,
    code: `
    m = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
    ]

    [row[1] + 10 for row in m if row[1] % 2 == 0]
    # [12, 18]
    `
  },

  { // begin new topic
    topic: 'Generators',
    title: 'Summing a matrix\'s rows',
    reference: 'LearningPython5thEd p. 112',
    description: `Generators produce results on demand`,
    code: `
    m = [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 9],
    ]

    g = (sum(row) for row in m)
    next(g)  # 6
    next(g)  # 15
    `
  },

  { // begin new topic
    topic: 'Comprehensions',
    title: 'Building core types',
    reference: 'LearningPython5thEd p. 113',
    description: `Comprehensions can build lists, dictionaries, sets, and generators`,
    code: `
    [ord(x) for x in 'spaam']  # list
    {ord(x) for x in 'spaam'}  # set
    {x: ord(x) for x in 'spaam'}  # dictionary, keys are unique
    (ord(x) for x in 'spaam')  # generator
    `
  },

  { // begin new topic
    topic: 'Dictionaries',
    title: 'Literals',
    reference: 'LearningPython5thEd p. 114',
    description: `Dictionaries are indexed by key, and the keys\' associated values may be changed.`,
    code: `
    d = {'food': 'spam', 'quantity': 4}
    `
  },

  { // begin new topic
    topic: 'Dictionaries',
    title: 'dict() initialization',
    reference: 'LearningPython5thEd p. 114',
    description: ``,
    code: `
    bob = dict(name='Bob', job='dev', age=40)
    `
  },

  { // begin new topic
    topic: 'Dictionaries',
    title: 'Check key existence',
    reference: 'LearningPython5thEd p. 117',
    description: ``,
    code: `
    'f' in d
    if not 'f' in D:
        print('missing')
    value = d['x'] if 'x' in d else 0
    `
  },

  { // begin new topic
    topic: 'Dictionaries',
    title: 'Sort keys',
    reference: 'LearningPython5thEd p. 119',
    description: ``,
    code: `
    for key in sorted(d):
        print(key, '=>', d[key]
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

  { // begin new topic
    topic: '',
    title: '',
    reference: '',
    description: ``,
    code: `
    
    `
  },

];


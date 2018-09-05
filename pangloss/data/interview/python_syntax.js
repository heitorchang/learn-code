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

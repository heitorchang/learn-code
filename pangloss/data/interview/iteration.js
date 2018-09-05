data = data.concat([

////////////////////////////////////////////////////////////
//
// Iteration, Iterators, Generators
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Iteration',
    title: 'Fibonacci sequence',
    reference: '',
    description: ``,
    code: `
def fib_iter(n):
    """Iterative version of Fibonacci sequence"""
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a

def test():
    """[0, 1, 1, 2, 3, 5, 8]"""
    testeql(fib_iter(0), 0)
    testeql(fib_iter(1), 1)
    testeql(fib_iter(3), 2)
    testeql(fib_iter(6), 8)
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'Why sequences are iterable',
    reference: 'Python Fluente, 453',
    description: `To iterate over an object x, <code>iter(x)</code> is called. This call checks if <code>__iter__</code> is implemented. If not, __getitem__ is called, starting with the index 0. If neither methods are implemented, TypeError is raised.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'Iterable, definition',
    reference: 'Python Fluente, 455, 461',
    description: `An iterable is any object from which the built-in function iter can obtain an iterator. Sequences are always iterable. While iterators are iterable, iterables are not iterators. Do not define __next__ and __iter__ in the same class, making it an iterable and iterator at the same time. One should be able to instantiate multiple, independent iterators from the same object.`,
    code: `
class C:
    def __init__(self):
        self.items = ['a','b']
    def __getitem__(self, index):
        return self.items[index]

c = C()
i = iter(c)
next(i)  # 'a'
next(i)  # 'b'
next(i)  # StopIteration
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'Iterator, definition',
    reference: 'Python Fluente, 458',
    description: `An iterator is any object that implements __next__, returning the next item in the sequence, and raises StopIteration when there are no more items. Iterators also implement __iter__, making them iterable. An iterator cannot be rewound; a new one (with initial state) must be created. The __iter__ method in an iterator may be: return self`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'Generator as __iter__',
    reference: 'Python Fluente, 462',
    description: `Any function that has <code>yield</code> is a generator. yield may be used more than once in a generator definition.`,
    code: `
import re

class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = re.findall(r'\\w+', text)
        
    def __iter__(self):
        for word in self.words:
            yield word
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'genexps (generator expressions)',
    reference: 'Python Fluente, 470',
    description: ``,
    code: `
import re

class Sentence:
    def __init__(self, text):
        self.text = text
    def __iter__(self):
        return (match.group() for match in re.finditer(r'\\w+', self.text))

s = Sentence("a man a plan a canal panama")
i = iter(s)
list(s)
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'count produces numbers by steps',
    reference: 'Python Fluente, 473',
    description: `itertools.count returns a generator. Does not end.`,
    code: `
gen = count(1, 0.5)
next(gen)  # 1
next(gen)  # 1.5    
next(gen)  # 2.0
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'takewhile predicate is True',
    reference: 'Python Fluente, 473',
    description: `An itertools generator that consumes another generator and stops when the given predicate is False`,
    code: `
gen = takewhile(lambda n: n < 3, count(1, 0.5))
list(gen)  # [1, 1.5, 2.0, 2.5]
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'compress keeps values for corresponding True values',
    reference: 'Python Fluente, 475',
    description: `itertools.compress consumes two iterables in parallel, returning the values of the first argument for which corresponding values of the second argument are True. The returned object is an iterator. 1 and 0 may be used instead of True and False`,
    code: `
a = compress([1,2,3,4,5], [True, False, False, True, True])
list(a)  # [1, 4, 5]
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'dropwhile predicate is True',
    reference: 'Python Fluente, 475',
    description: `itertools.dropwhile evaluates the predicate for items in the second argument. Once it is False, the remaining items are returned, and no more items are checked by the predicate.`,
    code: `
d = dropwhile(lambda n: n < 3, count(1, 0.5))
next(d)  # 3.0
next(d)  # 3.5
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'islice for iterables',
    reference: 'Python Fluente, 475',
    description: `itertools.islice(it, stop) and islice(it, start, stop, step=1) works for any iterable and is lazy`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'enumerate() pairs an index with the corresponding element',
    reference: 'Python Fluente, 476',
    description: `enumerate(iter, start=0)`,
    code: `
squares = [0, 1, 4, 9, 16, 25, 36, 49]

for (i, sq) in enumerate(squares):
    if sq % 2 == 1:  # if square is odd
        print("The square of", i, "is odd")
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'accumulate builds up partial results',
    reference: 'Python Fluente, 476',
    description: `itertools.accumulate produces accumulated sums. If a function of two arguments is given, it is applied to the first and second items, then to this result and the third item, and so on.`,
    code: `
a = [1, 2, 3, 4, 0, 6]
list(accumulate(a, lambda a, b: a * b))
# [1, 2, 6, 24, 0, 0]
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'chain joins given iterables',
    reference: 'Python Fluente, 478',
    description: `itertools.chain joins its arguments in order. chain.from_iterable(iter) joins the iterables within the given iterable.`,
    code: `
list(chain('ABC', range(1, 4)))
# ['A', 'B', 'C', 1, 2, 3]

list(chain(enumerate("ABC")))
# [(0, 'A'), (1, 'B'), (2, 'C')]
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'cycle repeatedly',
    reference: 'Python Fluente, 480',
    description: `itertools.cycle(iter) saves a copy of each item in iter and repeatedly produces them without end.`,
    code: `
list(islice(cycle(range(1, 4)), 10))
# [1, 2, 3, 1, 2, 3, 1, 2, 3, 1]
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'repeat an item',
    reference: 'Python Fluente, 480',
    description: `repeat(item, times=[forever]) repeats the given item the number of times given`,
    code: `
list(repeat(9, 3))
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'reversed',
    reference: 'Python Fluente, 483',
    description: `reversed(seq) returns a reverseiterator of a sequence or object that implements __reversed__`,
    code: `
reversed([1,2,3])    
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'groupby a given key',
    reference: 'Python Fluente, 483',
    description: `itertools.groupby(iter, key=None) produces tuples in the form (key, group) where key is the grouping criterion and group is the generator producing the corresponding items. Grouped items must be placed together in given iter.`,
    code: `
animals = ['bee', 'cat', 'duck', 'dog', 'tiger', 'sheep']
animals = sorted(animals, key=len)
[(length, list(group)) for (length, group) in groupby(animals, len)]
# [(3, ['bee', 'cat', 'dog']), (4, ['duck']), (5, ['tiger', 'sheep'])]    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'tee returns n generators',
    reference: 'Python Fluente, 483',
    description: `itertools.tee(iter, n=2) returns n independent generators that produce the items in iter.`,
    code: `
g1, g2 = tee('ABC')
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'yield from',
    reference: 'https://docs.python.org/3/whatsnew/3.3.html#pep-380',
    description: `yield from allows a generator to delegate part of its operations to another generator. For simple iterators, it replaces a for loop`,
    code: `
# for simple generators, yield from iterable is equivalent to:
    
for item in iterable:
    yield item
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'iterate until a sentinel is reached',
    reference: 'Python Fluente, 488',
    description: `iter(callable, sentinel) returns an iterator that stops when the sentinel was supposed to be returned.`,
    code: `
from random import randint
    
def d6():
    return randint(1, 6)

list(iter(d6, 1))
# [6, 3, 4, 2, 3, 6] : 1 is not present
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'Coroutines',
    reference: 'Python Fluente, 515',
    description: `Syntactically, coroutines look like generators. However, in a coroutine, yield will usually appear on the right side of an assignment. Unlike generators, you can both send and receive data to a coroutine.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'Interleave two lists',
    reference: 'https://stackoverflow.com/questions/7946798/interleaving-two-lists-in-python',
    description: `Note: lists must have the same length.`,
    code: `
from itertools import chain

a = [1, 2, 3]
b = ['a', 'b', 'c']

c = chain(*zip(a, b))
list(c)  # [1, 'a', 2, 'b', 3, 'c']
    `
  },

  { // begin new topic
    topic: 'Iteration',
    title: 'Group sequence into subsequences',
    reference: '',
    description: ``,
    code: `
size = 3
a = 'abcdefghijklmnopqrstuvwxyz'
[a[i:i+size] for i in range(0, len(a), size)]
# ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqr', 'stu', 'vwx', 'yz']
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

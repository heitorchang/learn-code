data = data.concat([

////////////////////////////////////////////////////////////
//
// FUNCTIONS
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Functions',
    title: 'Estimate from midpoints',
    reference: '',
    description: `Given a target, update guesses until the desired value is within a tolerance`,
    code: `
def sqrtEstimateMidpoint(x):
    left = 0
    right = x
    
    while True:
        midpoint = (right + left) / 2
        squareMidpoint = midpoint * midpoint

        if abs(squareMidpoint - x) < 1e-4:
            return midpoint
            
        if squareMidpoint > x:
            right = midpoint
        else:
            left = midpoint
    
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Recursion, basic (Fibonacci sequence)',
    reference: '',
    description: `Fibonacci sequence, not optimal but conceptually easy to understand.`,
    code: `
def fibRec(n):
    """Return the nth Fibonacci number. fib(0) = 0 and fib(1) = 1"""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibRec(n-1) + fibRec(n-2)

def test():
    """0, 1, 1, 2, 3, 5, 8"""
    testeql(fibRec(6), 8)
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'First-class function, definition',
    reference: 'Python Fluente, 175',
    description: `A first-class function:
<ul>
      <li>can be created at runtime</li>
      <li>can be assigned to a variable or inside a data structure</li>
      <li>can be passed as an argument to a function</li>
      <li>can be returned as the result of a function call</li>
</ul>
    `,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'map, starmap',
    reference: 'Python Fluente, 476',
    description: `map applies the given function to each element of the given iterable. starmap(f, iter) returns an iterable that applies f(*item_iter) for each item_iter that iter produces`,
    code: `
def square(x):
    return x * x

a = [1, 2, 3, 4, 5]
list(map(square, a))  # [1, 4, 9, 16, 25]

# alternative way, with listcomp
[square(n) for n in a]

# starmap    
import itertools, operator
list(itertools.starmap(operator.mul, enumerate('abc', 1)))
# ['a', 'bb', 'ccc']
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Higher-order function, definition',
    reference: 'Python Fluente, 177',
    description: `A higher-order function is a function that accepts a function as an argument or returns a function.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'applying a function to dynamic list of arguments',
    reference: 'Python Fluente, 178',
    description: `<code>apply</code> was removed because a function can be called with starred arguments`,
    code: `
# instead of apply(fn, args, kwargs), call

fn(*args, **kwargs)
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'filter',
    reference: '',
    description: `If predicate is True, the value is kept. itertools.filterfalse keeps items for which the predicate is False`,
    code: `
def is_odd(n):
    return n % 2 == 1

list(filter(is_odd, range(10)))  # [1, 3, 5, 7, 9]

list(filter(lambda x: x > 2, range(6)))  # [3, 4, 5]
    
# alternative way, with listcomp
[n for n in range(10) if n % 2 == 1]
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'reduce',
    reference: 'Python Fluente, 179',
    description: `reduce applies the given function to items of the iterable successively, returning the accumulated result`,
    code: `
from functools import reduce
from operator import mul

reduce(mul, range(1, 7))  # 720, same as factorial(6)
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'lambda creates anonymous functions',
    reference: 'Python Fluente, 180',
    description: `Lambdas are generally used in higher-order functions. In the example, we sort by the word ending to look for rhymes`,
    code: `
fruits = ['strawberry', 'fig', 'apple', 'cherry', 'raspberry', 'banana']
sorted(fruits, key=lambda word: word[::-1])
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Check if an object is callable',
    reference: 'Python Fluente, 181',
    description: ``,
    code: `
callable(2)  # False
callable(lambda x: x+1)  # True
callable(callable)  # True
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Variable number of arguments',
    reference: '',
    description: ``,
    code: `
def describe(category, *items, **properties):
    print(category)
    print(' '.join(items))
    print('\n'.join("%s : %s" % (key, val) for key, val in properties.items()))

describe("Games", 'Poker', 'Blackjack', 'Chess', owner="Joe", winner="Tim")
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'methodcaller',
    reference: 'Python Fluente, 197',
    description: ``,
    code: `
from operator import methodcaller

hyphenate = methodcaller('replace', ' ', '-')
hyphenate("something to do")  # 'something-to-do'
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'partial application',
    reference: 'Python Fluente, 198',
    description: `<code>partial</code> freezes part of the arguments passed to a function. By default, only the leftmost arguments may be frozen.<br><br>
    <code>partialmethod</code> works for methods.`,
    code: `
from unicodedata import normalize
from functools import partial

# typically, we would call normalize('NFC', s)
nfc = partial(normalize, 'NFC')
nfc('café')
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Closures',
    reference: 'Python Fluente, 232',
    description: `A closure is a function that has access to existing free variables when the function is defined, so that they may be used later when the scope of the definition is no longer available`,
    code: `
# calculate the average of a series of values
def make_averager():
    series = []

    def averager(new_value):
        series.append(new_value)  # here, series is a free variable
        total = sum(series)
        return total / len(series)

    return averager

# inefficient because the sum is repeatedly computed
    
# nonlocal is not needed because we were not assigning to series,
# only calling append (lists are mutable)

# a better solution uses 'count' and 'total',
# with nonlocal in averager

def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Single-dispatch',
    reference: '',
    description: `Decorating a simple function with <code>@functools.singledispatch</code> makes it a generic function (a group of functions that behaves in different ways, depending on the type of the first argument) `,
    code: `
from functools import singledispatch
import numbers
import html

@singledispatch
def htmlize(obj):
    content = html.escape(repr(obj))
    return "<pre>{}</pre>".format(content)

@htmlize.register(str)  # specify the type of the argument
def _(text):  # the name of a specific function is irrelevant; use _
    content = html.escape(text).replace('\n', '<br>\n')
    return "<p>{}</p>".format(content)

@htmlize.register(numbers.Integral)
def _(n):
    return "<pre>{0} (0x{0:x})</pre>".format(n)
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'A function may alter mutable arguments',
    reference: 'Python Fluente, 269',
    description: ``,
    code: `
def f(a, b):
    a += b
    return a

x = 1
y = 2
f(x, y)  # 3, but x is not altered

a = [1, 2]
b = [3, 4]
f(a, b)  # a becomes [1, 2, 3, 4]

t = (10, 20)
u = (30, 40)
f(t, u)  # (10, 20, 30, 40), but t is not altered
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Avoid mutable parameters as default values',
    reference: 'Python Fluente, 270',
    description: `The default value is evaluated when the function is defined, so when the mutable object is changed, this change will affect all future calls to that function. The solution is to use None as the default value, and make a copy of the argument passed.`,
    code: `
class Bus:
    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers)
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Rich comparisons, autocompleting',
    reference: 'https://docs.python.org/3/library/functools.html',
    description: `The decorator <code>@functools.total_ordering</code> supplies the class' remaining rich comparison ordering methods when one or more are of them defined.`,
    code: `
@total_ordering
class Student:
    def _is_valid_operand(self, other):
        return (hasattr(other, "lastname") and
                hasattr(other, "firstname"))
    def __eq__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) ==
                (other.lastname.lower(), other.firstname.lower()))
    def __lt__(self, other):
        if not self._is_valid_operand(other):
            return NotImplemented
        return ((self.lastname.lower(), self.firstname.lower()) <
                (other.lastname.lower(), other.firstname.lower()))    
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Newton\'s method to approximate an equation\'s solution',
    reference: 'SICP PDF, 108',
    description: `If x->g(x) is a differentiable function, then a solution of the equation g(x) = 0 is a fixed point of the function x->f(x), where f(x) = x - (g(x) / Dg(x)), where Dg(x) is the derivative of g evaluated at x.<br><br>A number x is a fixed point of a function f if f(x) = x. For some functions, repeatedly applying f(x), f(f(x)), f(f(f(x)))... can be done to find x.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Functions',
    title: 'Fixed point, finding',
    reference: 'SICP, 103',
    description: `Find x such that f(x) = x`,
    code: `
def fixedPoint(f, x):
    prev = x
    trial = f(x)
    while abs(trial - prev) > 0.0001:
        prev = trial
        trial = f(trial)
    return trial

def fixedSqrt(x):
    return fixedPoint(lambda y: 0.5 * (x/y + y), x)

fixedSqrt(2)  # 1.414213562...
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

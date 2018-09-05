data = data.concat([

////////////////////////////////////////////////////////////
//
// TOPIC NAME
//
////////////////////////////////////////////////////////////
  
  { // begin new topic
    topic: 'Decorators',
    title: 'Decorators, definition',
    reference: 'Python Fluente, 223',
    description: `A decorator is a callable that accepts another function as an argument (the decorated function). <br><br>
      A decorator can do some processing with the decorated function and return it or substitute it with another function. <br><br>
      Decorators are executed immediately after the decorated function is defined (typically when the module is imported, called import time)`,
    code: `
@deco
def target():
    print("Running target()")

# is the same as

def target():
    print("Running target()")

target = deco(target)
    `
  },

  { // begin new topic
    topic: 'Decorators',
    title: 'Substituting the decorated function',
    reference: 'Python Fluente, 223',
    description: ``,
    code: `
def deco(func):
    def inner():
        print("Running inner()")
    return inner

@deco
def target():
    print("Running target()")

target()  # Running inner()
    `
  },

  { // begin new topic
    topic: 'Decorators',
    title: 'Register functions in a registry',
    reference: 'Python Fluente, 224',
    description: ``,
    code: `
registry = []
def register(func):
    print("Running register(%s)" % func)
    registry.append(func)
    return func

@register
def f1():
    print("Running f1()");

@register
def f2():
    print("Running f2()");
    `
  },

  { // begin new topic
    topic: 'Decorators',
    title: 'Copy attributes of decorated function to decorator',
    reference: 'Python Fluente, 239',
    description: `To avoid __name__ and __doc__ being masked by a decorator, use <code>@functools.wraps</code>`,
    code: `
import functools

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        # code omitted
    `
  },

  { // begin new topic
    topic: 'Decorators',
    title: 'Stacking decorators',
    reference: 'Python Fluente, 246',
    description: `Nesting decorators work inside out`,
    code: `
@d1
@d2
def f():
    return "f"

# is the same as

f = d1(d2(f))
    `
  },

  { // begin new topic
    topic: 'Decorators',
    title: 'Decorators with arguments',
    reference: 'Python Fluente, 247',
    description: `To have a decorator that accepts arguments, we must create a decorator factory that accepts arguments and returns a decorator.`,
    code: `
registry = set()

def register(active=True):
    def decorate(func):
        print('running register(active=%s) -> decorate(%s)'
              % (active, func))
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        return func
    return decorate

@register(active=False)  # same as register(active=False)(f1)
def f1():
    print('running f1()')
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

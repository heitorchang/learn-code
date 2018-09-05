data = data.concat([

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Extend a built-in class',
    reference: 'Use a Cabeça Python',
    description: ``,
    code: `
class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        # list.__init__([])  # appears to be optional
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    def top3(self):
        return sorted(set(self))[:3]
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Instances may be callable',
    reference: 'Python Fluente, 182',
    description: `Defining __call__ inside a class definition allows instances of that class to be called.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'is compares identity and == value',
    reference: 'Python Fluente, 261',
    description: `<code>is</code> and <code>is not</code> compares the identity of objects, while == will compare their values`,
    code: `
alex_a = { 'name': 'Alex', 'born': 1990 }
alex_b = { 'name': 'Alex', 'born': 1990 }

id(alex_a)  # 17510012
id(alex_b)  # 17510274
    
alex_a == alex_b  # True
alex_a is alex_b  # False
    
alex_a is not alex_b  # True
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Use is to compare with None',
    reference: 'Python Fluente, 262',
    description: `Instead of using ==, use <code>is</code> and <code>is not</code> to check if a variable is or is not None`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Weakrefs',
    reference: 'Python Fluente, 276',
    description: `A weak reference does not increment the reference counter, so the object it refers to may be deleted when all its strong references are gone. Weakrefs are useful for caches. Weakref collections should be used instead of <code>weakref.ref</code> directly (WeakValueDictionary, WeakKeyDictionary, and WeakSet)<br><br>

    lists, dicts, ints, and tuples cannot be the target of a weakref, but user-defined types can. While a subclass of list may be the target of a weakref, a subclass of int or tuple cannot.
    `,
    code: `
import weakref

class Cheese:
    def __init__(self, kind):
        self.kind = kind

stock = weakref.WeakValueDictionary()
catalog = [Cheese('Tilsit'), Cheese('Brie'), Cheese('Parmesan')]

for cheese in catalog:
    stock[cheese.kind] = cheese

del catalog
sorted(stock.keys())  # ['Parmesan']

del cheese  # the temporary variable is a strong reference 
sorted(stock.keys())  # []
    `
  },
  
  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'classmethod (decorator)',
    reference: 'Python Fluente, 293',
    description: `@classmethod defines a method that operates on the class. The class itself (as <code>cls</code>) is received as the first argument, instead of what's typically the instance. This decorator is typically used for alternative constructors`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'staticmethod (decorator)',
    reference: 'Python Fluente, 293',
    description: `@staticmethod alters a method so that it doesn't receive the special first parameter. It is like a simple function that happens to be inside a class definition.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Read-only attributes',
    reference: 'Python Fluente, 299',
    description: ``,
    code: `
class Vector2d:
    def __init__(self, x, y):
        self.__x = float(x)  # use double underscore prefix
        self.__y = float(y)

    @property
    def x(self):
        return self.__x
        
    @property
    def y(self):
        return self.__y
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Hash value',
    reference: 'Python Fluente, 300',
    description: `Use XOR (^) to combine the hashes of the object's components.`,
    code: `
# in class Vector2d, with properties x and y

def __hash__(self):
    return hash(self.x) ^ hash(self.y)
    `
  },


  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Name mangling',
    reference: 'Python Fluente, 305',
    description: `Prefixing an attribute with two underscores will cause the attribute to become _ClassName__AttrName behind the scenes.<br><br>It may be better to explicitly use _ClassName_AttrName (single underscore prefix), because a single underscore has no special meaning. However, at a module level, names with a single underscore prefix will not be imported.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: '__slots__',
    reference: 'Python Fluente, 307',
    description: `__slots__ allows you to save memory. However, they are not inherited by subclasses. To define __slots__ is to say, "These are all the instance attributes for this class." Another downside of __slots__ is that an user will not be able to add other attributes to instances. To circumvent this, add '__dict__' to the __slots__ tuple. __weakref__ may also be added.`,
    code: `
class Vector2d:
    __slots__ = ('__x', '__y')
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Protocols',
    reference: 'Python Fluente, 322',
    description: `A protocol is an informal interface. For example, the protocol of a sequence implies onlt __len__ and __getitem__. Duck typing is calling an object a sequence because it behaves like one, not specifically because it is a subclass of sequence.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Attribute access',
    reference: 'Python Fluente, 329',
    description: `Implementing __getattr__ allows you to customize the result of <code>instance.x</code><br><br>__getattr__ is only called when the attribute, x, does not exist. If x is assigned to the instance, __getattr__ will no longer be called. __setattr__ must be defined to take care of this scenario.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'super()',
    reference: 'Python Fluente, 331, 401',
    description: `<code>super()</code> allows you to access methods from superclasses.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Interface and protocol, definition',
    reference: 'Python Fluente, 354, https://stackoverflow.com/questions/372042/difference-between-abstract-class-and-interface-in-python',
    description: `An interface is a set of method definitions. It is the subset of an object's public methods that allows it to play a specific role in the system.<br><br>A protocol is an informal interface. They are independent of inheritance. Protocols cannot be verified statically by the interpreter.<br><br>An analogy in the real world is the controls of a car. The interface of a car is the steering wheel, pedals, horn, and other controls.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Polymorphism, definition',
    reference: 'https://stackoverflow.com/questions/409969/polymorphism-define-in-just-two-sentences',
    description: `A language feature that allows values of different types to be handled by a uniform interface.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Goose typing',
    reference: 'Python Fluente, 361',
    description: `Goose typing is using <code>isinstance(obj, cls)</code>, where cls is an abstract base class (ABC). In other words, cls' metaclass is abc.ABCMeta`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Virtual subclass',
    reference: 'Python Fluente, 378, 796',
    description: `A virtual subclass does not inherit from a superclass, but it is registered as <code>TheSuperClass.register(TheSubClass)</code>, or with a decorator <code>@TheSuperClass.register</code>`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'API, definition',
    reference: 'https://www.reddit.com/r/learnprogramming/comments/1xvm9l/can_some_eli5_what_an_api_is/',
    description: `An API (Application Programming Interface) is the set of functions, protocols, and tools for building software. It allows a programmer to use and access code written by the API's author.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Subclass UserCollections instead of built-ins',
    reference: 'Python Fluente, 397',
    description: `Subclassing built-ins directly is unreliable because overwritten methods are not called. Instead, subclass UserList, UserDict, and UserString from the collections module.`,
    code: `
    
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'MRO (Method Resolution Order)',
    reference: 'Python Fluente, 399',
    description: `The __mro__ attribute in a class is a tuple in the MRO order. To call a specific superclass method, call the class method and pass the instance as its first argument.`,
    code: `
class B():
    def pong():
        print("PONG", self)

class C():
    def pong():
        print("PONG", self)

class D(B, C):
    def ping(self):
        print("PING", self)

d = D()
C.pong(d)
    `
  },

  { // begin new topic
    topic: 'Object-Oriented Programming',
    title: 'Subclasses must explicitly call super\'s __init__',
    reference: 'https://stackoverflow.com/questions/3782827/why-arent-pythons-superclass-init-methods-automatically-invoked',
    description: `There is a difference between __init__ and __new__. The superclass' __init__ must be called explicitly.`,
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

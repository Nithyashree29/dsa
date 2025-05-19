# Polymorphism - The ability to define generic type of behaviour that will (potenetially) behave differently when applied to different types.
# Python is very polymorphic in nature

# Special Methods
# we've already seen many special methods
# __init__   -> used during class instantiation.
# __enter__
#            -> context managers with ctx() as obj
# __exit__
  
#  __getitem__
#  __setitem__   -> sequence types a[i], a[i:j], del a[i] 
#  __delitem__ 
 
# __iter__
#                -> iterables and iterators, iter() or next()
# __next__

# __len__ -> implements len()
# __contains__ -> implements in 

# __str__ vs __repr__
# -> both are used to creating string representation of an object
# typically __repr__ is used by developers
# -> try to make it so that the string could be used to recreated the object.
# - otherwise make it as descriptinve as possible.
# - useful for debugging.
# - called when using the repr() function.

# __str__ is used by str() and print() functions, as well as various formatting functions.
# - typically used for display purposes to end user, logging. etc.
# - if __str__ is not implemented python will look for __repr__ method .
# if neither is implemented and since all objects inherit from Object, will use _repr__ defined there instead. 

# Hashing and Equality
class Person:
    pass

p1 = Person()
p2= Person()
hash(p1), hash(p2)
# Note - Two objects are equal if they have same hash

class Person:
    def __init__(self, name):
        self.name = name
        
    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name
    
    def __repr__(self):
        return f"Person(name= '{self.name}')"
    
# Note - as soon as it sees the eq method, it takes away the hash implementation. values might be same but address is different, so implement your own hash.
class Person:
    def __init__(self, name):
        self._name = name
        
    @property
    def name(self):
        return self._name 
        
    def __eq__(self, other):
        return isinstance(other, Person) and self.name == other.name
    
    def __hash__(self):
        return hash(self.name)
    
    def __repr__(self):
        return f"Person(name= '{self.name}')"

p1 = Person('Eric')
p2 = Person('Eric')

p1 == p2
hash(p1) == hash(p2)

class MyList:
    def __init__(self, length):
        self._length = length
        
    def __len__(self):
        print('__len__ called')
        return self._length

l1 = MyList(0)
l2 = MyList(10)

# Special Methods - callables
# Any object can be made to emulate a callable by implementing a __call__ method 
class Person:
    def __call__(self, name):
        return f'Hello {name}'
    
p = Person()
p('Eric')
p.__call__('Eric')
# usefull for creating function-like objects that need to maintain state.staticmethod.
# useful for creating decorator classes

from functools import partial

def func1(a,b,c):
    return a + b + c

partial_func = partial(func1, 10, 20)
partial_func(30)

class Partial:
    def __init__(self, func, *args):
        self._func = func
        self._args = args
    
    def __call__(self, *args):
        return self._func(*self._args, *args)
    
partial_func = Partial(func1, 10, 20)
partial_func(30)

import random
from time import perf_counter, sleep
from functools import wraps

def profiler(fn):
    _counter = 0 
    _avg_time = 0
    _total_elapsed = 0
    
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal _counter
        nonlocal _total_elapsed
        nonlocal _avg_time
        _counter += 1
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        _total_elapsed += (end - start)
        _avg_time = _total_elapsed / _counter
        return result
    
    def counter():
        return _counter
    
    def avg_time():
        return _avg_time
    
    inner.counter = counter
    inner.avg_time = avg_time
    
    return inner

@profiler
def func():
    sleep(random.random())
    
func1()
func1.counter()

# Alternate
class Profiler:
    def __init__(self, fn):
        self.couter = 0
        self.total_elapsed = 0
        self.fn = fn
        
    def __call__(self, *args, **kwargs):
        self.counter += 1
        start = perf_counter()
        result = self.fn(*args, **kwargs)
        end = perf_counter()
        self.total_elapsed += (end - start)
        
    @property
    def avg_time(self):
        return self.total_elapsed / self.counter
    
@profiler
def func_1(a, b):    
    sleep(random.random())
    return (a, b)
    
func_1 = profiler(func_1)

class Person:
    def __init__(self, name, dob):
        self.name = name
        self.dob = dob
        
    def __repr__(self):
        print('__repr__ called...')
        return f'Person(name={self.name}, dob={self.dob.isoformat()})'
    
    def __str__(self):
        print('__str__ called...')
        return f'Person({self.name})'

    def __format__(self, date_format_spec):
        print('__format__ called...')
        dob = format(dob, date_format_spec)
        return f'Person(name={self.name}, dob={self.dob})'
    
    
  
  
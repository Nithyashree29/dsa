import random
import numbers
from functools import lru_cache

lst = [random.randint(0,10) for _ in range(100)]
print(lst)

def freq_analysis(lst):
    return {k: lst.count(k) for k in set(lst)} 

print(freq_analysis(lst))

import sys
keys = sys.argv[1::2]
values = sys.argv[2::2]

print(f'{keys}')
print(f'{values}')

#python .\test.py --last-name clease --first-name jo

args = {k: v for k, v in zip(keys, values)}
print(args)


first_name = args.get('--first_name', None)
last_name = args.get('last_name', None)

# Thigs studied 
# functions and functions arguments - def my_func(p1, p2, *args, k1=None, **kwargs)
# lambda lambda x, y: x+y
# packing and unpacking iterables = my_func(*my_list)
# closures - nested scopes, free variables
# decorators - @my_decorator @my_decorator(p1, p2)
# Boolean truth values = bool(obj)
# named tuples = namedtuple('Data', 'field_1 filrd_2')

# zip - zip(list1, list2, list3)
# map - map(lambda x: x**2, my_list)
# reduce = reduce(lambda x, y: x * y, my_list, 10)
# filter = filter(lambda p: p, age > 18, persons)
# sorted = sorted(persons, lambda p: p.name.lower())

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
       if value <= 0:
           raise ValueError('Age must be greater than 0')
       else:
           self._age = value
           

class silly:
    def __init__(self, n):
        self.n = n
        
    def __len__(self):
        print|('Called __len__')
        return self.n
    
    def __getitem__(self, value):
        if value < 0 or value >= self.n:
            raise IndexError
        return 'This is a silly element'

from functools import lru_cache

@lru_cache
def fib(n):
    if n < 2:
        return n
    else:
        return fib(n-1) * fib(n-2)
    

fib(1)      

class Fib:
    def __init__(self, n):
        self.n = n
        
    def __len__(self):
        print|('Called __len__')
        return self.n
    
    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0:
                s  = self.n + s
                
            if s < 0 or s>= self.n: 
                raise IndexError
            else:
                return Fib._fib(s)
        else:
            start, stop, step = s.indices(self.n)
            rng = range(start, stop, step)
            return [fib._fib(i) for i in rng]
            
    @staticmethod
    @lru_cache(2 * 10)
    def _fib(n):
        if n < 2:
            return n
        else:
            return Fib._fib(n-1) + Fib._fib(n-2)

fib = Fib(10)
print(list(fib))

class MyClass:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f'MyClass(name={self.name})'
    
    def __add__(self, other):
        print(f'You called += on {self} and {other}')
        return 'Hello from __add__'
    
    def __iadd__(self, other):
        print(f'You called += on {self} and {other}')
        return 'Hello from __iadd__'
    
c1 = MyClass('instance 1')
c2 = MyClass('instance 2')
result = c1 + c2       


class MyClass:
    def __init__(self, name):
        self.name = name
        
    def __repr__(self):
        return f'MyClass(name-{self.name})'
    
    def __add__(self, other):
        return MyClass(self.name + other.name) 
    
    def __iadd__(self, other):
        if isinstance(other, MyClass):
            self.name += other.name
        else:
            self.name += other
        return self
    
    def __mul__(self, n):
        return MyClass(self.name * n)
    
    def __imul__(self, n):
        self.name += n
        return self       
    
    
class Point:
    
    def __init__(self, x, y):
        if isinstance(x, numbers.Real) and isinstance(y, numbers.Real):
            self._pt = (x, y)
            
        else:
            raise TypeError('Point co-ordination must be real numbers')
        
    def __repr__(self):
        return f'Point(x = {self._pt[0]}, y = {self._pt[1]})'
    
    def __len__(self):
        return len|(self._pt) 
    
    def __getitem__(self, s):
        return self._pt[s]
    
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
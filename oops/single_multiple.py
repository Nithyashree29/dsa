# Inheritance 
# - Fundamental concept in object oriented programming.
# - classes define properties and methods.
# - they can foprm a natural hierarchy.

 
# Implications of inheriting from object
# -> any object we create automatically inherits behaviors and attributes from object class.
#  -> __name__ 
#  -> __new__ 
#  -> __init__ many more ...
 
# The object is a class, lets say built in python class. every class in Python inhgerits from that class. 
type(object), type(int) #etc

class Person:
    pass
issubclass(int, object)
issubclass(Person, object) #True
# Module class is a type
import math
import types
type(math) #module
ty = type(math)
type(ty)  #type

def my_func():
    pass

type(my_func)
types.FunctionType is type(my_func) # True
types.FunctionType is type(math)  # True
dir(object)
o1 = object()
str(o1) , repr(o1)

class Person(object):
    pass 
  # or
  
  
class Person:
    pass

p = Person()
str(p) , repr(p)  # it gonna be use from inheritence chain

id(Person.__init__), id(object.__init__) # both will be same because you are inheriting from object class

class Person:
    def __init__(self):   #essentially you are overriding the init from object class, so id's will change
        pass
    
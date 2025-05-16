# classes (types) and object
# functions, methods and propeties
# polymorphism and speial dunder methods
# single inheritance
# descriptors
# enumerations
# exceptions

# class Attributes - 
class MyClass:
    language = 'Python'
    version = '3.9' 
    
getattr(MyClass, 'language')
getattr(MyClass, 'x', 'N/A')
# dot notation
MyClass.language
MyClass.x = AttributeError

# set attribute
setattr(MyClass, 'language', '3.7')
 
# Setting an attribute value to a callable
# Attribute values can be any object - other classes, any callable, amything.

class MyClass:
    language = 'Python' #class attribute
    
    def say_hello():
        print('Hello World!')
        
# Sayhello is also an attribute of the class -> its value happens to be callable
obj1 = MyClass.__dict__['say_hello']
obj1()

getattr(MyClass, 'say_hello')() 

# Class are callable
# When we  crate a class using the class keyword
# Python automatically adds behavious to the class
# - it aggs comething to make class callable. 
# - The return value of that callable is an object. 

# When we call a class instance object is created
# - The object has some attributes Python automatically implements fpr us:
#     __dict__ is the object's local namespace.
#     __class__ tells us which class was used to instantiate the object.
 
# ss 
class Person:
    def say_hello():
        print("Say Hello!")
        
        
obj1 = Person()
obj1.say_hello() # will give type error because it is not accepting any argument but you can give as below because it is bound object

Person.say_hello() # works fine
#    w   o      r    k    s                      
#  calling obj.method(args) -> method__func__(method.__self__, args) 

# Instance Methods
class Person():
    def say_hello(obj):    #first param will receive instance object, we often call as instance method
        print("Hey Hi!!")
 
 
# Note - In summary functions hat are defined in the class are transformed into methods when they're called from instances of the class.

# Initializing Class Instances
# when we create a class, by default python does two separate things:
#     - creates a new instances of the class.
#     - initializes the namespace of the class. 
     
class MyClass:
    language ='PYTHON'
    
    def __init__(self, version):
        self.version = version
        
# when we call MyClass(3.7) 
# - python creates a new instance of the object with an empty namespace.
# - if we have defined an __init__ function in the calss
#    - it calls obj.__init__(3.7) -> boundmethod -> MyClass.__init__(obj, '3.7')
    #  - function runs and adds version to the obj's namespace
    # - version is an instance attribute

# Bind or create a method to an instance at runtime.
# Creating Attribute At Run Time
class MyClass:
    language = 'Python'

obj = MyClass()

import math
from time import perf_counter
from types import MethodType

MethodType(function, object)
obj.say_hello = MethodType(lambda self: f'Hello {self.language}!, obj')
   
    
class Person:
    pass

p1 = Person()
p2 = Person()

p1.__dict__, p2.__dict__

p1.say_helo = lambda: 'hello'
print(p1.say_hello)

class Person:
    def __init__(self, name):
        self.name = name
        
p1 = Person('Eric')
p2 = Person('Alex')

def say_helo(self):
    return f'{self.name} says hello!'    
    
say_helo(p1)

# now add a method to an instance
p1.say_hello = MethodType(lambda self: f'say hi {self.name}', obj)
p2.say_hello = MethodType(say_helo, p1)


class Person:
    def __init__(self, name):
        self.name = name  # Bare attribute approach
    
    def register_do_work(self, func):
        # self._do_work = MethodType(func, self)
        setattr(self, '_do_work', MethodType(func, self))    
    
    def do_work(self):
        do_work_method = getattr(self, '_do_work', 'None')
        if do_work_method:
            return do_work_method()
        else:
            raise AttributeError('You must first register a do_work method')    
    
        
p1 = Person('Eric')

def work_math(self):
    return f'{self.name} will teach differentiatls today'

p1.register_do_work(work_math)

# PROPERTIES
class MyClass:
    def __init__(self, language):
        self._language = language
    
    def get_language(self):
        return self._language
    
    def set_language(self, value):
        self._language = value
        
# There are some good reasons why we might want to approach attribute using this programming style.
# - provides control on how an attribute's value is set and returned
 
# we can use a special property class
class MyClass:
    def __init__(self, language):
        self._language = language
        
    def  get_language(self):
        return self._language
    
    def set_language(self, value):
        self._language = value
        
    language = property(fget= get_language, fset=set_language)

   
class Person:
    def __init__(self, name):
        self.set_name(name)
        
    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if isinstance(value, str) and len(value.strip()) > 0:
            self._name = value
        else:
            raise ValueError('name must be an non empty string')
# Private variable - in oop you have access to variable as long as they are public.if its private no access from outside class but from inside yes.

# Property decorator

# ss 
class MyClass:
    def __init__(self, language):
        self._language = language
        
    @property   
    def language(self):
        return self._language
    
    @language.setter
    def language(self, value):
        self._language = value

# example decorator
def my_decorator(fn):
    print('decorating functions')
    def inner(*args, **kwargs):
        print('running decorated function')
        return fn(*args, **kwargs)
    return inner

# undecorated_function= my_decorator(my_func)
@my_decorator 
def my_func(a,b):
    print('running original function')
    return a + b

class Circle:
    def __init__(self, r):
        self.r = r
        
    @property
    def area(self):  # Read-only computed properties
        return math.pi * self.r * self.r   

class Circle:
    def __init__(self, radius):
        self.radius = radius
        self._area = None
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        self._area = None #logic lies here babe
        self._radius = value
        
    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * (self.radius)
        return self._area

class WebPage:
    def __init__(self,url):
        self.url = url
        self._page = None
        self._load_time_secs = None
        self._page_size = None
        
    @property
    def url(self):
        return self._url 
    
    @url.setter
    def url(self, value):
        self._url = value
        self._page = None
        
    @property
    def page(self):
        if self.page is None:
            self.download_page()
        return self._page
    
    @property
    def page_size(self):
        if self._page is None:
            self.download_page()
        return self._page_size
    
    @property
    def time_elapsed(self):
        if self._page is None:
            self.download_page()
        return self._load_time_secs
    
    def download_page(self):
        self._page_size = None
        self._load_time_secs = None
        start_time = perf_counter()
        with urllib.request.urlopen(self.url) as f:
            self._page = f.read()
        end_time = perf_counter()
        self._page_size = len(self._page)
        self._load_time_secs =  end_time - start_time        

urls = [
    'https://www.google.com',
    'https://www.python.org',
    'https://www.yahoo.com'
]

for url in urls:
    page = WebPage(url)
    print(f'{url}\tsize={format(page.page_size, "_")}\telapsed={page.time_elapsed:.2f} secs')


    
class UnitCircle:
    def __init__(self, color):
        self._color = color
        
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, value):
        self._color = value
        
    @color.deleter
    def color(self):
        del self._color
           
            
        
        
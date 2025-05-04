# Context = The circumstances that form the setting for an event, statement, or idea, and in terms of which it can be fully understand.
# In Python its the state surrounding a section of code.

# module.py
f = open('test.txt', 'r')   #Create the context  
# open('test.txt') --> creating a context manager
print(f.readlines()) #work inside the context
f.close()  #exit the context

# f -> a file object, global scope,
#   print(f.readlines()) runs, it has a context in which it runs.
# it running inside global scope context
# Context managers manage data in our scope. -> on entry, on exit
# like usefull in 
# 1. open /close file
# 2. start db transaction / commit or abort transactions.
# 3. set decimal precision to 3/ reset back to original precision.

# The context management protocol
# classes implement the context management protocol by implementing two methods
# __enter__ - setup and optionally return some object.
# __exit__ - tear down / cleanup

# with CtxManager() as obj:
#     #do something
#     #done with context
    
# mgr = CtxManager()
# obj = mgr.__enter__()
# try:
#     # do something
# finally:
#     # done with context
#     mgr.__exit__()
    
# Common Patterns
# open - close
# lock - Release
# Change - Reset 
# Start - Stop
# Enter - Exit  
        
class Myclass:
    def __init__(self):
        # init class
        pass
    def __enter__(self):
        return object
    
    def __exit__(self,):
        # clean up obj
        pass
    
# with Myclass() as obj:
#     -> creates an instance of Myclass -> no associated, but an instance exists.
#     -> calls my_instance.__enter__()
#     -> return value from __enter__ is assigned to obj (Note that not the instance of Myclass that was created)
# after the with block, or if an Exception occurs inside the with block:
#     -> my_instance.__exit__is exicuted.

# the __exit__ method needs three arguments - exception_type, exception_value, traceback
# ss
# ss
 
def test():
    with open('imp_links.txt', 'w') as file:
        print('inside with: fileclosed?', file.closed)
        return file
     
file = test()
file.closed
     
class MyContext:
    def __init__(self):
        self.obj = None
        
    def __enter__(self):
        print('entering context...')
        self.obj = 'the Return object' 
        return self.obj
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        print('exiting context...')
        if exc_type:
            print(f"*** Error occured: {exc_type}, {exc_value}") 
        return False #if want to supress the error return True
   
ctx =  MyContext()    
with ctx as obj:
    print('inside with block', 'r')
    raise ValueError('custom message')
     
class Resource:
    def __init__(self, name):
        self.name = name
        self.state = None
        

class ResourceManager:
    def __init__(self, name):
        self.name = name
        self.resource = None
        
    def __enter__(self):
        print('entering context')
        self.resource = Resource(self.name)
        self.resource.state = 'created' 
        return self.resource
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        print('exiting context')
        self.resource.state = 'destroyed'
        if exc_type:
            print('error occurred')
        return False
    
with ResourceManager('spam') as res:
    print(f'{res.name} = {res.state}')
print(f'{res.name} = {res.state}')
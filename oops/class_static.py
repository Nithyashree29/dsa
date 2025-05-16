# Class Methods - A function in a class that will always be bound to the class, and never the instances. 
# MyClass.fn -> method bound to class
# obj.fn -> method bound to MyClass

class MyClass:
    def hello():
        print('hello')
        
    def inst_hello(self):
        print(f'hello from {self}')
    
    @classmethod
    def cls_hello(cls):
        print(f'hello from {cls}')
        

#                 MyClass                      Instance
# hello           regular function              method bound to instance (by default, any function defined in a class will be handled as a bound method when called from an instance) 
#                                               Note - make sure about the args
# inst_hello      regular Function              method bound to instance 
# cls_hello       method bound to class         method bound to class

# Static Method -  A function in a class that will never be bound to any object called.
class MyClass:
    def inst_hello(self):
        print("hello")
        # Function bound to instance when called from instance - will receive instance as first parameter
    @classmethod
    def cls_hello(cls):
        print("hello")
        # Function bound to class when called from either the class or instance - will receive the class(MyClass) as first parameter
    @staticmethod
    def static_hello():
        print('static hello') 
        # Sstatic method is never bound to anything - receives no extra argument no matter how it is called.

# why static method 
# - cases where it makes sense for a function toi live in a class.
# - but doess not need access to either the instance or the class state. 
     
class Language:
    MAJOR = 3
    MINOR = 7
    REVISION = 4
    
    @property
    def version(self):
        return '{}, {}, {}'.format(self.MAJOR, self.MINOR, self.REVISION)
    
    @classmethod
    def cls_version(cls):
        return '{}, {}, {}'.format(cls.MAJOR, cls.MINOR, cls.REVISION)                        
        
    @staticmethod
    def static_version():
        return '{}, {}, {}'.format(Language.MAJOR, Language.MINOR, Language.REVISION)
    
    
l = Language()
l.MAJOR

# scope of variables

name = 'Guido'

class MyClass:
    name = 'Raymond'
    list_1 = [name] * 3
    list_2 = [name for i in range(3)]
    
    @classmethod
    def hello(cls):
        return '{} says hello'.format(name)
    

MyClass.hello()
MyClass.hello()    
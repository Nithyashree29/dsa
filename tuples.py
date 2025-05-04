# Tuples - Are read only lists.
#Tuples -  containers, order matters, heterogeneous/homogeneous, indexable, iterable, immutable, fixed length, fixed order
# Lists -  containers, order matters, heterogeneous/homogeneous, indexable, iterable, mutable, order, length can change
# Strings -  containers, order matters, homogeneous, indexable, iterable, immutable. fixed length, fixed order

# Immutability of Tuples
#1. elements cannot be added or removed.
#2. The order of elements cannot be changed.
#3. Works well for representing data structures.

 
s1 = (1, 2,3 ,6, 7,8 ,9)
print(s1)

# Modules packages and NameSspaces
# Modules - objects of type ModuleType
# Module - An objectr of certain data type     
def func():
    print("heye hey ")
f =  globals()['func']  #global namespaces
f()

def func():
    locals() # local namespaces inside main functions
print(globals())
# if you import any module the reference is added in global dictionary
# can check with sys.modules('your module name) , id(sys.modules()['math'])
import importlib.util
import math
#introspection
math.__name__
math.__dict__
math.__dict__['sqrt']

import fractions
import sys
sys.modules['fractions']
fractions.__dict__
dir(fractions)

import types
isinstance(fractions, types.ModuleType)

mod = types.ModuleType('test', 'this is module')
mod.__dict__
mod.hello = lambda: 'hello!'
print(mod.hello())
hello = mod.hello 
print(hello())

from collections import namedtuple
mod.Point = namedtuple('Point', 'x y')
p1 = mod.Point(0,0)

PT = getattr(mod, 'Point')
print(PT(10,20))
PT = mod.__dict__['Point']
print(PT(20,30))

print(mod.Point(20,30))

# Importing Modules
#What is Python actually doing?
#The first thing to note is that Python is doing the import at run time, i,e, while your code is actually running.
#This is different from traditional compiled language such as C where modules are compiled and linked at compile time.
#In both cases through, the system needs to know where those files exists.
#Python uses a relatively system of how to find and load modules. I'm not going to even attempt to describe this in detail, but we'ii take a brief look at the main points.
import sys
#sys.prefix -  where is python installed
#sys.exec_prefix - where are the compiled C binaries located.
#0sys.path -  where does python look for imports.

#At a high level, this is how Python imports a module from file:
#    checks the sys.modules cache to see if the module has already been imported - if so it simply uses the reference in there, otherwise:
#    creates a new module object (types.ModuleType)
#    loads the source code from file.
#    adds an entry to sys.modules with name as key and newly created
#    compiles and executive the source code.
import os.path

module_name = 'decorator'
module_file = 'decorator.py'
module_path = '.'

module_rel_file_path = os.path.join(module_path, module_file)
module_abs_file_path = os.path.abspath(module_rel_file_path)

with open(module_rel_file_path, 'r') as code_file:
    source_code = code_file.read()
    
mod = types.ModuleType(module_name)
mod.__file__ = module_abs_file_path

# set a reference in sys module
sys.modules[module_name] = mod

# compile source code
code = compile(source_code, filename=module_abs_file_path, mode='exec')

# execute compiled source code
print(exec(code, mod.__dict__))

#Done!!
#*
#finders + loaders = importers


import importlib
fractions = importlib.import_module('fractions')

# finders = returns module spec  =  fractions.__spec__, also specifies the loader 
importlib.util.find_spec('decimal')

import os
ext_module_path = os.environ['HOMEPATH']
file_abs_path = os.path.join(ext_module_path, 'module1.py')
with open(file_abs_path, 'w') as code_file:
    code_file.write("print('Running module1.py ...)\n")
    
importlib.util.find_spec('module1') # it has to know the path , if its in other than sys.path - then it will say module not found error.

# you can add using sys
sys.path.extend(ext_module_path)

# +
Steps
1. import math
2. is math in sys.modules
3. if not load it and insert ref in sys.modules
4. add symbol math to module1's global namespace referencing the same object
5. module1.globals()
6. if math symbol alreadfy present in module1's namespace, replace reference.

from match import sqrt
1. is math in sys.modules
2. if not, load it and insert ref in sys.modules.
3. add symbol sqrt to module1's global namespace referencing math.sqrt

  
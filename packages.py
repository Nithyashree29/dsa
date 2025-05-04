# Packages are modules, But modules are not necessarily packages
# they can contain modules , packages which are called sub-packages

# If a module is a package, it must have a value set for __path__
# After you have implemented a module, you can easily see if that module is a package by inspecting the __path__ attribute.
# empty -> Module
# non-empty -> package 

# File based packages

# -> package paths are created by using file system directories and files.
# Remember: a package is simple a module that can contain other modules/packages.
# On a file system we therefore have to use directories for packages.
# The directory name become the package name.
# So where  does the code go for the package (since it is a moddule)? -> will be in __init__.py 

# To create  a package in our system, we must:
#     create a directory whose name will be the package name.
#     create a file called __init__.py inside that directory
    
# that __init__.py file is what tells Python that the directory is a package as opposed to a standard dirtectory.
# (If we dont have an __init__.py file, then Python creates an implicit namespace package)

# Note:
#     __file__ is the location of module code in the file system.
#     __package__ is the package the module code is located in
#        An empty string is the module is located in the application root
#     if the module is also a package, then it also has a __path__ property.
    
# app/
#     module.py
    
#     pack1/
#         __init__.py
#         module1a.py
#         module1b.py
        
#         pack1_1/
#             __init__.py
#             module1_1a.py
#             module1_1b.py
                   
# module.__file__ - > ../app/module.py 
# module.__path__ -> not set
# module.__package__ -> '' 

# pack1.__file__ -> ../app/pack1/__init__.py 
# pack1.__path__ -> ../app/pack1 
# pack1.__packahe__ => pack1 
# pack1.module1a.__file__ -> ../app/pack1/module1a.py 
# pack1.module1a.__path__ -> not set 
# pack1.module1a.__package__ -> pack1 

print(1,2)
       
4.+
import email
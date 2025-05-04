"""
    This is often used in class properties
"""

import math

class Circle:
    def __init__(self, r):
        self.radius = r
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, r):
        self._radius = r
        self.area = math.pi * ( r **2)
        
#evrytime you create the radius you create th area - whats happens if lot of circles and no use of area
    
class Circle:
    def __init__(self, r):
        self.radius = r
        self._area = None
        
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None # when your radius changes
        
    @property
    def area(self):
        if self._area is None:
            self._area = math.pi * (self.radius ** 2)
        return self._area
    
    
class Factorials:
    def __init__(self, length):
        self.length = length
        
    def __iter__(self):
        return self.FactIter(self.length)
    
    class FactIter:
        def __init__(self, length):
            self.length = length
            self.i = 0
            
        def __iter__(self):
            return self
 
        def __next__(self):
            if self.i >= self.length:
                raise StopIteration
            else:
                result = math.factorial(self.i)
                self.i += 1
                return result            
    

#build in iterables and iterators
# Note - if a object is an iterable(but not an iterator) you can iterate over it many times.
# If an object is an iterator you can iterate over it only once.
# range(10) -> iterable
# zip(l1, l2) -> iterator
# enumerate(l1) -> iterator
# open('cars.csv') -> iteratoe
# dictionary .keys() -> iterable
# .values() -> iterable
# .items() -> iterable

with open('cars.csv') as f:
    print(type(f))
    print('__iter__' in dir(f))
    print('__next__' in dir(f))
    l = f.readlines()
    print(l)    
    
with open('cars.csv') as f:
    print(iter(f) is f)
    
l = [1,2 ,3,4,5]
iter(l) is l

file_name = 'nyc_parking_tickets_extract.csv'
with open(file_name) as f:
    for _ in range(10):
        print(next(f))
        
with open(file_name) as f:
    column_headers = next(f).strip('\n').split(',')
    sample_data = next(f).strip('\n').split(',')
    
column_headers
column_names = [header.replace(' ', '_') for header in column_headers]
zip(column_names, sample_data)

from collections import namedtuple

Ticket = namedtuple('Ticket', column_names)
with open(file_name) as f:
    next(f)
    raw_data_row = next(f)
    
raw_data_row
def read_data():
    with open(file_name) as f:
        next(f)
        yield from f 

raw_data = read_data()
for i in range(5):
    print(next(raw_data))  

def parse_int(value, *, default=None):
    try:
        return int(value)
    except ValueError:
        return default
    
from datetime import datetime

def parse_date(value, *, default=None):
    date_format = '%m/%d/%Y'
    try:
        return datetime.strptime(value, date_format).date()
    except ValueError:
        return default
    
parse_int(10)
  
def parse_string(value, *, default=None):
    try:
        cleaned = value.strip()
        if not cleaned:
            return default
        else:
            return cleaned
    except ValueError:
        return default
    
parse_string('        hello ya    ')

column_names

from functools import partial
column_parsers = (parse_int, parse_string, lambda x: parse_string(x, default=''), partial(parse_string, default=''),
                  parse_date, parse_int, partial(parse_string, default=''),
                  parse_string,
                  lambda x: parse_string(x, default='')
                  )

def parse_row(row):
    fields = row.strip('\n').split(',')
    parse_data = (func(filed) for func, filed in zip(column_parsers, fields))
    return parse_data

rows = read_data()
for _ in  range(5):
    row = next(rows)
    parsed_data = parse_row(row)
    print(list(parsed_data))
    
# Truthy - all([10, 'hello'])
# all([10, 'key', None,''])
def parse_row(row, * , default = None):
    fields = row.strip('\n').split(',')
    parse_data = (func(filed) for func, filed in zip(column_parsers, fields))
    if all(item is not None for item in parsed_data):
        return Ticket(*parsed_data)
    else:
        return default
    
for row in read_data():
    parsed_row = parse_row(row)
    if parsed_row is None:
        print(list(zip(column_names, row.strip('\n').split(','))),
        end= '\n\n')
    
def parsed_data():
    for row in read_data():
        parsed = parse_row(row)
        if parsed:
            yield parsed
            
parsed_rows = parsed_data()
for _ in range(5):
    print(next(parsed_rows))
    
from collections import defaultdict
# makes_count = {}
makes_count = defaultdict(int)
for data in parsed_data():
    if data.vehicle_make in makes_count:
        makes_count[data.vehicle_make] += 1
    else:
        makes_count[data.vehicle_make] = 1
print(makes_count)

for make, cnt in sorted(makes_count.items(),
                        key = lambda t: t[1],
                        reverse=True):
    print(make, cnt)
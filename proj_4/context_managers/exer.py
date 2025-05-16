import decimal 
import sys 
from time import perf_counter, sleep
print(decimal.getcontext())

class precision:
    def __init__(self, prec):
        print("INIT")
        self.prec = prec
        self.current_prec = decimal.getcontext().prec
        
    def __enter__(self):
        print("inside enter")
        decimal.getcontext().prec = self.prec
        
    def __exit__(self, exc_type, exc_value, exc_tb):
        print("exit")
        decimal.getcontext().prec = self.current_prec
        return False
    
with precision(3):
    print(decimal.Decimal(1) / decimal.Decimal(3))    
print(decimal.Decimal(1) / decimal.Decimal(3))   

with decimal.localcontext() as ctx:
    ctx.prec = 3
    print(decimal.Decimal(1) / decimal.Decimal(3))    
print(decimal.Decimal(1) / decimal.Decimal(3))    

class Timer:
    def __init__(self):
        self.elapsed = 0
        
    def __enter__(self):
        self.start = perf_counter()
        return self
        
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.stop = perf_counter()
        self.elapsed = self.stop - self.start
        return False
    
with Timer() as timer:
    sleep(1)
print(timer.elapsed)

class OutToFile:
    def __init__(self, fname):
        self._fname = fname
        self._current_stdout = sys.stdout
        
    def __enter__(self):
        self._file = open(self._fname, 'w')
        sys.stdout = self._file
        
    def __exit__(self,exc_type, exc_value, exc_tb):
        sys.stdout = self._current_stdout
        self._file.close()
        return False
    
with OutToFile('test.txt'):
    print('Line 1')
    print('Line 2')
        
class Tag:
    def __init__(self, tag):
        self._tag = tag
        
    def __enter__(self):
        print(f'<{self._tag}>', end = '')
        
    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f'</{self._tag}>', end = '')
        return False

with Tag('p'):
    print('some ', end = '')
    with Tag('b'):
        print('bold', end = '')
    print(' text', end='')

      
class ListMaker:
    def __init__(self, title, prefix='- ', indent=3):
        self._title = title
        self._prefix = prefix
        self._indent = indent
        self._current_indent = 0
        print(title)
        
    def __enter__(self):
        self._current_indent += self._indent
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self._current_indent -= self._indent
        return False
    
    def print_item(self, arg):
        s = ' ' * self._current_indent + self._prefix + str(arg)
        print(s)        

lm = ListMaker('Items')
with lm:
   lm.print_item('Item 1')
   with lm:
       lm.print_item('Itema 1')
       lm.print_item('Itema 1')
   lm.print_item('Item 2') 
     
     
# Generators and Context Managers
def open_file(fname, mode):
    f = open(fname, mode)
    try :
        yield f
        
    finally:
        f.close()
        
 
def my_gen():
    try:
        yield [1,2,3,4] 
    finally:
        print('exiting context and cleaning up')
        
gen = my_gen()
lst = next(gen)

try:
    next(gen)
except StopIteration:
    pass

class GenCtxManager:
    def __init__(self, gen_func):
        self._gen = gen_func()
        
    def __enter__(self):
        return next(self._gen)

    def __exit__(self, exc_type, exc_value, exc_tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False

with GenCtxManager(my_gen) as obj:
    print(obj)
    
class GenCtxManager:
    def __init__(self, gen_func, *args, **kwargs):
        self._gen = gen_func(*args, **kwargs)
        
    def __enter__(self):
        return next(self._gen)

    def __exit__(self, exc_type, exc_value, exc_tb):
        try:
            next(self._gen)
        except StopIteration:
            pass
        return False

def open_file(fname, mode):
    f = open(fname, mode)
    try:
        print('opening file ...')
        yield f
    finally:
        print('closing file...')
        f.close()
        
with GenCtxManager(open_file, 'test.txt', 'w') as f:
    f.writelines('TESING....')
    
with GenCtxManager(open_file, 'test.txt', 'r') as f:
    print(f.readlines())
    
# Decoring Generator Functions
     
def open_file(fname, mode = 'r'):
    print('opening file...')
    f = open(fname, mode)
    try:
        yield f
    finally:
        print('closing file...')
        f.close()
        
class GenContexManager:
    def __init__(self, gen):
        self.gen = gen
        
    def __enter__(self):
        return next(self.gen)
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        try:
            next(self.gen)
        except StopIteration:
            pass
        return False
    
file_gen = open_file('test.txt', 'w')
with GenContexManager(file_gen) as f:
    f.writelines('hehehehe')
    
def context_manager_Dec(gen_fn):
    def helper(*args, **kwargs):
        gen = gen_fn(*args, **kwargs)
        ctx = GenContexManager(gen)
        return ctx
    return helper

@context_manager
def open_file(fname, mode):
    f = open(fname, mode)
    try :
        yield f
        
    finally:
        f.close()
        
with open_file('test.txt') as f:
    f.readlines()
    
# build in decorator
from contextlib import contextmanager
@contextmanager
def open_file(fname, mode):
    f = open(fname, mode)
    try :
        yield f
        
    finally:
        f.close()
        
with open_file('test.txt') as f:
    f.readlines()

@contextmanager 
def timer():
    stats = dict()
    start = perf_counter()
    stats['start']  =start
    try:
        yield stats
    finally:
        end = perf_counter()
        stats['end'] = end
        stats['elapsed'] = end - start
        
with timer() as stats:
    sleep(2)
    
@contextmanager
def out_to_file(fname):
    current_stdout = sys.stdout
    file = open(fname, 'w')
    sys.stdout = file
    try:
        yield None
    finally:
        file.close()
        sys.stdout = current_stdout
        
with out_to_file('test.txt'):
    print('line 1')
    print('line 2')
    
from contextlib import redirect_stdout #doesnot require the filename , something like an object

with open('test.txt', 'w') as f:
    with redirect_stdout(f):
        print('LOOK on the success')
        
        
 
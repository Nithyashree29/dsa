def logged(fn):
    from functools import wraps
    from datetime import datetime, timezone
    
    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print('{0}: called {1}'.format(run_dt, fn.__name__))
        return result 
    return inner

#+
@logged
def func_1():
    pass

def func_2():
    pass

def timed(fn):
    from functools import wraps
    from time import perf_counter
    
    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print('{0} ran for {1:.6f}s'.format(fn.__name__, end-start))
        return result
    
    return inner

# @logged or you can use both or individually
@timed 
def fact(n):
    from operator import mul
    from functools import reduce
    
    return reduce(mul, range(1, n+1))
        
print(fact(4))

# fact = logged(timed(fact))
# fact(9)

def dec_1(fn):
    def inner():
        print('Running dec_1')
        return fn()
    return inner

def dec_2(fn):
    def inner():
        print("Running dec_2")
        return fn()
    return inner

@dec_1
@dec_2
def my_func():
    print("Running my_func")
    
my_func()

# Decorator Application (Memoization) - Is something that allows you to do a cache of the value of functions, functionss, return values based on input params
def fib(n):
    print('Calculating fib(0)'.format(n))
    return 1 if n<3 else fib(n-1) * fib(n-2)

class Fib:
    def __init__(self):
        self.cache = {1: 1, 2: 1}
        
        
    def fib(self, n):
        if n not in self.cache:
            print("Calculating fib{0}".format(n))
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
            
        return self.cache[n]
f = Fib()
print(f.fib(10))    
    
def fib():
    cache = {1: 1, 2: 1}
    
    def calc_fib(n):
        if n not in cache:
            cache[n] = calc_fib(n-1) + calc_fib(n-2) 
        return cache[n]
    return calc_fib

f = fib()
print(f(10))     

        
def memorize(fib):
    cache = {1: 1, 2: 1}
    
    def inner(n):
        if n not in cache:
            cache[n] = fib(n)
        return cache[n]
    
    return inner

@memorize
def fib(n):
    print('Calculating fib({0})'.format(n))
    #return 1 if n <2 else fib(n-1) + fib(n-2)
    return 1 if n <2 else n * fib(n-1)

print(fib(6))
print(fib(7))

from functools import lru_cache

@lru_cache
def fib(n):
    return 1 if n < 2 else fib(n-1) * fib(n-2)

@lru_cache(maxsize=8)
def fib(n):
    return 1 if n < 2 else fib(n-1) * fib(n-2)

print(fib(10))
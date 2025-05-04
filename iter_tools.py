# things known - iter, reversed, next, len, slicing, zip, filter, sorted, enumerate, min, max, sum, all, reduce etc...
# iter_tools_module - very usefull functions that allows us to work iterators and iterables
# slicing - isslice
# selecting and filtering - dropwhile, takewhile, compress, filterfalse
# chaining and teeing - chain, Tee 
# mapping and reducing - starmap, accumulate
# infinite iterators - count, cycle, repeat
# zipping - zip_longest
# combinations - product, permutations, combinations, combinations_with_replacement

from itertools import chain


l1  = [1,2, 3]
l2 = [4,5,6,7]
l3 = [7,8,9]
lists = [l1,l2,l3]
for item in chain(*lists):
    print(item)
    
def squares():
    yield (i**2 for i in range(4))
    yield (i**2 for i in range(4, 8))
    yield (i**2 for i in range(3, 12))
    
print("heyyyyy", *squares())

for item in chain(*squares()):
    print(item,'\n')
    
c = chain.from_iterable(squares())
for item in c:
    print(item)
    
def chain_iterables(*iterables):  #variable number of arguments
    for iterable in iterables:
        yield from iterable
        
def chain_from_iterable(iterable): #single argument
    for item in iterable:
        yield from item

for item in chain_from_iterable(squares()):
    print(item)
    
for item in chain_iterables(*squares()):
    print(item)
    
print(squares())
print(*squares())


from itertools import tee

#  Mapping - Applying a callable to each element of an iterable.
# map(fn, iterable)
# Accumulkation - Reducing an iterable down to a single value
# sum(iterable)  
# reduce(fn, iterable, [initializer])

# starmap - it unpacks every sub element of the iterable argument, and passes that to the map function.
# itertools.zip_longest(*args, [fillvalue = None])
  


      
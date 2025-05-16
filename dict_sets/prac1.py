# ss 
# Hash Function - A hash function is a function that maps from a set of arbitary size to another set of fixed size (range)
# h: D -> R where X(R) < X|(D)
# for our hash tables, we'll also want :
# 1. The range to be defined subset of the non-negative integers.
# 2. The generated indices for expected input values to be uniformly distributed as much as possible.
     
# If an object is hashabble:
#     The hash of the object must be an integer value.
#     if two objects compare equal, the hashes must also be equal.
#     None- Two objuects that do not compare equal may still have the same hash.
    
print(hash((1,2,3)))

class Number:
    def __init__(self, x):
        self.x = x
    
    def __eq__(self, other):
        if isinstance(other, Number):
            return self.x == other.x
        else:
            return False
        
    def __hash__(self):
        return 100 

  
"""
We need to create a Polygon class with the following properties
1. Number of vertices n - passed to the initializer
2. circumradius R - passed to the initializer
3. number of edges
4. number of sides
5. interior angle (in degrees)
6. apothem
7. surface area
8. perimeter
9. supports equality based on number of vertices and circumradius
10. supports > based on number of vertices
"""

import math
import random


class Polygon:
    def __init__(self, n, R):
        self._n = n
        self._R = R
        
    def __repr__(self):
        return f'Polygon(n={self._n}, R={self._R})'
    
    @property
    def count_vertices(self):
        return self._n
    
    @property
    def count_edges(self):
        return self._n

    @property
    def circumradius(self):
        return self._R
    
    @property
    def interior_angle(self):
        return (self._n - 2) * 180 / self._n
    
    @property
    def side_length(self):
        return 2 * self._R * math.sin(math.pi / self._n) 
    
    @property
    def apothem(self):
        return self._R * math.cos(math.pi / self._n)
    
    @property
    def area(self):
        return self._n / 2 * self.side_length * self.apothem
    
    @property 
    def perimeter(self):
        return self._n * self.side_length
    
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return (self.count_edges == other.count_edges
                    and self.circumradius == other.circumradius)
        else:
            return NotImplemented
            
    def __gt__(self, other):
        if isinstance(other, Polygon):
            return self.count_vertices == other.count_vertices
        else:
            raise NotImplemented
        
                
    

assert 1 == 1
def test_polygon():
    n = 3
    R = 1
    p = Polygon(n, R)
    assert str(p) == f'Polygon(n=3, R=1)', f'actual: {str(p)}'
    assert p.count_vertices == n, (f'actual: {p.count_vertices}, '
                                   f' expected: {n}')
    assert p.count_edges == n
    assert p.circumradius == R
    # assert math.isclose(p.interior_angle, 150)
    # assert math.isclose(p.area, 27,
                        # rel_tol = rel_tol,
                        # abs_tol = abs_tol), (f'actual: {p.area}, '
                                        #    f' expected: {2.0}')
                        
    p1 = Polygon(3, 19)
    p2 = Polygon(15, 100)
    #assert p2 > p1
    #assert p2 == p1 
    
test_polygon()

# As you should be aware, comparing floats is not equality is not something we should do.
# Instead, we are going to use the math modules is_close function with relative and absolut tolerances set o 0.001. 

class Polygons:
    def __init__(self, m, R):
        if m < 3:
            raise ValueError('m must be greater than 3')
        self._m  = m
        self._R = R
        self._polygons = [Polygon(i, R) for i in range(3, m+1)]
        
    def __len__(self):
        return self._m - 2

    def __repr__(self):
        return f'Polygons(m={self._m}, R={self._R})'
    
    def __getitem__(self, s):
        return self._polygons[s]
    
    @property
    def max_efficiency_polygon(self):
        sorted_polygons = sorted(self._polygons,
                                 key = lambda p: p.area/p.perimeter,
                                 reverse=True)
        return sorted_polygons[0]
    
p = Polygons(4, 2)
print(p)
print(p._polygons)

class RandomNumbers:
    def __init__(self, length, *, range_min=0, range_max=10):
        self.length = length
        self.range_min = range_min
        self.range_max = range_max
        self.num_requested = 0
        
    def __len__(self):
        return self.length
    
    def __next__(self):
        if self.num_requested >= self.length:
            raise StopIteration
        else:
            self.num_requested += 1
            return random.randint(self.range_min, self.range_max)
       
    def __iter__(self):
        return self
        
numbers = RandomNumbers(3)
print(next(numbers))

class Square:
    def __init__(self, length):
        self.length = length
        self.i =0 
    
    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result
       
    def __iter__(self):
        return self

sq = Square(5)
for item in sq:
    print(item)
    
print(list(enumerate(sq)))
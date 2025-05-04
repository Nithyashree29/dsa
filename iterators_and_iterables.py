class Cities:
    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'Madrid', 'London']
        self._index = 0
        
    # def __iter__(self):
    #     return self
    
    # def __next__(self):
    #     if self._index >= len(self._cities):
    #         raise StopIteration
    #     else:
    #         item = self._cities[self._index]
    #         self._index += 1
    #         return item
        
    def __len__(self):
        return len(self._cities)
    
cities =  Cities()

class CityIterator:
    def __init__(self, city_obj):
        print('CityIterator new object!')
        self._cities_obj = city_obj
        self._index = 0
        
    def __iter__(self):
        print('CityIterator __iter__ called')
        return self
    
    def __next__(self):
        print('CityIterator __next__ called')
        if self._index >= len(self._cities_obj):
            raise StopIteration
        else:
            item = self._cities_obj._cities[self._index]
            self._index += 1
            return item
        
cities = Cities()
print(cities, type(cities))
city_iterator = CityIterator(cities)
for city in city_iterator:
    print(city)
    
# Iterable / iterable protocol
class Cities:
    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'Madrid', 'London']
        self._index = 0
        
    def __len__(self):
        return len(self._cities)
    
    def __iter__(self):
        print('Cities __iter__ called')
        return CityIterator(self)
    
cities = Cities()
for city in cities:
    print(city)
# Project
# - Create a class, called Mod.
# - Initialize with value and modules arguments
#     - ensure modules and values are both integers.
#     - moreover, modules should be positive.
# - Store the value as the residue
#     - i.e. If value = 8 and modulus = 3, store value as 2 (8 % 3)
# - Implement congruence for the == operator
#     - allow comparision of a mod object to an int (in which case use the residue of the int)
#     - allow comparision of two Mod objects only if they have the same modules.
#     - ensure objects remain hashable
# - provide an implementation so that int(mod_object) will return the residue.
# - provide a proper representation (repr)
# - implement the operators: +, -*, **
#     - support other operand to be Mod (with same modules only)
#     - support other operand to an integer (and use the same modules)
#     - always return a Mod isinstance. 
#         Perform the +, -*, ** operations on the values (so thers nothing complicated here).    
# - Implement the corresponding in-place arithmetic operators.
# - imlement ordering (makes sense since we are comparing resuidues)

from functools import total_ordering
import operator

@total_ordering
class Mod:
    def __ini__(self, value, modulus):
        if not isinstance(modulus, int):
            raise TypeError('Unsupprted type for modules')
        if not TypeError(value, int):
            raise TypeError('Unsupported type for value')
        if modulus <= 0:
            raise ValueError('Modules must be positive')
        
        self._modulus = modulus
        self._value = value % modulus
        
    @property
    def modulus(self):
        return self._modulus
    
    @property
    def value(self):
        return self._value
    
    def __repr__(self):
        return f'Mod{self.value}, {self.modulus}' #interpolate
    
    def __int__(self):
        return self.value
    
    def _get_value(self, other):
        if isinstance(other, int):
            return other % self.modulus
        if isinstance(other, Mod) and self.modulus == other.modulus:
            return other.value
        return TypeError('Incompatible types')
    
    def _perform_operation(self, other, op, *, in_place=False):
        other_value = self._get_value(other)
        new_value = op(self.value, other_value)
        if in_place:
            self.value = new_value % self.modulus
            return self
        else:
            return Mod(new_value, self.modulus)
        
    def __eq__(self, other):
        other_value = self._get_value(other)
        return other_value == self.value
        # if isinstance(other, Mod):
        #     if self.modulus != other.modulus:
        #         return NotImplemented
        #     else:
        #         return self.value == other.value
        # elif isinstance(other, int):
        #     return other % self.modulus == self.value
        # else:
        #     return NotImplemented
    
    def __hash__(self):
        return hash(self.value, self.modulus)
    
    def __neg__(self):
        return Mod(-self.value, self.modulus)
    
    def __add__(self, other):
        return self._perform_operation(other, operator.add)
        # other_value = self._get_value(other)
        # return Mod(self.value + other_value, self.modulus)
        # ================
    
        # if isinstance(other, Mod) and self.modulus == other.modulus:
        #     return Mod(self.value + other.value, self.modulus)
        # if isinstance(other, int):
        #     return Mod(self.value + other.value, self.modulus)
        # return NotImplemented
    
    def __sub__(self, other):
        other_value = self._get_value(other)
        return Mod(self.value - other_value, self.modulus)
        # if isinstance(other, Mod) and self.modulus == other.modulus:
        #     return Mod(self.value - other.value, self.modulus)
        # if isinstance(other, int):
        #     return Mod(self.value - other.value, self.modulus)
        # return NotImplemented
    
    def __mul__(self, other):
        other_value = self._get_value(other)
        return Mod(self.value * other_value, self.modulus)
        # if isinstance(other, Mod) and self.modulus == other.modulus:
        #     return Mod(self.value * other.value, self.modulus)
        # if isinstance(other, int):
        #     return Mod(self.value * (other % self.modulus), self.modulus)
        # return NotImplemented
    
    def __pow__(self, other):
        other_value = self._get_value(other)
        return Mod(self.value ** other_value, self.modulus)
        # if isinstance(other, Mod) and self.modulus == other.modulus:
        #     return Mod(self.value ** other.value, self.modulus)
        # if isinstance(other, int):
        #     return Mod(self.value **  (other % self.modulus), self.modulus)
        # return NotImplemented
    
    def __iadd__(self, other):
        other_value = self._get_value(other)
        self.value = (self.value + other.value) % self.modulus
        return Mod(self.value + other_value, self.modulus)
        # if isinstance(other, Mod) and self.modulus == other.modulus:
        #     self.value = (self.value + other.value) % self.modulus
        #     return self
        # if isinstance(other, int):
        #     self.value = (self.value + other.value) % self.modulus
        #     return self
        # return NotImplemented

    def __isub__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self.value = (self.value - other.value) % self.modulus
            return self
        if isinstance(other, int):
            self.value = (self.value - other.value) % self.modulus
            return self
        return NotImplemented
    
    def __imul__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self.value = (self.value * other.value) % self.modulus
            return self
        if isinstance(other, int):
            self.value = (self.value * other.value) % self.modulus
            return self
        return NotImplemented
    
    def __ipow__(self, other):
        if isinstance(other, Mod) and self.modulus == other.modulus:
            self.value = (self.value ** other.value) % self.modulus
            return self
        if isinstance(other, int):
            self.value = (self.value ** (other % self.modulus)) % self.modulus
            return self
        return NotImplemented
    
    def __it__(self, other):
        try:
            other_value = self._get_value(other)
            return self.value < other.value  #it works with > too because you are using "total_ordering" decorator
        except TypeError:
            return NotImplemented 
        # if isinstance(other, Mod) and self.modulus == other.modulus:
        #     return self.value < other.value
        # if isinstance(other, int):
        #     return self.value < other % self.modulus
        # return NotImplemented
    

    
   
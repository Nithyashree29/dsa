#Strings, Character, Charecter Array
# String - it is a class that holds a character array inside, wrapped inside a double quote and underneath we have a array, and this array has a dataype of character. In java the string is immutable
# List, dict, set -> mutable; tuple, string, frozenset, int, float, bool None -> Immutable
# ascii(American standard code for information interchange) val for 'a' - 97 
s  = 'nithya'
# s = s+'j' -> takes more time, s += 'j' -> significantly lesser amount of time 
def reverseString(val):
    return val[::-1]

print(reverseString('nithya'))

def reverse1(val):
    n = len(val)
    dup = [0] *n
    for i in range(n):
        dup[n-i-1] = val[i]
    return ' '.join(dup)

def opt_reverseString(text):
    char = s.strip().split()
    left, right = 0, len(char)-1
    while left < right:
        char[left], char[right] = char[right], char[left]
        left +=1
        right -= 1
    return ''.join(text)       
                    
            
def reverse_2(text):
    rev_text = ""
    for char in text:
        rev_text = char + rev_text
    return rev_text 
 
def palindrome(s):
    left = 0
    right = len(s) - 1
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    return True

                                                                                                                                                                                     
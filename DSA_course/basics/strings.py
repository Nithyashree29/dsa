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
 
def opt_reverseString(char):
    char = char.strip().split()
    left, right = 0, len(char)-1
    while left < right:
        char[left], char[right] = char[right], char[left]
        left +=1
        right -= 1
    return ''.join(char)       
                    
            
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

#Given s atring s, representing a large integer, the task is to return the largest-values odd integer(as a string) that is the substring of the given string s . the number returned should not have leading sero's. Bute the given input string may have leading sero.
#Using sub-string is a better option 
def largestOddNumber(s):
    ind = -1
    i = 0
    for i in range(len(s)-1, -1, -1):
        if (int(s[i]) % 2) == 1:
            ind = i
            break
        
    i = 0
    while i < ind and s[i] == '0':
        i += 1
    return s[i:ind+1]  #TC - O(N), SC - O(1)


def longestCommonPrefix(arr):  #  sort it for better, and compare first and last
    if not arr:
        return ""
    arr.sort()
    first = arr[0]
    last = arr[-1]
    ans = []
    for i in range(min(len(first), len(last))):
        if first[i] != last[i]:
            return ''.join(ans)
        ans.append(first[i])
    return ''.join(ans)


       
                                                                                                                                                                              
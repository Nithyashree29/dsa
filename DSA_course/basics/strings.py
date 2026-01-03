#Strings, Character, Charecter Array
# String - it is a class that holds a character array inside, wrapped inside a double quote and underneath we have a array, and this array has a dataype of character. In java the string is immutable
# List, dict, set -> mutable; tuple, string, frozenset, int, float, bool None -> Immutable
# ascii(American standard code for information interchange) val for 'a' - 97 
from collections import Counter


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
def isomorphic(s, t): #Given two strings s and t are isomorphic if the characters in s can be replaced to get t, All occurences of a character must be replaced with another character while preserving the order of characters, No two characters may map to the same character, but a character may map to itself.
    smap = [0] * 256, tmap = [0] * 256
    n = len(s)
    for i in range(n):
        if smap[ord(s[i])] != tmap[ord(t[i])]:
            return False
        smap[ord(s[i])] = i+1
        tmap[ord(t[i])] = i+1
    return True    #TC - O(n), SC - O(1)
# Why index+1? Because index starts from 0, and 0 is the initial value meaning "not seen yet". Using i+1 ensures we never store 0 as a valid seen index.
def isIsomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    
    map_s_to_t = {}
    map_t_to_s = {}
    
    for i in range(len(s)):
        char_s, char_t = s[i], t[i]
        
        if char_s in map_s_to_t:
            if map_s_to_t[char_s] != char_t:
                return False
        else:
            map_s_to_t[char_s] = char_t
        
        if char_t in map_t_to_s:
            if map_t_to_s[char_t] != char_s:
                return False
        else:
            map_t_to_s[char_t] = char_s
    
    return True    

def rotate_string(s, goal): #Given two strings a and goal , return if and only if s can become goal after some number of shifts on S. Ashift on s consists of moving character of s to the rightmost position.Ex if s = 'abcde' then it will be 'bcdea' after on shift
    #brrotforce approach
    left = ""
    for i in range(len(s)-1):
        right = s[i:]
        if right + left == goal:
            return True
        left += s[i]
    return False   # TC - O(n2), SC = O(n) * 2
def rotate(s, goal):
    # find/in -> internally uses Rabin karp Algorithm 
    if len(s) != len(goal):
            return False
    doubled_s = s + s
    return goal in doubled_s
        
def anagram(s, t):   #Given two strings s and t, return true if its is an anagram of s, a wors or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly one.
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)


def sort_char_by_freq():   #Given string return the array of unique charaters, sorted by highest to lowest occuring characters, if two or more have same frequency then arrange them in alphabetic order.
    if not s:
        return ""
    freq = Counter(s)
    sorted_char = sorted(freq.keys(), key = lambda x: (-freq[x], x))
    return ''.join(sorted_char)
        
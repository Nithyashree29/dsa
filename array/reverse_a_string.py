# Reverse a string - Hi my name is nithya
from typing import List
def reverse_string(val: str):
    if type(val) != str or len(val) < 2:
        raise ValueError("Please enter a valid string")
    
    arr = list(val) #O(n)
    reversed_string = arr[::-1] #O(n)
    val = ''.join(reversed_string) #O(n)
    print(val)

def reverse_string1(val: str):
    char_arr = list(val)
    left, right = 0, len(char_arr) -1
    while left < right:
        char_arr[left], char_arr[right] = char_arr[right], char_arr[left]
        left+=1
        right-=1
    return ''.join(char_arr)

def rev3(val:str):
    arr = list(val)
    rev_str = list(reversed(val))
    print(''.join(rev_str))

def rev4(val: str):
    reverse_str = ''
    for i in range(len(val)-1, -1,-1):
        reverse_str+=val[i]
    print(reverse_str)


def merge_sorted_array(arr1:List, arr2:List): #[0,1,4,5, 89] [3,6,7,45]
    # if not sorted opr one arr is given 
    #  len(Arr)//2, la = arr[:mid], ra = arr[mid:]
    arr =[]
    i = 0
    j = 0
    if len(arr1) == 0:
        return arr2
    if len(arr2) == 0:
        return arr1
    
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1
    return arr
print(reverse_string1("HI MY NAME IS STAR"))
print(rev3("ashjdfb kjahdia kadhsi"))
print(rev4("ashjdfb kjahdia kadhsi"))
print(merge_sorted_array([0,1,4,5,89], [3,6,7,45]))
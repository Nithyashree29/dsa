# Hashing - Hashing is a technique used in computer science to quickly find, store, and manage data. It works by taking an input, like a number or a staring and converting it into a fixed-size value calles a hash. This hash then points to wqhere the data is atored in a structure cal;led hash table. The main goal os hashing is to make data retrieval fast, even when dealing with large amounts of information, Hashing is widely used in carious applications, such as searching databases, managing passwords, and speeding up data lookups in many types of software.
# Note - (Number hashing)if you want to declare the array datya structure to hash the values if you are declaring it inside main in that case the largest number could be 10 to the power 6 only. Outside the maib which is global variable (ousiude int main()) you ca declare as big as 10 power 7 in case of int, In case of boolean you could go as large as 10 ower 8.
def hash_int(arr):
    hash_table = [0] * 10
    for i in arr:
        hash_table[i] += 1
    return hash_table

print(hash_int([2,3,4,6,9,9,9,9,9,9])[9])
# Charecter Hashing - Every charecter has the ascii value associated with it. Typrcast and then print
# Note : 1sec = 10^8 operations, for more number it will lead to time limit exceeded (TLE)
def char_hash(arr):
    hash_table= [0] * 26
    for char in arr:
        index = ord(char) - ord('a')
        hash_table[index] += 1
    return hash_table

def char_str(arr):
    freq = {}
    for s in arr:
        if s in freq:
            freq[s] += 1
        else:
            freq[s] = 1
            
             
    
print(char_hash(['a', 'b']))

#hash map - O(1) best case
            # O(N) worst case, collisions.
#tree map ->  O(log N) always, always try to use hashmap in case of TLB use tree map.
# How stl's or collections implemented internally? - Division method. folding method, mig square method.

# In division method remember collision happens lets say we have [21, 25, 36, 52, 28] and if you hypothetically modulo the number by prime number 7 then collision happens. (same num pointing to the same index)
# This is when something like chaining comes in -

def highest_occuring_element(arr):               #TC -O(N2), SC = O(N)
    n = len(arr)
    masFreq = 0
    maxEle = 0
    visited = [False] * n
    for i in range(n):
        if visited[i]:
            continue
        freq = 0
        for j in range(i, n):
            if nums[i] == nums[j]:
                ferq += 1
                visited[j] = True
        if freq > maxFreq:
            masFreq = Freq
            maxEle = nums[i]
        elif freq == maxFreq:
            masEle = min(maxEle, nums[i])
            































    










        

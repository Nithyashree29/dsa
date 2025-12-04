#✈️# Hashing - Hashing is a technique used in computer science to quickly find, store, and manage data. It works by taking an input, like a number or a staring and converting it into a fixed-size value calles a hash. This hash then points to wqhere the data is atored in a structure cal;led hash table. The main goal os hashing is to make data retrieval fast, even when dealing with large amounts of information, Hashing is widely used in carious applications, such as searching databases, managing passwords, and speeding up data lookups in many types of software.
# Note - (Number hashing)if you want to declare the array datya structure to hash the values if you are declaring it inside main in that case the largest number could be 10 to the power 6 only. Outside the maib which is global variable (ousiude int main()) you ca declare as big as 10 power 7 in case of int, In case of boolean you could go as large as 10 ower 8.
from collections import Counter
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

def highest_occuring_element(nums):               #TC -O(N2), SC = O(N), Brute force approach
    n = len(nums)
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
            maxFreq = Freq
            maxEle = nums[i]
        elif freq == maxFreq:
            masEle = min(maxEle, nums[i])
    return None


def optimized_approach(arr):
    maxi = arr[0]
    hash_table = [False] * len(arr)
    for i in range(len(arr)):
        maxi = max(maxi, arr[i])
    hash_table[maxi+1] = [0]
    
# def max_element(arr):
#     hash_table = [False] * len(arr)
#     maxi = 0
#     for i in range(len(arr)):
#         if hash_table[arr[i]]:
#             hash_table[arr[i]] += 1
#         else:
#             hash_table[arr[i]] = 1
#         maxi = max(maxi, arr[i])
#     return maxi, hash_table, hash_table[maxi])
    
# Note - In map in all cases it takes O(log N), Best , average and worst aswell, and is ordered.
# Unordered map - besta nd average  o[1], O(N) in worst case when lot of collisions happening.
# tree map - always O(log N).
# Internally all these are implemented using 
    # Division Method - mod(num) and reminder will be like the index value for it, there is a chance of collision and that is when chaining comes into picture. (When ypur formula ends up pointing same index then collision happens) and dicision implements chaining Internally along with the sorted order and individual chains will be very very small and it might use binary search etc to search and fetch results.
        # TC - o(1).
    # Folding Method
    # Mid Square Method
def mostFrequentElement(nums):
    if not nums:
        return -1
    count = Counter(nums)
    max_freq = max(count.values)
    val = [num for num, freq in count.items() if freq == max_freq]
    return min(val)

def mostFrequentElement(nums):
    if not nums:
        return -1
    freq = {}
    max_count = 0
    result = float('inf')

    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > max_count:
            max_count = freq[num]
            result = num
        elif freq[num] == max_count and num < result:
            result = num
    return result

def secondMostFrequent(nums):
    count = Counter(nums)
    if len(count) < 2:
        return -1
    return count.most_common(2)[1][0]


def secondMostFrequent(nums):    #need to debug
    if len(nums) < 2:
        return -1
    freq = {}            #Hash Map
    first_count = second_count = 0
    first_num = second_num = float('inf')

    for num in nums:
        freq[num] =  freq.get(num, 0) + 1
        count = freq[num]

        if count > first_count:
            #promote current to first , old first becomes second
            if num != first_num:
                second_count = first_count
                second_num = first_num
            first_count = count
            first_num = num
        elif count > second_count:
            second_num = num
            second_count = count
        elif count == first_count and num < first_num:
            #tie for first -> keep smaller numder
            first_num = num
        elif count == second_count and num < second_num:
            second_num = num

    return second_num if second_count >0  else -1        #TC -O(n) SC - O(k)
    
        





















    










        

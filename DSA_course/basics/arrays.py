#ARRAY - All the elements should have the same data type. The memory block is not scatterd, they are contigious.
# Traversing an 1D array - going through each element of an array.

def sum_of_array(n):
    s = 0
    for i in range(n):
        s += n[i]
    return s

def recursive_sum(arr, left):
    if left > len(arr):
        return 0
    return arr[left] + recursive_sum(arr, left+1 ) #TC - O(N), SC - O(N)
    
def count_odd(arr):
    count = 0
    for num in arr:
        if num%2!=0:
            count += 1
    return count


def arraySortedOrNote(arr, n):
    for i in range(n-1):
        for j in range(i+1, n):
            if arr[i] > arr[j]:
                return False
    return True

def reverse_array(arr, n):   #make the change within the array, pass by reference 
    temp = [0]*n
    for i in range(n-1, -1,-1):
        temp[n-i-1] = arr[i]
        
    for j in range(n):
        arr[i]= temp[i]
        
    return                          #TC - O(N)*2  SC = O(N)

def two_pointer_apaproach(arr, n):   #swap using three variable function
    # left = 0, right =  n-1, temp = 0
    # while(left< right):
    #     for i in range(n):
    #         for j in range(n-1, -1, -1):
    #             temp = arr[i]
    #             arr[i] = arr[j]
    #             arr[j] = temp
    if n ==0:
         return
    endPtr = n-1
    print([i for i in range(0, n//2)])
    for i in range(0, n//2):
        print(arr, i)
        arr[i], arr[endPtr] = arr[endPtr], arr[i]
        endPtr = endPtr - 1

arr =[3,4,5,6,8,9,9]    
two_pointer_apaproach(arr, 7)
print(arr)

def sorted_1(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    return False                    #TC - O(N), SC - O(1)


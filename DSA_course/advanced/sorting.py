# Selection - select minimum and swap.The selection sort algorithm sorts and array by repeatedly finding the minimum element from  the unsorted part and putting it at the beginning . The largest element will end up at the last index of an array.
class Solution():
    def selectionSort(self, nums):
        for i in range(len(nums)-1):
            min_index = i 
            for j in range(i+1, len(nums)):
                if nums[j] < nums[min_index]:
                    min_index = j
            if min_index != i:
                nums[i], nums[min_index] = nums[min_index], nums[i]
        return nums  
# TC - O(N2), SC - O(1) as it is an in-place sorting algorithm and deos not require additional storage proportional to the imput size.

# Bubble sort - The bubble sort algorithm sorts an array by repeatedly swapping adjacent elements if they are in the wrong. The largest elements "bubble" to the end of the arary with each pass.
    def bubbleSort(self, nums):
        n = len(nums)
        for i in range(n-1, -1, -1):
            isswapped= False
            for j in range(i):
                if nums[j] > nums[j+1]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
                    isswapped =True
            if not isswapped:
                break
        return nums
#TC - O(N2), O(N) for the best case, SC - O(1), because bubble sort is ain in-place sorting algorithm
    
#Insertion Sort - Insertion sort builds array one element at a time by repeatedly picking the next element and inserting it into its correct position within the already sorted part of the array.

    def insertionSort(self, nums):
        n = len(nums)
        for i in range(1, n):
            key = nums[i]
            j = i - 1
            
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
            
        return nums
# TC - O(N2), SC - O(1)

# MergeSort -  Is a powerful sorting algorithm that follows the divide and conquer approach.The array is divided into two equal halves until each sub-array contains only one element, Each pair of smaller sorted ararys is then merged into a larger sorted array.
# The algorithm consists of two main functions :
#     merge() - This function merges the two halves of the arraym, assuming both parts are already sorted.
#     mergeSort() -  This function divides the array into 2 parts, how to mid an dmid+1 to high where, low is the leftmost index of the arary, high iss the rightmost index of the arary, and mid is the middle index of the array.
    
        
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
    
    
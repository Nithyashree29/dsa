# list1 = [1,2,3]
# list2 = [3,4,5]
# for i in list1:
#     for j in list2:
#         if i == j:
#             print(True)

# O(a*b) - since the size of the array is different 
# O(1) - Space Complexity

def find_array_element(list3, list4):
    #  Steps babe
    #  loop through first array and create object, where properties === items in the array
    #  Loop through second array and check if iten in second array exists on the created object.
    #  Can we assume always two parametrs in? how to test etc
    dict2 = {ele: True for ele in  list3}
    print(dict2)
    for ele2 in list4:
        if ele2 in dict2:
            print(ele2)
            return True
    return False
val = find_array_element([3,4,5], [7,8,9,4])
print(val)

#  You can use set since you are just dealing with member ship operations

def find_array_element2(arr1, arr2):
    set1 = set(arr1)
    # return any(ele in set1 for ele in arr2)
    for ele in arr2:
        if ele in set1:
            return True
    return False
# O(a+b)
# O(a) Space complexity

# What if the array is large ?, what if i have empty array, what if strings?
print(find_array_element2([3,5,6,7,8], ['null', 7, 8]))
# return(set(arr1) & set(arr2))
# lets say it flushes in memory and 
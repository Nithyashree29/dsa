# Given array = [2,5,2,2,3,5,1,2,4]
# should return 2

# Given Array = [2,1,1,2,3,4,1,2,4]
# should return 1

# Given Array = [2,3,4,5]
# should return undefined
               

def recurring_num(arr):
    if not arr:
        return "Undefined"

    count_dict = {}
    for i in arr:
        if i in count_dict:
            count_dict[i] += 1
        else:
            count_dict[i] = 1
    max_val = max(count_dict.values())
    # print(max_val)
    return {k:v for k,v in count_dict.items() if v == max_val}


print(recurring_num([2,3,5,7,3,2,45,7,2,7]))


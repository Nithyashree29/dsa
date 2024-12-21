counter = 0
def inception():
    global counter
    if counter > 3:
        return "Done"
    counter += 1
    return inception()
# print(inception())


def factorial(n):
    if n in [0,1]:
        return 1
    else:
        return n * factorial(n-1)

    
# print(factorial(7))
# print(factorial(2))


def fabinocci(n):
    if n < 2:
        return n
    return fabinocci(n-1) + fabinocci(n-2)
    
# # Carrot
# def reverse_string(value):
#     list1  = []
#     print("inside")
#     for i in range(0, len(value),-1):
#         print("inside loop")
#         print(i)

def reverse_string_iterative(str1):
    arrstr = str.split("")
    reverse_str = []
    
    def add_to_array(array):
        if len(array) >0:
            reverse_str.append(array.pop())
            add_to_array(array)
        
    add_to_array(arrstr)
    return ''.join(reverse_str)

def reverse_recursie(str1):
    if str1 == "":
        return ""
    return reverse_recursie(str1[1:] + str1[0])
 
def rec(value):
    return "".join(list(reversed(value)))

print(rec("carrot"))
# Recursion - When a function calls itself.
# The calls that has happend get recided in the stack space (recursive stack space), everything is kept in the memory. 
# If infinite recusrsion leads to Segmentation fault.
# Finite recursion - call the function itself and stop it according to the requirement
 
# Head Recursion - Recursive call occurs before any other processing logic, The function waits for the recursive call to return before proceeding with any operation
def head_recursion(n):
    if n>0:
        head_recursion(n-1)
        print(n, end= "")
# Tail Recursion - The recursive call is the last operation in the function. Omce the function calls itself, therte is no need to retain the current function's state , allowing the compiler to optimize tail recursion. There nothing left to do after it returns. The result can be returned directly.
def tail_recursion(n):
    if n==0:
        return
    print(n, end='')
    tail_recursion(n-1)
# StackOverflow/Seg-mentation call - If it goes infinite number of times and computer has no base condition met or  supposed to remember infinite originating points and thats when StackOverflow happenss.
# Recursion Tree - Same as the head or tail recursion 
# TC - O(N), SC - O(N)

# Parameterized recursion - based on the input params you control the base logic.
def func1(i, N):
    if i>N:
        return
    print(i)
    func1(i+1, N)
func1(1, 3)

def func1(N):
    if N==0:
        return
    func1(N-1)
    print(N)
    
sum = 0
def first_n_natural_number(i,n):
    
    if i > n:
        return
    sum = sum + i
    first_n_natural_number(i+1, n)
    print(sum)
    
def func_recursion(i, N):
    if i >N:
        return 0
    return i + func_recursion(i+1, N)
     
def func_recursion(N):
    if N == 0:
        return 0
    return N + func_recursion(N-1)

def fact_num(N):
    if N <= 1:
        return 1
    return N * fact_num(N-1)

def sum_arr(i, arr, N):
    if i > N:
        return 0
    return arr[i] + sum_arr(i+1, arr, N)

class Solution:
    def arrSum(self, nums):
        return self.sum(nums, 0)
    def sum(self, nums, left):
        if left >= len(nums):
            return 0
        return nums[left] + self.sum(nums, left+1)
    
def reverseString(l, r, str):
    if l > r:
        return str
    str[l], str[r] = str[r], str[l]
    return reverseString(l+1, r-1, str)

print(reverseString(0, 5, ['b','a','n','a','n','a']))

class Solution:
    def reverseString(s):
        def reverse(l,r, s):
            if l > r:
                return
            s[l], s[r] = s[r], s[l]
            reverse(l+1, r-1, s)
        reverse(0, len(s)-1, s)
        return"".join(s)
print(Solution.reverseString(['B', 'A', 'N', 'A']))
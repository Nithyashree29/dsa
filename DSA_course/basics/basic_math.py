import math

def count_digits(num):
    if num == 0:
        return 1
    cnt = 0
    while (num>0):
        num = num//10
        cnt = cnt+1
    return cnt
##print(count_digits(5627))

# can use log10(num) + 1

def count_odd_digits(num):
    cnt_odd = 0
    while (num >0):
       lstdigit = num%10
       if lstdigit%2 ==1:
           cnt_odd = cnt_odd+1
       num = num//10
    return cnt_odd

#print(count_odd_digits(890987))

def reverse_num(num):
    new_num =0
    while (num>0):
        ld = num % 10
        new_num  = (new_num * 10) + ld
        num = num//10
    return new_num

#print(reverse_num(345890))    #TC - O(log10num), SC  -  O(1)

def palindrome(num):
    new_num =0
    o_num = num
    while (num>0):
        ld = num % 10
        new_num  = (new_num * 10) + ld
        num = num//10
    if new_num == o_num:
        return True
    else:
        return False
#print(palindrome(1219))   #TC - O(log10num), SC  -  O(1)

def largest(n):
    ld = 0
    while(n>0):
        num = n % 10
        if num > ld:
            ld = num
        n = n //10
    return ld

#print(largest(34567890))  #TC - O(log10num), SC - O(1)

def factorial(n):  
    #Factorial of a number is the product of all positive integers less than or equal to that number
    if n==1 or n==0:
        return 1
    ans = 1
    for i in range(1, n+1):
        ans = ans * i
    return ans   
#print(factorial(5))   #TC - O(n), SC - O(1) (Because no external space only ans variable)


def cuntDigit(n):
    if n == 0:
        return 1
    count = int(math.log10(n)) + 1
    return count

def armstrong(n):  #armstrong number is a number which is equal to the sum of the dgits of the number, raised to the power of number of digits.
    
    count =  count_digits(n)
    sum = 0
    copy = n
    while n >0:
        ld = n % 10
        sum += pow(ld, count)
        n = n // 10
        
    if sum == copy:
        return True
    return False
        
#print(armstrong(153))   #Tc - O(log10(n)) SC - O(1)

def perfect_num(n):   #A perfect number is a number whose proer divisors(excluding he number itself) add up to the number iself
    sum = 0
    for i in range(1,n):
        if n % i == 0:
            sum += i
    return sum == n
  
#print(perfect_num(28)) #TC - O(N), SC- O(1)  
# number that are divisible are 1 n/1, 2 n/2, 3 n/3 etc.. end tat sqrt(n)

def perfectnum(n):
    #print(int(math.sqrt(n)))
    sum = 1 # a peroper divisor
    for i in range(2, n):
        if i*i < n:
            if n % i ==0:
                sum = sum+i
                if i!= (n/i):
                    sum = sum + (n/i)
        return sum == n 

print(perfectnum(5))    
 
def prime_number(n):       # A Prime number is a number which has no divisors except 1 and itself.
    if n == 1:
        return False
    for i in range(2, n):    #can just loop for sqrt only
        if n % i == 0: 
            return False
    return True

print(prime_number(5))               #TC - O(n), SC - O(1), can also apply sqrt logic

def primev2(n):
    cnt = 0
    for i in range(1, n+1):
        if n % i == 0:
            cnt += 1
    if cnt == 2:
        return True
    return False   

def count_primenumbers(n):
    count = 0
    for i in range(2, n+1):
        if primev2(i):
            count += 1
    return count
        
    
print(count_primenumbers(6))

def gcd(n1, n2):   # The greatest common divisor of two numbers is the largest positive integrer that divides both of the integers.
    lar = 1
    # for i in range (min(n1, n2)+1):   # better do backward traversal
    #     if (n1%i ==0) & (n2%i==0):
    #         if i < lar:range 
    #             lar = i
    for i in range(min(n1, n2)+1, 1, -1):
        if (n1%i ==0) & (n2%i==0):
            lar = i
            break
    return lar
print(gcd(60, 120))                 #TC = O(min(n1, n2)) SC = O(1)

# To optimize the above we can make use of Euclidean Algorithm 
# n1 > n2 , gcd (35, 10) = gcd (35-10, 10) , n2-n2%gcd == 0
def gc_euclidean(n1, n2):
    while (n1 !=0 & n2 !=0):
        if n1 > n2:
            n1 = n1 - n2
        else:
            n2 = n2 - n1
    if n2 == 0:
        return n1
    return n2     #takes lot of time

def gc_2(n1, n2):
    while(n1 != 0 & n2 != 0):
        if n1 > n2:
            n1 = n1  % n2 
        else:
            n2 = n2 % n1
    if n2 == 0:
        return n1
    return n2     #Tc O(log(N1, N2)), SC = 0(1)


def lcm(n1, n2):        #The lowest common muliple of two numbers is the lowest positive integer that is divisible by both the integer
    lcm = 0
    n = max(n1, n2)
    i = 1
    while True:
        mul = n * i
        if mul % n1 == 0 and mul % n2 == 0:
            lcm = mul
            break
        i+=1
    return lcm
print(lcm(4, 12))  # TC - O(N1 * N2) SC = O(1)

# Optimized approach N1 * N2 /gcd(N1 , N2)

def divisors(n):
    l1 = []
    for i in range(1,n+1):
        if n % i == 0:
            l1.append(i)
    return l1

print(divisors(6))def count_digits(num):
    if num == 0:
        return 1
    cnt = 0
    while (num>0):
        num = num//10
        cnt = cnt+1
    return cnt
#print(count_digits(5627))

# can use log10(num) + 1

def count_odd_digits(num):
    cnt_odd = 0
    while (num >0):
       lstdigit = num%10
       if lstdigit%2 ==1:
           cnt_odd = cnt_odd+1
       num = num//10
    return cnt_odd

print(count_odd_digits(890987))

def reverse_num(num):
    new_num =0
    while (num>0):
        ld = num % 10
        new_num  = (new_num * 10) + ld
        num = num//10
    return new_num

print(reverse_num(345890))

def palindrome(num):
    new_num =0
    o_num = num
    while (num>0):
        ld = num % 10
        new_num  = (new_num * 10) + ld
        num = num//10
    if new_num == o_num:
        return True
    else:
        return False
print(palindrome(1219))

def largest(n):
    ld = 0
    while(n>0):
        num = n % 10
        if num > ld:
            ld = num
        n = n //10
    return ld

print(largest(34567890))

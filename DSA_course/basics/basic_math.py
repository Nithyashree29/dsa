def count_digits(num):
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
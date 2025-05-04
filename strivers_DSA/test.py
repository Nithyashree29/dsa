def print1(n):
    for i in range(1,n):
        for j in range(1, i+1):
            print(j, end = "")
        print()

def print2(n):
    for i in range(1,n+1):
        for j in range(1, n+1):
            print(j, end = "")
        print()

def print3(n):
    for i in range(0, n):
        for j in range(0,i+1):
            print("*", end="")
        print()
        
def print4(n):
    for i in range(1,n+1):   
        for j in range(1,i+1):
            print(j, end= "")
        print()
            
def print5(n):
    for i in range(1,n+1):
        for j in range(n - i+1):
            print("*", end= "")
        print()
      
def print6(n):
    for i in range(1, n+1):
        for j in range(n-i+1):
            print(j+1, end="")
        print() 
def print7(n):
    for i in range(0, n):
        for j in range(0, n-i-1):
            print(" ", end="")
        for j in range(0,2*i-1):
            print("*", end="")
        for j in range(0, n-i-1):
            print(" ", end = "")
        print()

def print8(n):
    for i in range(0, n):
        for j in range(0, i):
            print(" ", end="")
        for j in range(0,2*n - (2*i+1)):
            print("*", end="")
        for j in range(0, i):
            print(" ", end = "")
        print()
   
def print10(n):
    for i in range(1, ((2*n)+1-1)):
        stars = i
 
        if i >= 5:
            stars = (2*n - i)
        for j in range(1,stars+1):
            print("*",end="")
             
        print()      
print1(5)
print("\n")
print2(5)
print("\n")
print3(5)
print("\n")
print4(5)
print("\n")
print5(5)
print("\n")
print6(5)
print("\n")
print7(5)
print("\n")
print8(5)
print("\n")
print10(5)
print("\n")
#Identifying patterns is the most important technique in problem solving.
# pattern 1
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# Rules - 1. Figure out the number of lines to be printed and write your outer loop on it.
#         2. Figure out whats happening at every line and try to connect with outer loop if possible.Write your inner loop on this basis.
#         3. Execute the print statements when needed.
#         4. Observe symmetry - Optional.
class Solution1:
    def pattern1(self, n):
        for i in range(0,n):  #outer loop
            for j in range(0,n):
                print("*", end = ' ')
            print()   
    # def main(self):
    #     N=4
    #     sol = Solution1()
    #     sol.pattern1(N)

    def pattern2(self, n):
        for i in range(n):
            for j in range(i+1):
                print('*', end=' ')
                print(i, end = ' ')
            print()
       
    def pattern3(self, n):
        for i in range(1, n+1):
            for j in range(1,i+1):
                print(j, end = '')
            print()
                 
    def pattern4(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(i, end='')
            print()
       
    def pattern5(self, n):
        for i in range(1, n+1):
            for j in range(i, n+1):  #n-i+
                print('*', end = '')
            print()   
       
    def pattern6(self, n):
        for i in range(1, n+1):
            for j in range(1, n+1-i+1):
                print(j, end = '')
            print()
        
    
    def pattern7(self,n):
        # n = n+1
        # for i in range(1, n):
        #     for j in range(1, n-i):
        #         print(' ',end ='')
        #     for j in range(1, 2*i+1-1):
        #         print("*",end ='')                
        #     for j in range(1, n-i):
        #         print(' ', end ='')
        #     print()
        for i in range(n):
            for j in range(n-i-1):
                print(" ", end='')
            for j in range(2*i+1):
                print("*", end='')
            print()
                  
    def pattern8(self, n):
        for i in range(n):
            for j in range(i):
                print(' ',end='')
            for j in range(0, 2*n - (2*i+1)):
                print('*',end ='')
            print()
    
    def pattern9(self, n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ", end='')
            for j in range(2*i+1):
                print("*", end='')
            print()
        for i in range(n):
            for j in range(i):
                print(' ',end='')
                
            for j in range(0, 2*n - (2*i+1)):
                print('*',end ='')
            print()
       
    def pattern10(self, n):
        start = 1
        for i in range(n):
            if i % 2 ==0 :
                start = 1
            else:
                start = 0
            for j in range(i+1):
                print(start, end =' ')
                start = 1- start
                
            print()     
     
    def pattern11(self, n):
        for i in range(1,n+1):
            for j in range(1, i+1):
                print(j, end='')
            for j in range(1, 2*n-2*i+1):
                print(' ', end='')

            for j in range(i, 0, -1):
                print(j, end ='')
            print()
                 
    
    def pattern12(self, n):
        val = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(val, end=' ')
                val = val+1
            print()
        
        
    def pattern13(self, n):
        for i in range(n):
            for j in range(ord('A'), ord('A')+i+1):
                print(chr(j), end='')
            print()
            
    def pattern14(self, n):
        for i in range(n):
            for j in range(ord('A'), ord('A')+n-i):
                print(chr(j), end='')
            print()                                            
                
    
    def pattern15(self, n):
        for i in range(n):
            ch = chr(ord('A')+i)
            for j in range(i+1):
                print(ch, end='')
            print()
            
    def pattern16(self, n):
        for i in range(n):
            for j in range(n-i-1):
                print(" ", end='') 
            ch = 'A'
            breakpoint = (2 * i + 1) //2
            # print(breakpoint)
            for j in range(1, 2 * i + 2):   #Based on i you can icreament and then decrement
                print(ch, end='')
                if j <= breakpoint:
                    ch = chr(ord(ch)+1)
                else:
                    ch = chr(ord(ch)-1)
            print()
                
    def pattern17(self, n):
        for i in range(n):
            for ch in range(ord('A') + n - 1 - i, ord('A') + n):
                print(chr(ch), end ='')
            print()
                
                
                
    def pattern18(self, n):
        for i in range(n):
            for j in range(n-i):
                print("*", end ='')
                
            for j in range(2*i):
                print(" ", end = '')
            for j in range(n-i):
                print("*", end ='')                
            print()     
        for i in range(n):
            for j in range(i+1):
                print("*", end ='') 
            for j in range(2*n-(2*i+4)+2):
                print(" ", end='')
            for j in range(i+1):
                print("*", end='')
            print()       
             
                
                
                
                
        
        
        
if __name__ == '__main__':
    p1 = Solution1()
    p1.pattern1(5)
    print()
    p1.pattern2(5)
    print()
    p1.pattern3(5)
    print()
    p1.pattern4(5)
    print()
    p1.pattern5(5)
    print() 
    p1.pattern6(5)
    print()
    p1.pattern7(5)
    print()
    p1.pattern8(5)
    print()
    p1.pattern9(5)
    print()
    p1.pattern10(5)
    print()
    p1.pattern11(5)
    print()
    p1.pattern12(5)
    print()
    p1.pattern13(5)
    print()
    p1.pattern14(5)
    print()
    p1.pattern15(5)
    print()
    p1.pattern16(4)
    print()
    p1.pattern17(5)
    print()   
    p1.pattern18(5)
    print()
    # p1.pattern19(5):
    #     print()

# pattern - 2






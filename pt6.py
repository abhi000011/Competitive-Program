# WAP to print Pattern

# *_ _ _ _ _*        
# *_ _ _ _*           
# *_ _ _*               
# *_ _*    
# *_*  
# *


n = int(input("Enter number of rows: "))
for i in range(n):
    print("*", end="")   
    if i != n - 1:   
        print(" " * (n - i - 1), end="")
        print("*")
    else:
        print()

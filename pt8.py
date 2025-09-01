# WAP to print Pattern

# * * * * *          
# _* * * *        
# _ * * *         
# _ _* *        
# _ _ * 


n = int(input("Enter rows: "))

for i in range(n, 0, -1):       
    for j in range(n - i):      
        print(" ", end="")
    for k in range(i):          
        print("* ", end="")
    print()

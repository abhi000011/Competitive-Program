# WAP to print Pattern

# 1  
# 1 *  
# 1 * 3  
# 1 * 3 *  
# 1 * 3 * 5  

n = int(input("Enter number :"))
for i in range(1, n+1):
    for j in range(1, i+1):
        if(j%2==0):
            print("*",end=" ")
        else:
            print(j,end=" ")
    print()

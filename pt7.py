# WAP to print Pattern

#  _ _ _ _*        
#  _ _ _ * *           
#  _ _  * * *           
#  _   * * * * 
#     * * * * *   

n = int(input("Enter rows: "))
for i in range(1, n+1):
    for j in range(n-i):
        print(" ", end="")
    for k in range(2*i-1):
        print("*", end="")
    print()

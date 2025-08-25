# 7. Take an integer A as input. You have to print the sum of all odd numbers in the range [1, A]. 

a = int(input("Enter the number : "))
sum = 0
for i in range(1,a):
    if(i%2!=0):
        sum = sum+i
        
print("Sum of odd no : ",sum,end=" ")
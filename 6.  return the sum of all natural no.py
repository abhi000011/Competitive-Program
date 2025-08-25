# 6. You are given an integer A, you need to find and return the sum of all the even numbers between 1 and A. Even numbers are those numbers that are divisible by 2. 

a = int(input("Enter the number : "))
sum = 0
for i in range(1,a):
    if(i%2==0):
        sum = sum+i
        
print("Sum of even no : ",sum,end=" ")
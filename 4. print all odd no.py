# 4. Write a program to print all odd numbers from 1 to N, where you have to take N as input from user. 

num = int(input("Enter the number : "))

if(num>0):
    for i in range(1,num+1):
        if(i%2!=0):
            print("Odd: ",i,end=" ")
else:
    print("Enter integer number...")
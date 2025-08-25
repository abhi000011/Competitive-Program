# Q- WAP to print all factors/divisor of a given +ve number.

num = int(input("Enter the number : "))

if(num>0):
    for i in range(1,num+1):
        print(i,end=" ")
else:
    print("Enter integer number...")



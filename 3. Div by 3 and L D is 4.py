# Q3- WAP to Check if a number is divisible by 3 and the last digit is 4.

num = int(input("Enter a number :"))
if (num%10==4 and num%3==0):
    print("YES")
else:
    print("NO")
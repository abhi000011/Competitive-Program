# 8. Take an integer N as input and print the count of digits of that number.

num = int(input("Enter the number : "))
digit=0
for i in range(num):
    if(num>0):
        num= num//10
        digit += 1
print(digit)    
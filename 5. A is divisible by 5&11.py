# Q5- Take an integer A as input.You have to tell wheather A is divisible by both 5 and 11 or not.

A= int(input("Enter any integer :"))
if (A%5==0 and A%11==0):
    print("This number is Divisibe")
else:
    print("This number will not dibisible by 5 and 11")
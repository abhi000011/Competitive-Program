# Q6- Read three integers and print their maximum.

a = int(input("Enter your A :"))
b = int(input("Enter your B :"))
c = int(input("Enter your C :"))
if (a >= b and a >= c):
    print("A is maximum")
elif(b>=c):
    print("B is maximum")
else:
    print("C is maximum")
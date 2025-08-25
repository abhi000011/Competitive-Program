# Write a program to input three numbers(A, B & C) from the user and print the minimum element among A, B & C. 
A =int(input("Enter first number: "))
B = int(input("Enter second number: "))
C = int(input("Enter third number: "))
if A < B and A < C:
    print("a is minimum")
elif B < A and B < C:
    print("b is minimum")
elif C < A and C < B:
    print("c is minimum")
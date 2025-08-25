# 10. You are given an integer A as input, and you need to determine whether it is a palindrome 
# or not. A palindrome integer is one whose digits, when reversed, result in the same number. 
# For example, 121 is a palindrome because its reverse is also 121, but 123 is not a palindrome 
# because its reverse is 321.Note: The given integer will not have any leading zeros. 

num = 12321
rev=0

for i in range(num):
    if(num>0):
        temp = num%10
        rev = rev*10+temp
        num = num//10
    if(num==rev):
            print("yes")
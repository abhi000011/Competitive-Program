# Q10- WAP to accept a number from 1 to 7 and display the name of the day, like 1 for Sunday, 2 for Monday, etc. 

num= int(input("Enter number between 1-7 :"))
if (num <= 0 or num >=8):
    print("ENTER NUMBER BETWEEN 1-7 ONLY")
if(num==1):
    print("SUNDAY")
elif(num==2):
    print("MONDAY")
elif(num==3):
    print("TUESDAY")
elif(num==4):
    print("WEDNESDAY")
elif(num==5):
    print("THURSDAY")
elif(num==6):
    print("FRIDAY")
elif(num==7):
    print("SATURDAY")
else:
    ("Thank u")

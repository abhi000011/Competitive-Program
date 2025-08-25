# 11. Take a number A as input, print its multiplication table having the first 10 multiples.

num = int(input("Enter the number : "))
tble=0
count=1
for i in range(count,11):
    if(count>0):
        tble = num*count
        print(f"{num} * {count} = ",tble)
        count+=1
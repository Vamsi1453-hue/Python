#write a python program to read an integer as input from the user and find the count of digits without using builtin functions
num = int(input("Enter an integer: "))
count = 0
rem=0
while(num!=0):
    rem=num%10
    count+=1
    num=num//10
print(f"The count of digits is: {count}")
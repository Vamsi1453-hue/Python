#write a python program to read three integer values and find largest number 
int1=int(input("Enter first number: "))
int2=int(input("Enter second number: "))
int3=int(input("Enter third number: "))
if int1>int2 and int1>int3:
    print(f"{int1} is the largest number.")
elif int2>int1 and int2>int3:
    print(f"{int2} is the largest number.")
else:
    print(f"{int3} is the largest number.")
    
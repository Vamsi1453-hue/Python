#write a python program to print reversed multiplication table of n 
num=int(input("Enter a number: "))
for i in range(10,0,-1):
    print(f"{num} x {i} = {num*i}")
    
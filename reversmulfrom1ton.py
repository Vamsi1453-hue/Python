#write a python program to print reversed multiplication tables from 1 to n
num=int(input("Enter a number: "))
for i in range(num,0,-1):
    print(f"Multiplication table of {i}:")
    print("------------------------------------------")
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")
    print()
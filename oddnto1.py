#write a python program to print odd numbers from 1 to n
n=int(input("Enter a number: "))
for i in range(1,n+1):
    if i%2!=0:
        print(i)
print("-"*35)
for i in range(1,n+1,2):
    print(i)
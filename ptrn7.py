n=int(input("Enter a value: "))
for i in range(1,n+1):
    for j in range(i,n+i):
        print(chr(j+64),end=" ")
    print()
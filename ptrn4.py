n=int(input("Enter the value: "))
for i in range(n,0,-1):
    for j in range(n):
        print(chr(96+i),end=" ")
    print()
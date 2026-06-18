n=int(input("Enter a value :"))
for i in range(n,0,-1):
    for j in range(n,0,-1):
        if (j<=i):
            print(chr(96+i),end=" ")
        else:
            print(" ",end=" ")
    print()
        
n=int(input("Enter a value :"))
k=1
for i in range(1,n+1):
    for j in range(n,0,-1):
        if (j<=i):
            print(chr(64+j),end=" ")
            k-=1
        else:
            print(" ",end=" ")
    print()
        
n=int(input("Enter a value :"))
for i in range(1,n+1):
    k=0
    for j in range(n,0,-1):
        if (j<=i):
            k=k+1
            print(f"{k}",end=" ")
        else:
            print(" ",end=" ")
    print()
        
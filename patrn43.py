n=int(input("Enter a value :"))
for i in range(1,n+1):
    for j in range(n,0,-1):
        k=1
        k=i*i
        if (j<=i):
            print(f"{k:2d}".format(k),end=" ")
        else:
            print("  ",end=" ")
    print()
        
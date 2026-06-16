n=int(input("Enter the value: "))
for i in range(n,0,-1):
    for j in range(1,n+1):
        print(f"{j}",end="")
    print()
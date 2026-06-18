n=int(input("Enter a value :"))
for i in range(n,0,-1):
    k=0
    for j in range(n,0,-1):
        if (j<=i):
            k+=1
            print(chr(96+k),end=" ")
        else:
            print("",end=" ")
    print()
        
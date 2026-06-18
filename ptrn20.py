n=int(input("Enter a value: "))
k=n
for i in range(n,0,-1):
    for j in range(n,0,-1):
        print(chr(k+96),end=" ")
        k-=1
    else: 
        print(" ",end=" ")
    print()
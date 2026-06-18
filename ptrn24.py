# alphabet patterns a b b c c c d d d d 
n=int(input("Enter a value: "))
for i in range(1,n+1):
    for j in range(n,0,-1):
        k=1
        k-=1
        print(chr(96+i),end=" ")
    print() 
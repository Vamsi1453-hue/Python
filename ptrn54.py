n=int(input("Enter the value: "))
num=0
for i in range(n,0,-1):
    for j in range(1,i+1):
        num+=1
        print(chr(num+64),end=" ")
    print()
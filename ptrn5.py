n=int(input("ENter the value:"))
k=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(f"{chr(k+64)} ",end="")
        if(k<=25):
            k+=1
        else:
            k=0
    print()
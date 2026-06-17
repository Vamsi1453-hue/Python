n = int(input("Enter a value: "))
for i in range(1, n+1):  
    for j in range(1, n+1):
        k=j*j   
        print("{:2d}".format(k), end=" ")
    print()

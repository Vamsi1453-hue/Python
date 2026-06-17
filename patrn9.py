n = int(input("Enter a value: "))
for i in range(1, n+1):
    k = i * i   
    for j in range(1, n+1):   
        print("{:2d}".format(k), end=" ")
    print()

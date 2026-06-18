n=int(input("enter a value: "))
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    for k in range(n-i):
        print("*", end=" ")
    print()

n = int(input("Enter the value: "))
for i in range(1, n+1):
    if i % 2 == 0:  
        for j in range(1, n+1):
            print(f"{i}", end=" ")
        print()

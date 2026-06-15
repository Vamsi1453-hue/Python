n = int(input("Enter: "))
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(j % 2, end=" ")
    print()
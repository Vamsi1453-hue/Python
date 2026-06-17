n = int(input("Enter the value: "))
num = 2
for i in range(1, n+1):
    for j in range(i):
        print(f"{num}", end=" ")
        num += 2
    print()

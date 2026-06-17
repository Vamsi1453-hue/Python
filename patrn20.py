n = int(input("Enter the value: "))
num = 2
for i in range(1, n+1):
    k = num * num
    for j in range(1, n+1):
        print(f"{k}", end=" ")
    print()
    num += 2

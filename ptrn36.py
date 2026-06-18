n = int(input("Enter a value: "))
for i in range(n, 0, -1):
    for s in range(n - i):
        print("", end=" ")
    for j in range(n, n - i, -1):
        print(chr(64 + j), end=" ")
    print()

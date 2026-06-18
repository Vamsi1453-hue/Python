n = int(input("Enter a value: "))
for i in range(n, 0, -1):
    print(" " * (n - i), end="")
    for j in range(n, n - i, -1):
        print(chr(96 + j), end=" ")
    print()

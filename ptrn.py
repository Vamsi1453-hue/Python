n = int(input("Enter how many lines: "))
for i in range(ord('E'), ord('E') + n):
    for j in range(i, i - 5, -1):
        print(chr(j), end=" ")
    print()

n = int(input("Enter rows: "))
for i in range(1, n+1):
    print(" " * (n - i) + " ".join(str(j % 2 == 0 and 1 or 0) for j in range(i)))

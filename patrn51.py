n = int(input("Enter rows: "))
for i in range(1, n+1):
    val = "1" if i % 2 else "0"
    print(" " * (n - i) + " ".join([val] * i))
